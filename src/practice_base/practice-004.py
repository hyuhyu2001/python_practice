#!/user/bin/env python
#encoding:utf-8

'''
python核心编程第五章练习

最好不要在函数中使用print语句输出信息，而是通过return语句返回必要的值，这样调用函数的代码可以自己处理代码，实用性更强

5-1 整形 讲讲Python 普通整型和长整型的区别
在Python中，标准整形的取值和你的计算机处理器位数有关，如果你的计算机是32位，那么范围就是[-2**32，(2**31-1)*2+1].后面之所以不写成2**32-1是因为2**32已经超出了范围。在系统中已经转为L型了。
长整形能表达的数值仅仅与你的机器支持的(虚拟)内存有关。整形通过在后面加L(或者小写)转为长整形
'''

#5-2 计算两个数的乘积
def  mul(a,b):
    return a*b

print mul(2.23123, 3.54546)


#5-3 算出评分乘积
def grade(score):
    if 90<=score<=100:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70<=score<80:
        return 'C'
    elif 60<=score<70:
        return 'D'
    elif score<60:
        return 'E'

print grade(100)

#5-4 取余，判断给定年份是否是闰年;divmod(x,y)这个函数也可以获得商和余数，比如divmod(5,2)，返回的值为(2,1)，其中2为商，1为余数
def div(year):
    if (divmod(year,4)[1] == 0 and divmod(year,100)[1] != 0) or divmod(year,400)[1] == 0:
        return '闰年'
    else:
        return '不是闰年'
 
print div(1900)


#5-5 取余：取一个小于一美元的硬币，计算可以换算最少多少枚硬币，必须是最少，硬币有1美分、4美分、10美分、25美分4种
def div2(money):
    yingbi = [25,10,5,1]
    i = 0
    jieguo = []
    while True:
        a = divmod(money, yingbi[i])
        b =  '%s枚%d美分' %(a[0],yingbi[i])
        jieguo.append(b)
        if a[1] == 0:
            break
        else:
            money -= a[0]*yingbi[i]
            i +=1
            continue
    return ','.join(jieguo)  # 第一种实现方式，用join转换为字符串
    #for key in jieguo:#第二种实现方式，打印列表的每一项
       # print  key
print div2(99)

#打印字符串时，使用print str.encode('utf8');
#打印中文列表时，使用循环 for key in list：print key
#打印中文字典时，可以使用循环，也可以使用json：import json ; print json.dumps(dict, encoding='UTF-8', ensure_ascii=False)


#5-6 算术。写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符：
#N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数，运算符可以是+, -, *, /, %, ** 分别表示
#加法，减法， 乘法， 整数除，取余和幂运算。计算这个表达式的结果，然后显示出来
def operation(ope):
    if '+' in ope:
        return  float(ope.split('+')[0]) + float(ope.split('+')[1])
    elif '-' in ope:
        return float(ope.split('-')[0]) - float(ope.split('-')[1])
    elif '/' in ope:
        return float(ope.split('/')[0]) / float(ope.split('/')[1])
    elif '%' in ope:
        return float(ope.split('%')[0]) % float(ope.split('%')[1])
    elif '*' in ope:
        if ope.count('*') == 1:
            return float(ope.split('*')[0]) * float(ope.split('*')[1])
        if ope.count('*') == 2:
            return float(ope.split('**')[0]) ** float(ope.split('**')[1])
    else :
        return '请输入正确的符号'

print operation('4**2')

#5-8 几何。计算面积area和体积volume（1）正方形和立方体（2）圆和球
def geometry(shape,length): 
    if shape == 'square' :#正方形
        return length*2
    elif shape == 'cube' :#立方体
        return length*3
    elif shape == 'circle' :#圆
        return 3.14*length*length 
    elif shape == 'ball' :#球
        return 4*3.14*length*length*length/3
print geometry('square', 3)

#math模块实现了许多对浮点数的数学运算函数. 这些函数一般是对平台 C 库中同名函数的简单封装, 所以一般情况下, 不同平台下计算的结果可能稍微地有所不同, 有时候甚至有很大出入
import math
def sqcube():
    s = float(raw_input('enter length of one side: '))
    print 'the area is:', s ** 2., '(units squared)'
    print 'the volume is:', s ** 3., '(cubic units)'
def cirsph():
    r = float(raw_input('enter length of radius: '))
    print 'the area is:', math.pi * (r ** 2.),'(units squared)'
    print 'the volume is:', (4. / 3.) * math.pi * (r **3.), '(cubic units)'
sqcube()
cirsph()  


