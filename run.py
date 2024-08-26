import tkinter as tk
from tkinter import ttk
from tools.ansha import ansha
from tools.daxiong import daxiong
from tools.juren import juren
from tools.hanshuang import hanshuang
class ContactAuthorApp:
	def __init__(self, root):
		self.root = root
		self.root.title("试炼岛刷卡v1.0   有问题联系作者1915616162")
		self.power_var = tk.StringVar()
		self.entry = None
		self.init_widgets()
		self.methods = {
				"寒霜": self.method_frost,
				"暗杀": self.method_assassination,
				"大熊": self.method_bear,
				"巨人": self.method_giant
		}
	def method_frost(self, number):
		hanshuang(number)


		print(f"执行寒霜方法，消耗卡片数量: {number}")

	def method_assassination(self, number):
		ansha(number)
		print(f"执行暗杀方法，消耗卡片数量: {number}")

	def method_bear(self, number):
		
		daxiong(number)
		print(f"执行大熊方法，消耗卡片数量: {number}")

	def method_giant(self, number):
		juren(number)
		print(f"执行巨人方法，消耗卡片数量: {number}")
	
	def init_widgets(self):
		# 创建单选按钮
		for power in ["寒霜", "暗杀", "大熊", "巨人"]:
			ttk.Radiobutton(self.root, text=power, value=power, variable=self.power_var).pack(side="top" ,anchor='w')
		# 创建提示标签
		label = ttk.Label(self.root, text="请输入需要消耗的卡片数量:")
		label.pack()
		# 创建输入框
		self.entry = tk.Entry(self.root)
		self.entry.pack()
		# 为了让按钮在新的一行，我们添加一个填充
		ttk.Separator(self.root).pack(fill='x', padx=10, pady=10)
		# 创建确认和取消按钮
		confirm_button = tk.Button(self.root, text="确认执行", command=self.on_confirm)
		confirm_button.pack(side='left', padx=10)
		cancel_button = tk.Button(self.root, text="取消", command=self.root.destroy)
		cancel_button.pack(side='right')
	def on_confirm(self):
		# 获取单选按钮的选择
		selected_power = self.power_var.get()
		# 获取输入框的内容
		input_text = self.entry.get()
		# 检查输入内容是否为正整数
		if self.is_positive_integer(input_text):
			# 在这里你可以处理数字输入和单选按钮的选择
			print(f"Selected power: {selected_power}")
			print(f"Entered number: {input_text}")
			method = self.methods.get(selected_power)
			if method:
			# 调用方法并传递卡片数量
				method(int(input_text))
			else:
				tk.messagebox.showerror("错误", "未找到对应的方法。")
			# TODO: 执行进一步的操作
		else:
			# 弹出错误消息
			tk.messagebox.showerror("错误", "请输入有效的正整数卡片数量。")
	@staticmethod
	def is_positive_integer(s):
		try:
			value = int(s)
			return value > 0
		except ValueError:
			return False
	def run(self):
		# 设置窗口大小并居中
		window_width = 500
		window_height = 300
		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()
		center_x = int((screen_width - window_width) / 2)
		center_y = int((screen_height - window_height) / 2)
		self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
		# 运行主循环
		self.root.mainloop()


def main():
	# 创建主窗口
	root = tk.Tk()

	# 创建应用程序实例
	app = ContactAuthorApp(root)

	# 运行应用程序
	app.run()

if __name__ == "__main__":
	main()
