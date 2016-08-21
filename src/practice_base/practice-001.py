#!/user/bin/env python
#encoding:utf-8

'''
python核心编程第二章练习
'''
#print 1+2*4
#print 3//2


#2.6、判断输入的数字
a = input('请输入你的数字？')
#print type('%s ' %a)
#print type(int('%s' %a))

if int('%s'%a) < 0:
    print '负数'
elif int('%s'%a) > 0:
    print '正数'
else:
    print '零'


#2.5打印0-10
a = 0
while a <= 10:
    print a
    a += 1

a = 0
while True:
    print a
    a += 1
    if a<=10:
        continue
    else:
        break

for i in range(11):
    print i 

#2.7、逐行显示字符串
str = 'abcdefg' #0-6
i = 0
while i < len(str):
    print str[i]
    i +=1

for i in str:
    print i

#2.8、求字典里各个数字的总和
l = ['1.1','2.1','3.1','4.1','5.1']
s = float('0')
for i in range(len(l)): 
    s += float(l[i]) 
print s

#求输入元素的合
subtot=0
for i in range(5):
    subtot += int (raw_input('enter a number:'))
    print subtot
    
#2.9、求字典数字的平均值
print s/(float(len(l)))

def average(seq,total=0.0):
    for item in range(len(seq)):
        total += float(seq[item])
    return  total/(float(len(seq)))

a = average(l)
print a


      
#2.10用户输入1-100的数字，输入满足条件后成功 并退出，不满足则一直输入
while True:
    a = input('猜猜我心中的整数?')
    guest = 88
    if a == guest:
        print '恭喜你，猜中了'
        break
    elif  1 <= a < guest:
        print '猜小了,请继续'
        continue
    elif  guest< a <=100 :
        print '猜大了，请继续'
        continue
    elif a < 1 or a >100:
        print '请输入1-100之内的整数'
        continue
  
#2.11、选择菜单程序，执行对应程序
#求字典数字的和
def sum(seq,total=0.0):
    for item in range(len(seq)):
        total += float(seq[item])
    return  total

#求字典数字的平均值
def average(seq,total=0.0):
    for item in range(len(seq)):
        total += float(seq[item])
    return  total/(float(len(seq)))


l = ['1.1','2.1','3.1','4.1','5.1']

while True:
    print'''
    1、取5个数的和
    2、取5个数的平均值
    3、退出
    '''
    choice = input('请选择你要执行的功能编号')
    if choice == 1:
        print sum(l)
        break
    elif choice == 2:
        print average(l)
        break
    elif choice == 3:
        print '已退出'
        break
    else:
        print '请输入正确的数字'
        continue

 #2.12,2.13、dir内建函数,使用dir()函数可以查看对像内所有属于及方法，在python中任何东西都是对象
print dir() #['__builtins__', '__doc__', '__file__', '__name__', '__package__']
print dir #<built-in function dir>
print type(dir)#<type 'builtin_function_or_method'>
print dir.__doc__  #dir([object]) -> list of strings
print dir(str)
print dir(int)
print dir(list)
print dir([])
x = ['x','y']
print dir(x)
import sys
print dir(sys)
print type(dir)
print cmp('%d'%a,'%d'%b)
print a,b


#2.15、元素排序
#列表实现
a  = input('请输入数值a')
b  = input('请输入数值b')
c  = input('请输入数值c')

d = [int('%d'%a),int('%d'%b),int('%d'%c)]
d.sort()
d.reverse()
print d


#2.15、元素排序
#常规实现
a  = input('请输入数值a')
b  = input('请输入数值b')
c  = input('请输入数值c')
a = int('%d'%a)
b = int('%d'%b)
c = int('%d'%c)
mi = min(a,b,c)
ma = max(a,b,c)

if mi == a:
    if ma == b:
        print a,c,b
    else:
        print a,b,c
elif mi == b:
    if ma == a:
        print b,c,a
    else:
        print b,a,c
elif mi == c:
    if ma == b:
        print c,a,b
    else:
        print c,b,a

#设计程序,输入3个数据,分别代表 操作码（ASMD分别代表加减乘除）和2个操作数,输出操作数按操作代码计算后的结果.
def operate(ASMD, num1, num2):
    if ASMD == 'A' or 'a':
        return num1 + num2
    elif ASMD == 'S' or 's':
        return num1 - num2
    elif ASMD == 'M' or 'm':
        return num1 * num2
    elif ASMD == 'D' or 'd':
        return float(num1)/num2