#5-9 数值格式的问题
print 17+32 #49
print 017+32 #47  #Python中0开头的数字表示八进制数。八进制数017表示15，而八进制数032表示26，所以得到如题所示答案
print 017+032 #41
print 561 + 781 #561加上781才是1342，而56l加上78l是134L

#5-10 转换。写一对函数来进行华氏度到摄氏度的转换。转换公式为C = (F - 32) * (5 / 9)应该在这个练习中使用真正的除法，否者你会得到不正确的结果。
def Centigrade(F):  #摄氏度,将华氏度Fahrenheit转换为摄氏度   
        return (F-32)*(5.0/9.0)
        
print Centigrade(400)

#5-11、取余。
#（a）使用循环和算术运算，求出0~20之间的所有偶数。
#（b）同上，不过这次输出所有的奇数。
#（c）综合（a）和（b），请问辨别奇数和偶数的最简单的办法是什么？
#（d）使用（c）的成果，写一个函数，检测一个整型能否被另一个整型整除。
#现要求用户输入两个数，然后你的函数判断两者是否有整除关系，根据判断结果分别返回True和False。
def Even_Odd(): #even偶数；odd奇数
    even = []
    odd = []
    for num in range(0,21):
        if divmod(num, 2)[1] == 0:
            even.append(num)
        else:
            odd.append(num)
    print '偶数为：%s' %even
    print '奇数为：%s' %odd

Even_Odd()


#5-12：系统限制。写一段脚本确认一下你的Python 所能处理的整数，长整数，浮点数和复数的范围
import sys
print sys.maxint
print (sys.long_info)
print (sys.float_info)
print (sys.long_info)

#5-13：转换。写一个函数把小时和分钟所表示的时间转换成为只用分钟表示的时间
def minute(tim):
    tim = tim.split(':')
    a = tim[0]
    b = tim[1]
    return int(a)*60+int(b) 

print minute('17:23')


#5-14：银行利息。写一个函数，以定期存款利率为参数， 假定该账户每日计算复利，请计算并返回年回报率。
#复利： 最终金额=本金＊(1+第1期报酬率)＊(1+第2期报酬率)＊(1+第3期报酬率)＊ ….. ＊(1+第N期报酬率)
#年回报率 = (1+第1期报酬率)＊(1+第2期报酬率)＊(1+第3期报酬率)＊ ….. ＊(1+第N期报酬率)
def interest(capital,rate):
    for i in range(365):
        capital *= (1+float(rate))
    return capital
print interest(10000.0, 0.0035)

#5-15：最大公约数和最小公倍数。请计算两个整型的最大公约数和最小公倍数。
#本题答案采用的是更相减损术，又称“等值算法”求两个数的最大公约数，而两个数的最小公倍数是他们的乘积除以最大公约数。
#最小公倍数（Least Common Multiple，缩写LCM）
#最大公约数（Greatest Common Divisor，缩写GCD；或Highest Common Factor，简写为HCF）

def GCD(a,b):
    i = 0
    if (a%2 == 0) and (b%2 == 0):
        c = a/2
        d = b/2
        i +=1
    else:
        c = a
        d = b
    while c != d:
        if c>d:
            c = c - d
        elif c<d:
            d = d - c
        else:
            return c *(2**i) 
    return c *(2**i) 
def LCM(a,b):
    return a*b/GCD(a,b)

print GCD(4044, 9088)
print LCM(4044, 9088)

#5-16 家庭财务。给定一个初始金额和月开销数， 使用循环，确定剩下的金额和当月的支出数， 包括最后的支出数。
#Payment() 函数会用到初始金额和月额度， 输出结果应该类似下面的格式（例子中的数字仅用于演示）：
def payment(x,y):
    i = 0
    while x >= y:
        print '%d $ %.2f $%f'%(i,y,x-y) 
        i += 1
        x = x - y
    print   '%d $ %.2f $%f'%(i,x,0.00) 
          
    
balance = input('月初的金额数为：')   
payment1 = input('此笔的消费金额为：')
payment(balance, payment1)


#5-17 随机数。熟读随机数模块然后解下面的题：生成一个有 N 个元素的由随机数 n 组成的列表， 
#其中 N 和 n 的取值范围分别为： (1 <N <= 100), (0 <= n <= 231 -1)。
#然后再随机从这个列表中取 N (1 <= N <= 100)个随机数出来， 对它们排序，然后显示这个子集
from random import randint,sample

N = randint(2,100)
l = []
for i in range(N):
    n = randint(-1,230)
    l.append(n)
    l.sort()
#random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
#randlist = random.sample(xrange(0, 2**31 - 1), N)
print l
l2 = sample(l,randint(1,100))
print l2

