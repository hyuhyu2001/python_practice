#!/user/bin/env python
#encoding:utf-8


'''
python核心编程第六章练习
'''
'''
#6–1.字符串.string 模块中是否有一种字符串方法或者函数可以帮我鉴定一下一个字符串，是否是另一个大字符串的一部分?
a = 'dafreesadadfrfefreeg'
b = 'free'
print a.find(b) 
print a.rfind(b)
print a.index(b)
print a.rindex(b)
print a.count(b)

#6-2.字符串标识符.修改例 6-1 的 idcheck.py 脚本,使之可以检测长度为一的标识符,并且
#可以识别 Python 关键字,对后一个要求,你可以使用 keyword 模块(特别是 keyword.kwlist)来帮你

import string
import keyword
print  dir(keyword)

alphas = string.letters + '_'
nums = alphas+string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
inp = raw_input('Identifier to test? ')

if len(inp) > 0:
    if inp[0] not in alphas:
        print 'invalid: first symbol must be alphabetic'
    else:
        if len(inp)>1:
            for otherChar in inp[1:]:
                if otherChar not in nums:
                    print 'invalid: remaining symbols must be alphanumeric'
                    break
            else:
                if inp not in keyword.kwlist:
                    print 'ok'
                else:
                    print 'Error: keyword name'
else:
    print "okay as an identifier"

 
#6–3.排序(a) 输入一串数字,从大到小排列之.(b) 跟 a 一样,不过要用字典序从大到小排列之.
def compare():
    num_list= []
    num = ''
    while num != '!':
        num = raw_input('请输入一些数字，以！结束')
        if num != '!':
            num_list.append(float(num))
            continue
        else:
            break
    num_list.sort(reverse=True)
    return num_list
print compare()
#字典序就是按照字典的排列方式，比如21就大于111，因为2大于1，方式就是把输入的数字改为字符串即可

#6–4、列表求平均值
def grade():
    grade_list = []
    grade = ''
    while grade != '!':
        grade = raw_input('请输入一些数字，以！结束')
        if grade != '!':
            grade_list.append(float(grade))
            continue
        else:
            break
    total = 0
    for item in range(len(grade_list)):
        total += float(grade_list[item])
    return  total/(float(len(grade_list)))
print grade()


#6–5. 字符串 
#a 更新你在练习 2-7 里面的方案,使之可以每次向前向后都显示一个字符串的一个字符. 
str = 'abcdefg' #0-6
a = raw_input('请输入要查询的字符')
print str.find(str1)
print str.rfind(str1)

for a in str:
    print a
for a in str[::-1]:
    print a

#b、通过扫描来判断两个字符串是否匹配(不能使用比较操作符或者 cmp()内建函数)。附加题: 在你的方案里加入大小写区分. 
str1 = raw_input('请输入要查询的字符')
str2 = raw_input('请输入要查询的字符')

if len(str1) != len(str2):
    print '不匹配'
else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print '不匹配2'
            break
    else:
        print '匹配'


#(c)判断一个字符串是否重现(后面输入的跟前面的一致).附加题:在处理除了严格的回文之外,加入对 例如控制符号和空格的支持。 
#print str1.count(str2)  >1则表示str2在str1中出现多次
i = 0
stlist = []
while True:
    print stlist
    str1 = raw_input('请输入字符').strip()
    for i in range(len(stlist)):
        if str(str1) == stlist[i]:
            print '已出现'   
            break
    else:
        astlist.append(str1)    
        continue   #continue之后便不走后面的代码了


#(d)接受一个字符,在其后面加一个反向的拷贝,构成一个回文字符串.
#回文字符串，就是一个字符串，从左到右读和从右到左读是完全一样的，比如"aba"
str1 = raw_input('请输入字符')
str1 += str1[::-1]
print str1

#6-6、字符串, 创建一个string.strip()的替代函数: 接受一个字符串,去掉它前面和后面的空格(如果使用string.*strip()函数那本练习就没有意义了)
def strip_replace(str):
    c = len(str)-1
    for i in range(c):
        if str[i] == ' ':
            continue
        else:
            str = str[i:]
            str = str[::-1]
            for m in range(len(str)-1):
                if str[m] == ' ':
                    continue
                else:
                    str = str[m:]
                    str = str[::-1]
                    break
            break
    return str
def strip_replace2(str):
    c = 0
    d = len(str)-1
    while str[c] == ' ':
        c = c+1
    while str[d] == ' ':
        d = d -1
    str = str[c:d+1]  
    return str
print strip_replace2('   dsadsadad dadd     ')

#6.7、调试, 看一下在例6.5 中给出的代码(buggy.py)(a) 研究这段代码, 并描述这段代码想做什么,在所有的(#)处都要填写你的注释.
#(b)这个程序有一个很大的问题, 比如输入6,12,20,30 等它会死掉,实际上它不能处理任何的偶数,找出原因.
#(c) 修正(b)中提出的问题.

num_str = raw_input('Enter a number: ') #得到一个用户输入
num_num = int(num_str) #将用户输入的数字字符转化成int类型
fac_list = range(1, num_num + 1) #创建一个1~用户输入数字的列表
print "Before:",fac_list
 
i = 0  # 定义一个整型变量并赋值为0
deleted = []

while i < len(fac_list): # while循环判断条件
    if num_num % fac_list[i] == 0:      # 用户输入数字对里表中index 为i的数字求余.
        deleted.append(fac_list[i]) #修改此处. 
    i = i + 1 #变量自增
    for ch in deleted:
        fac_list.remove(ch)
    print "After:", fac_list


#6-8、列表.给出一个整数值,返回代表该值的英文,比如输入 89 返回"eight-nine"。
#附加题:能够返回符合英文语法规则的形式,比如输入“89”返回“eighty-nine”。本练习中的值限定在家 0到 1,000.
def translateNumberToEnglish(number):
    number_dict = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
        10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
        20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
        100:'hundred',1000:'thousand'}
    #可以声明多个字典，将10位数、百分数的分别声明
    number = int(number.lstrip('0 '))
    if number <= 20 :
        return number_dict.get(number)
    elif 20<number<100 and len(str(number)) == 2:
        if str(number)[1] == '0':
            return number_dict.get(int(str(number)[0]+'0'))
        else:
            return number_dict.get(int(str(number)[0]+'0'))+' '+number_dict.get(int(str(number)[1]))
    elif 100 <= number < 1000 and len(str(number)) == 3:
        if str(number)[2] == '0' and str(number)[1] == '0':
            return number_dict.get(int(str(number)[0]))+' '+number_dict.get(100)
        elif str(number)[2] == '0' and str(number)[1] != '0':
            return number_dict.get(int(str(number)[0]))+' '+number_dict.get(100)+' and '+number_dict.get(int(str(number)[1]+'0'))
        elif str(number)[2] != '0' and str(number)[1] == '0':
            return number_dict.get(int(str(number)[0]))+' '+number_dict.get(100)+' and '+number_dict.get(int(str(number)[2]))
        elif str(number)[2] != '0' and str(number)[1] != '0':
            return number_dict.get(int(str(number)[0]))+' '+number_dict.get(100)+' and '+number_dict.get(int(str(number)[1]+'0'))+' '+number_dict.get(int(str(number)[2]))
    elif number == 1000 and len(str(number)) == 4:
        return 'one'+' '+number_dict.get(number)
    else :
        return '请输入0-1000的整数'

try: 
    number = raw_input('please enter your number')
except Exception,e:
    print '编码错误：',e
    number = input('please enter your number')
        
print translateNumberToEnglish(number)


#6–9.转换.为练习 5-13 写一个姊妹函数, 接受分钟数, 返回小时数和分钟数. 总时间不变,并且要求小时数尽可能大.
def minute(tim):
    tim = divmod(int(tim), 60)
    a = str(tim[0])
    b = str(tim[1])
    return a+':'+b

print minute( '1043') 


#6–10.字符串, 写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转.比如,输入"Mr.Ed", 应该返回"mR.eD"作为输出.
#print 'Mr.Ed'.swapcase() #直接通过函数转换
def swap():
    str_1 = raw_input('Enter your string:')
    str_list = list(str_1)
    result_list = []
    for i in str_list:
        if i.isupper():
            result_list.append(i.lower())
        elif i.islower():
            result_list.append(i.upper())
        else:
            result_list.append(i)
    
    return ''.join(result_list)
    
print swap()


#6-11. 转换.(a) 创建一个从整形到IP地址的转换程序, 如下格式: WWW.XXX.YYY.ZZZ(b) 更新你的程序, 使之可以逆转换.
def NumberToIp():
    a = raw_input('Enter your number(必须12位):')
    a_list = []
    if len(a) == 12:
        for i in range(0,11,3): #xranger有起始和结束，3为步长，
            b = a[i:i+3]
            a_list.append(b)
    else:
        return '请输入12位整型数字'
    return '.'.join(a_list)

def IpToNumber():
    a = raw_input('Enter your IP:')
    a_list = a.split('.')
    return ''.join(a_list) 
'''

#6-12. 字符串.
#(a)创建一个名为findchr()的函数,函数声明如下.def findchr(string,char)
    #findchr()要在字符串string中查找字符char,找到就返回该值的索引,否则返回-1.不能用string.*find()或者string.*index函数和方法
#(b) 创建另一个叫rfindchr()的函数,查找字符char最后一次出现的位置.它跟findchr()工作类似,不过它是从字符串的最后开始向前查找的.
#(c) 创建第三个函数,名字叫subchr(),声明如下.def subchr(string,origchar,newchar)
    #subchr()跟findchr()类似,不同的是如果找到匹配的字符就用新的字符替换原先的字符.返回修改后的字符
    
def findchr(string,char):
    for i in range(len(char)):
        if char[0] not in string:
            return -1 
            break
        else: 
            if len(char) ==1:
                return '匹配1'
            elif 1 < len(char) <= len(string):
                if char[0:i] in string:
                    continue
                else:
                    return -1
            elif len(char)>len(string):
                return -1
    return '匹配2'

#print findchr('dadadaddstring','string')



