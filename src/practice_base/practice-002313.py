#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
3–13. 添加新功能。将你上一个问题改造好的 readNwriteTextFiles.py 增加一个新功
能：允许用户编辑一个已经存在的文本文件。 你可以使用任何方式，无论是一次编辑一行，还
是一次编辑所有文本。需要提醒一下的是，一次编辑全部文本有一定难度，你可能需要借助 GUI 
工具包或一个基于屏幕文本编辑的模块比如 curses模块。要允许用户保存他的修改（保存到
文件）或取消他的修改（不改变原始文件），并且要确保原始文件的安全性（不论程序是否正
常关闭）。

答：使用了Tkinter  ,platform 
注：初学者可能不容易掌握
'''

from Tkinter import *
import tkMessageBox,tkFileDialog
import platform
 
# nl = os.linesep
 
def openfile():
    global filename             # 使用global声明为全局变量，方便后边的程序调用
    systype = platform.system() # 判断系统类型
    if systype == 'windows':
        basedir = 'c:\\'
    else:
        basedir = '/'
        filename = tkFileDialog.askopenfilename(initialdir=basedir)
    try:
        fobj_r = open(filename, 'r')
    except IOError, errmsg:
        print '*** Failed open file:', errmsg
    else:
        editbox.delete(1.0, END)
        for eachline in fobj_r:
            editbox.insert(INSERT, eachline)
        fobj_r.close()

def savefile():
    save_data = editbox.get(1.0, END)
    try:
        fobj_w = open(filename, 'w')
        fobj_w.writelines(save_data.encode('utf-8')) # 感谢OSC-骠骑将军 指教
        fobj_w.close()
        tkMessageBox.showinfo(title='提示',message='保存成功')
    except IOError, errmsg:
        tkMessageBox.showwarning(title='保存失败', message='保存出错    ')
        tkMessageBox.showwarning(title='错误信息', message=errmsg)
    except NameError:
        tkMessageBox.showwarning(title='保存失败', message='未打开文件')
    def showlinenum():
        tkMessageBox.showinfo(title='提示',
        message='这个功能作者现在不会写,放这里装饰用的.')
def destroy_ui(ui):
    ui.destroy()
    
def aboutauthor():
    author_ui = Toplevel()
    author_ui.title('关于')
    author_ui.geometry('200x80')
    about_string = Label(author_ui,text="作者: ToughGuy\n\n主页: http://www.techzhai.net/")
    confirmbtn = Button(author_ui, text='确定',command=lambda:destroy_ui(author_ui))
    about_string.pack()
    confirmbtn.pack()
    # author_ui.mainloop()
    
def CreateMenus():
      # 初始化菜单
    Menubar = Menu(root)
    
     # 创建文件菜单
    filemenu = Menu(Menubar, tearoff=0)
    filemenu.add_command(label='打开文件', command=openfile)
    filemenu.add_command(label='保存文件', command=savefile)
    filemenu.add_command(label='退出', command=lambda:destroy_ui(root))
    Menubar.add_cascade(label='文件', menu=filemenu)
    
      # 创建编辑菜单
    editmenu = Menu(Menubar, tearoff=0)
    editmenu.add_command(label='显示行号', command=showlinenum)
    Menubar.add_cascade(label='编辑', menu=editmenu)
    
     # 创建帮助菜单
    helpmenu = Menu(Menubar, tearoff=0)
    helpmenu.add_command(label='关于作者', command=aboutauthor)
    Menubar.add_cascade(label='帮助', menu=helpmenu)
    root.config(menu=Menubar)
    
root = Tk()
root.title('文本编辑器')
root.geometry('500x400')
CreateMenus()
editbox = Text(root, width=70, height=25, bg='white')
editbox.pack(side=TOP, fill=X)
root.mainloop()