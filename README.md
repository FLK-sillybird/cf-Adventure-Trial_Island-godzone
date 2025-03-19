# cf-Adventure-Trial_Island-godzone
帮助cf试炼岛玩家进行低星卡自动放、刷卡，解放双手

版本更新了！！！
## 之前存在的问题：
1. 程序代码冗余，召唤逻辑都一样，却有四个脚本文件。措施：2.0将会大改，增加config文件，在config文件全局配置开枪时间，等待时间，换子弹方法等
2. 程序运行过程中中止麻烦，需要回到代码编辑器使用ctrl+c强制停止。措施：后期增加监听全局中止键，比如按q停止程序

解决措施：
新增config文件，在config文件全局配置开枪时间，等待时间等
新增按q键终止程序
增加用户可交互界面，通过配置菜单，用户可自由修改点击位置，开枪时间等

主界面：

![image](https://github.com/user-attachments/assets/cc9941c7-e6fe-416f-8892-6bcc3c2ec7ff)

配置界面：

![image](https://github.com/user-attachments/assets/73c53309-e54e-411d-9ab3-65b3da83b5f5)

以寒霜为例，修改配置参数

![image](https://github.com/user-attachments/assets/ab7c677b-12ca-4ed5-843e-b08518b84ffe)

参数解释：
1star -x ： 选择星级(一星)在屏幕x坐标， y ：选择星级(一星)在屏幕y坐标；
2star -x ： 选择星级(二星)在屏幕x坐标， y ：选择星级(二星)在屏幕y坐标；
card -x ： 一星卡片在屏幕x坐标，y：一星卡片在屏幕y坐标；
confirm -x ：确认键在屏幕x坐标， y：确认键在屏幕y坐标；

one_star:    单位都是秒
waitForDuration：一星boss召唤完等待时间
cartridge_change_time： 枪械换弹时间
time2kill：开枪持续时间
waitTime：一星boss死亡等待召唤柱能重新召唤时间

two_star:
waitForDuration：二星boss召唤完等待时间
cartridge_change_time： 枪械换弹时间
time2kill：开枪持续时间
waitTime：二星boss死亡等待召唤柱能重新召唤时间

## 代码主要框架
不哔哔了，说了你也不懂

## 使用方法
在代码路径打开黑窗口（命令提示符，操作方法：文件资源管理器地址栏输入cmd），输入命令.\venv\Scripts\python.exe run.py打开程序界面（如下图），等待游戏试炼岛开局，玩家自行前往召唤柱，在可视化界面选择相应的boss和星级，填写消耗的卡数，点击确认执行，即可自动召唤和攻击。按q键终止，在黑窗口可以显示召唤了多少张卡。
![image](https://github.com/user-attachments/assets/88bba082-47f8-46fb-9b04-457dcb6a1a77)


## 使用须知
boss的召唤流程都一致。玩家必须自行前往boss召唤柱，不能跑图，游戏窗口全屏，游戏内分辨率使用1024*768，使用枪械任意，如果限时内不能击杀boss，自己更改time2kill时间。

## 目前存在的问题：
不知道，暂时使用一个星期

