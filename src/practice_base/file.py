#!/user/bin/env python
#encoding:utf-8

import os
import stat
import shutil #高级文件操作模块

#一、python中对文件、文件夹操作时经常用到的os模块和shutil模块常用方法
#os.getcwd()得到当前工作目录，即当前Python脚本工作的目录路径结果：D:\pythonWorkspace\oneClass\python_practice\src\practice_base
print os.getcwd() 
#os.listdir返回指定目录下的所有文件和目录名,以列表形式展现 ['aa', 'aaaa.txt', 'accounts.txt', 'account_lock.txt']
print os.listdir(r'D:\files')
#os.path.isfile()检测给出的文件是否一个文件，False
print os.path.isfile("D:\files")
#os.path.isdir()检测给出的文件是否一个目录，False
print os.path.isdir("D:\files")
#os.path.isabs()检测是否绝对路径，False
print os.path.isabs("D:\files")
#os.path.exists()判断此路径、文件是否存在
print os.path.exists(r'D:\files')#True
print os.path.exists(r'D:\files\aaaa.txt')#True
#os.path.split() 返回一个路径的目录名和文件名:
print os.path.split(r'D:\files') #结果：('D:\\', 'files')
print os.path.split(r'D:\files\aaaa.txt')#结果：('D:\\files', 'aaaa.txt')
#os.path.splitext()分离扩展名
print os.path.splitext(r'D:\files') #结果：('D:\\files', '')
print os.path.splitext(r'D:\files\aaaa.txt') #结果('D:\\files\\aaaa', '.txt')
#os.path.dirname()获取路径名
print os.path.dirname(r'D:\files') #结果D:\
print os.path.dirname(r'D:\files\aaaa.txt') #结果D:\files
#os.path.basename()获取文件名
print os.path.basename(r'D:\files\aaaa.txt') #结果aaaa.txt
print os.path.basename(r'D:\files')  #结果files
#os.system()运行shell命令
#os.system(r'ping 192.168.0.1') #返回值是脚本的退出状态码,只是调用，调用完后自身退出，可能返回个0吧
#os.popen('cmd') 返回值是脚本执行过程中的输出内容,可以实现一个“管道”，从这个命令获取的值可以继续被调用
#得到ntpd的进程id：os.popen('ps -C ntpd | grep -v CMD |awk '{ print $1 }').readlines()[0]
#读取和设置环境变量os.getenv()与os.putenv()
print os.getenv('path')
#给出当前平台使用的行终止符:os.linesep 
print  os.linesep
#os.name指示你正在使用的平台, 对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
print os.name


#os.stat(file)获取文件属性
print os.stat(r'D:\files\bbbb.txt') #结果：nt.stat_result(st_mode=33206, st_ino=0L, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=713L, st_atime=1469505047L, st_mtime=1469293894L, st_ctime=1469505047L)
#os.chmod(path,mode)修改文件权限与时间戳,需要导入stat模块
#print os.chmod(r'D:\files\bbbb.txt', stat.S_IXGRP)
#os.exit()中止当前进程：os._exit() 直接退出 Python程序，其后的代码也不会继续执行
#sys.exit() 引发一个 SystemExit异常，若没有捕获这个异常，Python解释器会直接退出；捕获这个异常可以做一些额外的清理工作。0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获
#一般来说os._exit() 用于在线程中退出；sys.exit() 用于在主线程中退出。
#os.path.getsize()获取文件大小
print os.path.getsize(r'D:\files\bbbb.txt') #713，以byte为单位

#二、文件操作方法大全
#os.mknod(filename[, mode=0600[, device=0]])
#直接打开一个文件，如果文件不存在，则创建一个
os.chdir(r"D:\files") #前往某一目录，然后在这一目录创建文件等操作
#文件打开与关闭
fp = open('test.txt','a+b') #open和file。他们的用法完全一样,默认是r只读
#with open('log','r') as f 当with代码块执行完毕时，内部会自动关闭并释放文件资源。
'''
w：以写方式打开，
a：以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+：以读写模式打开
w+：以读写模式打开 (参见 w )
a+：以读写模式打开 (参见 a )
rb：以二进制读模式打开
wb：以二进制写模式打开 (参见 w )
ab：以二进制追加模式打开 (参见 a )
rb+：以二进制读写模式打开 (参见 r+ )
wb+：以二进制读写模式打开 (参见 w+ )
ab+：以二进制读写模式打开 (参见 a+ )
'''
#2、文件读入
#print fp.read(10)#用来直接读取字节到字符串中，可以指定读取数目，默认是文件将被读取直至末尾
#print fp.readline() #读取打开文件的一行，包括行结束符，也可选size参数，默认为-1，代表直至读到行结束符
print fp.readlines() #把文件名的每一行作为一个list里的成员，返回列表['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10']
#3、文件输出
#fp.write('11') #write(str)参数是字符串，并不会在str后加上一个换行符
#writelines(seq)writelines参数是序列，比如列表把seq的内容全部写到文件中，这个函数也只是忠实地写入，不会在每行后面加上任何东西。
#fp.writelines(['12','13','14'])
#fp.flush()#把缓存区的内容写入到硬盘
print fp.fileno()#返回一个长整型的"文件标签" #结果：3
print fp.isatty() #文件是否是一个终端设备文件（unix系统中的）结果：false
#4、文件移动
print fp.tell() ##返回文件操作标记的当前位置，以文件的开头为原点,结果：182
fp.seek(0) #将文件打操作标记移到offset的位置;0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算;如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
print fp.next() #无需将文件读取,返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.truncate()#把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置
#fp.readinto(buffer ,nbytes)读取 n 字节数据至一个 buffer 对象
#5、文件迭代
for eachline in fp:
    print eachline
fp.close()#关闭文件，使用完文件后，一定要记得关闭文件

#三、目录操作方法
os.chdir(r"D:\files") 
#1、创建目录
#os.makedirs()创建多级目录,创建两个文件目录,创建的全是目录
#os.makedirs(r'D:\files\b\b1')
#os.mkdir()创建单个目录
#os.mkdir(r'D:\files\c')
#2、复制文件
shutil.copyfile("bbbb.txt","aaaa.txt")        #oldfile和newfile都只能是文件
#shutil.copy(r'D:\files\b',r'D:\files\c')            #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
#3.复制文件夹：
#shutil.copytree("olddir","newdir")        #olddir和newdir都只能是目录，且newdir必须不存在
#4、重命名文件（目录）os.rename(old,new)
#os.rename(r"D:\files\aaaa.txt",r"D:\files\bbbb.txt")
#5、移动文件目录shutil.move("oldpos","newpos")   
#shutil.move("D:\files","D:\files\b")
#6.删除文件
#os.remove()函数用来删除一个文件:先获取当前目录os.getcwd() ，再进行删除os.remove()
#os.remove('aaaaa.txt')
#7、删除目录
#os.rmdir(r"D:\files\c")只能删除空目录  
#os.removedirs()删除多个目录,先获取当前目录，再进行删除os.removedirs()
#os.removedirs(r"D:\files\aaaa")
#8、转换目录
os.chdir(r"D:\files") 