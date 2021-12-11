# demo
import tkinter as tk,os
from random import randint
from time import sleep

# 配置窗口
root = tk.Tk()
root_height_old = root.winfo_screenheight()
root_width_old = root.winfo_screenwidth()
root_height = (root_height_old - 400)// 2
root_width = (root_width_old - 400) // 2
root.geometry('400x400+{}+{}'.format(root_width, root_height))
root.wm_attributes('-topmost',1)

if os.path.exists('NameList.txt'):
    Tem = open('NameList.txt',encoding='utf-8')
    TemLst = Tem.readlines()
    Tem.close()
    People = [i.strip() for i in TemLst]
    # 函数
    def begin():
        size = [30,35,40,43]
        global People
        global Display
        user = randint(0,len(People)-1)
        for i in People:
            Display.place_forget()
            Display = tk.Label(root, text=i, font=("Consolas",30,"bold"))
            Display.place(x=80, y=130)
            sleep(0.05)
            root.update()
        num = 0.2
        for i in range(4):
            Display.place_forget()
            Display = tk.Label(root, text=People[i], font=("Consolas",30,"bold"))
            Display.place(x=80, y=130)
            sleep(num)
            num += 0.2
            root.update()
        for i in size:
            Display.place_forget()
            Display = tk.Label(root, text=People[user], font=("Consolas",i,"bold"))
            Display.place(x=80, y=130)
            sleep(0.3)
            root.update()
    Display = tk.Label(root, text="还没有\n抽过", font=("Consolas",30, "bold"))
    Display.place(x=80,y=130)
        
    Begin = tk.Button(root, text="开\n\n始", font=("Consolas", 20, 'bold'), height=8, command=begin)
    Begin.place(x=300, y=50)
else:
##    print("Error: File NameList.txt not found")
    Error = tk.Label(root, text='Error:\nFile NameList.txt not found', font=("Consolas",18))
    Error.pack(expand='yes')

root.mainloop()
