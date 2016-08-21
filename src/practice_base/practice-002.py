#!/user/bin/env python
#encoding:utf-8

'''
python核心编程第三章练习
'''
'''
3-1.为什么Python中不需要变量名和变量类型声明？ 
答案：Python语言中对象的类型和内存都是运行时确定的。在创建也就是赋值时，解释器会根据语法和右侧的操作数来决定新对象的类型。 
因为变量在第一次赋值的时候就被自动声明了。Python是无类型的语言。 
Python既是动态类型语言(因为它不使用显示数据类型声明，在运行期间才去确定数据类型)，
又是强类型语言(因为只要一个变量获得了一个数据，它就一直就是这个数据的数据类型)。  
3-2.为什么Python中不需要声明函数类型？ 
答案：函数没有定义返回的数据类型。Python不需要指定返回值的数据类型；甚至不需要指定是否有返回值。
实际上，每个Python函数都返回一个值；如果函数执行过return语句，它将返回指定的值，否则将返回None(Python的空值)

#python支持多元赋值
x,y,z = 1,2,3
print x,y,z
z,x,y = y,z,x
print x,y,z 
'''

#makeTextFile.py —— 创建文件
import os
ls = os.linesep  #字符串给出当前平台的行终止符，例如windows使用'\r\n,linux使用'\n',mac使用'\r'
 #使用局部变量代替模块变量：如果在一个函数中频繁使用一个属性，建议为该属性取一个本地变量别名

os.chdir(r"D:\files") #切换到目录文件

print'''
    1、创建文件
    2、读取文件
    '''
choice = input('请选择你要执行的功能编号')
#get filename
if choice ==1 :
    while True:
        fname = raw_input('请输入要创建的文件名称') 
        if os.path.exists('%s.txt' %fname): #判断目标路径，有没有重名的文件
            print '''ERROR:'%s.txt' already exists'''%fname
        else:
            break
            
    #get file content(text) lines    
    all = []
    print '''\nEnter lines('.' by itself too quit). \n'''#先换行，输入行信息，输入‘.’结束输入，换行
    
    
    #loop until user terminates input
    while True:
        entry = raw_input('请输入你要添加的信息>')
        if entry == '.':
            break
        else:
            all.append(entry)#将输入的信息插入到列表all中
    
    #write lines to file with proper line-ending
    fobj = open('%s.txt'%fname,'w')#创建文件，以只写模式打开
    fobj.writelines(['%s%s' %(x,ls) for x in all])#将all列表里数据写入到文件中，并按系统中的换行符进行换行
    fobj.close()#关闭文件
    print 'Done!'

#readtextfile.py:文件读取和显示
elif choice == 2:
    fname2 = raw_input('请输入要读取的文件名称') 
    try:
        fobj = open('%s.txt'%fname2,'r')
    except Exception,e:
        print '文件不存在',e
    else:
        for eachline in fobj:
            print eachline.strip('\n')
        fobj.close()
else:
    print '请重新输入'

