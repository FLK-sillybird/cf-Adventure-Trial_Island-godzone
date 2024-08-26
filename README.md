# cf-Adventure-Trial_Island-godzone
帮助cf试炼岛玩家进行低星卡自动放、刷卡，解放双手
  
![image](https://github.com/user-attachments/assets/003acd61-8291-4ecc-83f4-4c7d8e2094b9)


## 代码主要框架包括两部分
第一部分在run.py文件，其作用是构建一个可视化界面，给用户选择相应的boss以及消耗的卡数。
第二部分是tools文件夹下的几个boss召唤方法，四个boss方法大同小异，主要区别在于boss血量不同以及玩家伤害不同导致击杀时间不一致，还有boss死亡后到能重新召唤的时间不同。如果玩家不能召唤或者不能完全击杀boss，请自行修改对应文件下的时间

## 程序逻辑
四个boss的召唤流程都一致，玩家必须自行前往boss召唤柱，游戏窗口全屏，分辨率使用1024*768，目前版本必须使用aa12-擎天柱（因为擎天柱右键两下能更换子弹，其他枪械暂未发现用鼠标更换子弹，作者测试，脚本按r不能更换子弹，原因待查明）

## 使用方法
开局后，玩家自行前往召唤柱，启动run.py，在可视化界面选择相应的boss，填写消耗的卡数，点击确认执行，然后在一秒内（时间玩家自己定义）回到cf客户端，即可自动召唤和攻击。注：召唤的星级是你按e那个界面的星级，即，如果想要修改星级，在确认执行之前，按e调到想要的星级界面。（一般都是一星二星吧，有人用脚本放高星？？？）

## 目前存在的问题：
1. 程序代码冗余，召唤逻辑都一样，却有四个脚本文件。措施：2.0将会大改，增加config文件，在config文件全局配置开枪时间，等待时间，换子弹方法等
2. 程序运行过程中中止麻烦，需要回到代码编辑器使用ctrl+c强制停止。措施：后期增加监听全局中止键，比如按q停止程序


## 程序需要的环境及package
  python>=3.7
  pyautogui
  time
  tkinter 

## 若新手用户遇到 No module named “***”问题，使用pip install *** 安装即可
