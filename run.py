import tkinter as tk
from tkinter import ttk, messagebox
import json
import sys
from action import action

# 新增 ConfigManager 类
class ConfigManager:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        try:
            # 添加配置文件存在时但内容为空的情况处理
            with open('config/config.json', 'r', encoding='utf-8') as f:
                config = json.load(f)
                if not config:
                    raise ValueError("配置文件内容为空")
                return config
        except FileNotFoundError:
            messagebox.showerror("错误", "配置文件未找到。")
            print("错误: 配置文件未找到。")
            return {}
        except json.JSONDecodeError as e:
            messagebox.showerror("错误", f"配置文件解析错误: {e}")
            print(f"错误: 配置文件解析错误: {e}")
            return {}
        except Exception as e:
            messagebox.showerror("错误", f"加载配置文件时出现未知错误: {e}")
            print(f"错误: 加载配置文件时出现未知错误: {e}")
            return {}

    # 修改保存方法，移除GUI相关操作
    def save_config(self, power, new_config):
        try:
            if power not in self.config:
                raise ValueError(f"未找到 {power} 的配置项")
            # 直接更新配置数据
            self.config[power] = new_config
            # 将更新后的配置保存到文件
            with open('config/config.json', 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=4)
            print(f"已保存 {power} 的配置")
            return True
        except Exception as e:
            print(f"保存配置错误: {e}")
            return False

class ContactAuthorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("tkinter")
        self.power_var = tk.StringVar()
        self.star_var = tk.StringVar(value="一星")
        self.entry = None
        # 初始化 ConfigManager 实例
        self.config_manager = ConfigManager()
        self.config = self.config_manager.config
        self.init_sidebar()
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(pady=10)
        self.init_widgets()
        # 添加一个全屏标志
        self.is_fullscreen = False
        # 绑定 F11 键用于切换全屏
        self.root.bind("<F11>", self.toggle_fullscreen)
        # 绑定 ESC 键用于退出全屏
        self.root.bind("<Escape>", self.exit_fullscreen)
        # 监听窗口大小变化事件，判断是否进入或退出全屏
        self.root.bind("<Configure>", self.on_window_configure)

        # 增强异常回调处理
        def handle_exception(exc_type, exc_value, exc_traceback):
            error_msg = f"未处理的异常: {exc_type.__name__}: {exc_value}"
            print(error_msg)
            import traceback
            traceback.print_tb(exc_traceback)
            # 在GUI线程中显示错误
            self.root.after(0, lambda: messagebox.showerror("严重错误", "程序遇到意外错误，请检查日志"))
        self.root.report_callback_exception = handle_exception

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)
        if self.is_fullscreen:
            messagebox.showinfo("提示", "已进入全屏模式")
        else:
            messagebox.showinfo("提示", "已退出全屏模式")

    def exit_fullscreen(self, event=None):
        self.is_fullscreen = False
        self.root.attributes("-fullscreen", False)
        messagebox.showinfo("提示", "已退出全屏模式")

    def on_window_configure(self, event):
        if self.root.attributes("-fullscreen") and not self.is_fullscreen:
            self.is_fullscreen = True
            messagebox.showinfo("提示", "已进入全屏模式")
        elif not self.root.attributes("-fullscreen") and self.is_fullscreen:
            self.is_fullscreen = False
            messagebox.showinfo("提示", "已退出全屏模式")

    def show_config_edit(self, power=None):
        self.clear_main_frame()  # 清除主界面内容
        try:
            
            power_var = tk.StringVar(value=power)
            # 在下拉框创建前添加空值保护
            power_options = list(self.config.keys())
            if not power_options:
                return

            # 创建下拉框时增加异常捕获
            try:
                power_menu = ttk.OptionMenu(
                    self.main_frame, 
                    power_var,
                    power,
                    *power_options,
                    command=lambda p: self.root.after(100, lambda: self._show_config_and_expand(p))
                )
                power_menu.pack(pady=10)
                # self.sidebar.selection_set(child_item)
            except tk.TclError as e:
                print(f"下拉框创建失败: {str(e)}")
                return

            # Display the detailed information of the selected configuration
            title_label = ttk.Label(self.main_frame, text=f"参数配置详情 - {power}")
            title_label.pack(pady=10)

            # 在创建输入框时添加引用存储
            input_data = {
                "click_positions": {},
                "sleep_times": {}
            }

            # Display the click position parameters
            click_positions = self.config[power]["click_positions"]
            for pos_key, pos_value in click_positions.items():
                # print(pos_key,pos_value)
                pos_frame = ttk.Frame(self.main_frame)
                pos_frame.pack()
                position_label = ttk.Label(pos_frame, text=f"{pos_key} - x:")
                position_label.pack(side='left')
                x_entry = ttk.Entry(pos_frame, width=10)
                x_entry.insert(0, pos_value['x'])
                x_entry.pack(side='left', padx=5)
                # 显示点击位置的 y 坐标标签
                y_label = ttk.Label(pos_frame, text="y:")
                # 优化：将 y 坐标标签左对齐
                y_label.pack(side='left')
                # 显示点击位置的 y 坐标输入框
                y_entry = ttk.Entry(pos_frame, width=10)
                y_entry.insert(0, pos_value['y'])
                y_entry.pack(side='left', padx=5)
                input_data["click_positions"][pos_key] = (x_entry, y_entry)  # 添加这行

            # Display the sleep time parameters
            sleep_times = self.config[power]["sleep_times"]
            for star_key, star_value in sleep_times.items():
                star_label = ttk.Label(self.main_frame, text=f"{star_key}:")
                star_label.pack()
                input_data["sleep_times"][star_key] = {}  # 移动到外层循环初始化
                for time_key, time_value in star_value.items():
                    time_frame = ttk.Frame(self.main_frame)
                    time_frame.pack()
                    time_label = ttk.Label(time_frame, text=f"{time_key}:")
                    time_label.pack(side='left')
                    time_entry = ttk.Entry(time_frame, width=10)
                    time_entry.insert(0, time_value)
                    time_entry.pack(side='left', padx=5)
                    input_data["sleep_times"][star_key][time_key] = time_entry  # 直接存储entry引用

            # 修改保存按钮命令
            save_button = ttk.Button(
                self.main_frame,
                text="保存",
                command=lambda p=power: self._handle_save(p, input_data)  # 使用闭包捕获当前power值
            )
            save_button.pack(pady=10)

        except Exception as e:
            print(f"Error in show_config_edit: {e}")

    def _handle_save(self, power, input_data):
        """处理保存操作，实时获取输入框值"""
        try:
            new_config = {
                "click_positions": {},
                "sleep_times": {}
            }
            
            # 验证坐标数据（必须为整数）
            for pos_key, (x_entry, y_entry) in input_data["click_positions"].items():
                try:
                    x = int(x_entry.get())
                    y = int(y_entry.get())
                except ValueError:
                    raise ValueError(f"{pos_key} 坐标必须为整数")
                
                new_config["click_positions"][pos_key] = {"x": x, "y": y}
            
            # 验证时间数据（可以是整数或浮点数）
            for star_key, times in input_data["sleep_times"].items():
                new_config["sleep_times"][star_key] = {}
                for time_key, entry in times.items():
                    try:
                        value = float(entry.get())
                    except ValueError:
                        raise ValueError(f"{star_key}.{time_key} 必须为数字")
                        
                    new_config["sleep_times"][star_key][time_key] = value
            
            # 调用保存方法
            if self.config_manager.save_config(power, new_config):
                messagebox.showinfo("提示", "配置已保存。")
            else:
                messagebox.showerror("错误", "保存失败，请检查日志")
                
        except ValueError as ve:
            messagebox.showerror("验证错误", str(ve))
        except Exception as e:
            messagebox.showerror("错误", f"发生未知错误: {str(e)}")
    
    def show_config_overview(self):
        # 显示所有配置的简要信息
        title_label = ttk.Label(self.main_frame, text="配置项列表", font=("微软雅黑", 12, "bold"))
        title_label.pack(pady=10)
        for key in self.config.keys():
            # 创建一个标签显示配置项
            label = ttk.Label(self.main_frame, text=key)
            label.pack()
            # 为标签绑定点击事件，点击时调用 show_config_edit 方法，并展开配置子菜单
            label.bind("<Button-1>", lambda event, power=key: self._show_config_and_expand(power))

    def _show_config_and_expand(self, power):
        
        # 找到配置项的 iid 并展开它
        # print("从配置主页面点击")
        for item in self.sidebar.get_children():
            if self.sidebar.item(item, "text") == "配置":
                config_iid = item
                self.sidebar.item(config_iid, open=True)  # 展开配置菜单
                for child_item in self.sidebar.get_children(config_iid):
                    if self.sidebar.item(child_item, "text") == power:
                        # print(child_item)
                        self.sidebar.selection_set(child_item)  # 选中对应子项
                        break
        # print(power)#power是在配置界面点击的那几个链接
        self.show_config_edit(power)

    def init_sidebar(self):
        self.sidebar = ttk.Treeview(self.root, columns=(), show='tree')
        self.sidebar.pack(side='left', fill='y')

        # 添加一级菜单
        top_items = ["启动", "配置", "设置", "关于"]
        config_iid = None  # 用于保存配置项的 iid
        for item in top_items:
            iid = self.sidebar.insert('', 'end', text=item)
            if item == "配置":
                config_iid = iid  # 保存配置项的 iid

        # 添加配置的二级菜单
        if config_iid:
            for key in self.config.keys():
                child_iid = self.sidebar.insert(config_iid, 'end', text=key)
                # 为二级菜单绑定点击事件
                self.sidebar.tag_bind(child_iid, "<<TreeviewSelect>>", lambda event, power=key: self.show_config_edit(power))
        self.sidebar.bind("<<TreeviewSelect>>", self.on_sidebar_select)

    def clear_main_frame(self):
        # Destroy all widgets in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def on_sidebar_select(self, event):
        selected_item = self.sidebar.selection()
        if selected_item:
            item_text = self.sidebar.item(selected_item, "text")
            print(f"你点击了: {item_text}")
            self.clear_main_frame()
            if item_text == "启动":
                self.init_widgets()
            elif item_text == "配置":
                # 显示配置的二级菜单
                self.show_config_overview()
            elif item_text == "设置":
                self.show_settings()
            elif item_text == "关于":
                self.show_about()
            elif item_text in self.config.keys():
                self.show_config_edit(item_text)

    def on_config_sidebar_select(self, event, sidebar, edit_frame):
        selected_item = sidebar.selection()
        if selected_item:
            item_text = sidebar.item(selected_item, "text")
            # 清除编辑区域内容
            for widget in edit_frame.winfo_children():
                widget.destroy()

            if item_text == "click_positions":
                # 显示点击位置的参数
                for power, config in self.config.items():
                    ttk.Label(edit_frame, text=f"{power} - {item_text}").pack()
                    for pos_key, pos_value in config[item_text].items():
                        x_label = ttk.Label(edit_frame, text=f"{pos_key} - x:")
                        x_label.pack(side='left')
                        x_entry = ttk.Entry(edit_frame, width=10)
                        x_entry.insert(0, pos_value["x"])
                        x_entry.pack(side='left', padx=5)
                        y_label = ttk.Label(edit_frame, text="y:")
                        y_label.pack(side='left')
                        y_entry = ttk.Entry(edit_frame, width=10)
                        y_entry.insert(0, pos_value["y"])
                        y_entry.pack(side='left', padx=5)
                        ttk.Label(edit_frame, text=" ").pack(side='left')
                    ttk.Label(edit_frame, text=" ").pack()

            elif item_text == "sleep_times":
                # 显示休眠时间的参数
                for power, config in self.config.items():
                    ttk.Label(edit_frame, text=f"{power} - {item_text}").pack()
                    for star_key, star_value in config[item_text].items():
                        ttk.Label(edit_frame, text=f"{star_key}:").pack()
                        for time_key, time_value in star_value.items():
                            time_label = ttk.Label(edit_frame, text=f"{time_key}:")
                            time_label.pack(side='left')
                            time_entry = ttk.Entry(edit_frame, width=10)
                            time_entry.insert(0, time_value)
                            time_entry.pack(side='left', padx=5)
                        ttk.Label(edit_frame, text=" ").pack()
                    ttk.Label(edit_frame, text=" ").pack()

    def show_settings(self):
        resolution_label = ttk.Label(self.main_frame, text="分辨率:")
        resolution_label.pack(pady=10)
        resolution_entry = ttk.Entry(self.main_frame, width=20)
        resolution_entry.pack(pady=5)

        def save_settings():
            resolution = resolution_entry.get()
            if resolution:
                messagebox.showinfo("提示", f"分辨率设置为 {resolution}。")

        save_button = ttk.Button(self.main_frame, text="保存", command=save_settings)
        save_button.pack(pady=10)

    def show_about(self):
        about_text = """\
        注：被封号概不负责！！！
        本项目自有代码使用宽松的MIT协议，在保留版权信息的情况下可以自由应用于各自商用、非商业的项目。 
        但是本项目也零碎的使用了一些其他的第三方库，由于使用本项目而产生的商业纠纷或侵权行为一概与本项目及开发者无关，请自行承担法律风险。 
        在使用本项目代码时，也应该在授权协议中同时表明本项目依赖的第三方库的协议，以及遵循相应的规定。   ---抄别人的readme
        """
        about_label = ttk.Label(self.main_frame, text=about_text, justify='left', wraplength=self.main_frame.winfo_width())
        about_label.pack(pady=20)
        # 绑定窗口大小变化事件，更新 wraplength
        configure_id = self.main_frame.bind("<Configure>", lambda event: about_label.config(wraplength=event.width))

        def unbind_configure():
            self.main_frame.unbind("<Configure>", configure_id)

        # 绑定销毁事件，在销毁前解绑配置事件
        about_label.bind("<Destroy>", lambda event: unbind_configure())

    def execute_action(self, power, number, star_level):
        try:
            config = self.config.get(power)
            if not config:
                messagebox.showerror("错误", "未找到对应的配置。")
                return
            star_key = "one_star" if star_level == "一星" else "two_star"
            sleep_times = config['sleep_times'][star_key]
            click_positions = config['click_positions']
            
            # 添加窗口激活异常处理
            card_num = action(number, sleep_times, click_positions, star_key)
            print(f'消耗了{card_num}张卡')
        except Exception as e:
            if "SetForegroundWindow" in str(e):
                messagebox.showerror("错误", "请先打开游戏窗口！")
            else:
                messagebox.showerror("执行错误", f"操作失败: {str(e)}")

    def init_widgets(self):
        options_frame = ttk.Frame(self.main_frame)
        options_frame.pack(pady=10)
        # 假设这几个选项在配置中存在
        # powers = ["寒霜", "暗杀", "大熊", "巨人", "禁区大熊"]

        for idx, power in enumerate(self.config.keys()):
            rb = ttk.Radiobutton(
                options_frame,
                text=power,
                value=power,
                variable=self.power_var,
            )
            rb.pack(side='left', padx=5)  # 使用 side='left' 使单选按钮水平排列

        # 下拉框所在的框架
        dropdown_frame = ttk.Frame(self.main_frame)
        dropdown_frame.pack(pady=10)

        menubutton = ttk.Menubutton(
            dropdown_frame,
            textvariable=self.star_var,
            width=10,
        )
        menu = tk.Menu(menubutton, tearoff=0)
        menubutton["menu"] = menu
        options = ["一星", "二星"]
        for option in options:
            menu.add_radiobutton(label=option, value=option, variable=self.star_var)
        menubutton.pack(anchor='w')  # 下拉框显示在新的一行

        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(pady=10)
        label = ttk.Label(input_frame, text="请输入需要消耗的卡片数量:")
        label.pack(side='left')
        self.entry = ttk.Entry(input_frame, width=10)
        self.entry.pack(side='left', padx=5)
        ttk.Separator(self.main_frame).pack(fill='x', padx=10, pady=10)
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=10)
        confirm_button = ttk.Button(button_frame, text="确认执行", command=self.on_confirm, width=15)
        confirm_button.pack(side='left', padx=10)
        cancel_button = ttk.Button(button_frame, text="取消", command=self.root.destroy, width=15)
        cancel_button.pack(side='right', padx=10)

    def on_confirm(self):
        selected_power = self.power_var.get()
        star_level = self.star_var.get()
        input_text = self.entry.get()
        if self.is_positive_integer(input_text):
            number = int(input_text)
            self.execute_action(selected_power, number, star_level)
        else:
            messagebox.showerror("错误", "请输入有效的正整数卡片数量。")

    @staticmethod
    def is_positive_integer(s):
        try:
            value = int(s)
            return value > 0
        except ValueError:
            return False

    def run(self):
        window_width = 600
        window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        # 允许窗口大小调整
        self.root.resizable(True, True)
        self.power_var.set(next(iter(self.config.keys())))
        self.entry.insert(0, "1")
        self.root.mainloop()


def main():
    def handle_global_exception(exc_type, exc_value, exc_traceback):
        print(f"Global unhandled exception: {exc_type.__name__}: {exc_value}")
        import traceback
        traceback.print_tb(exc_traceback)
        messagebox.showerror("错误", f"发生全局未处理异常: {exc_type.__name__}: {exc_value}")

    sys.excepthook = handle_global_exception
    root = tk.Tk()
    app = ContactAuthorApp(root)
    app.run()


if __name__ == "__main__":
    main()