#!/user/bin/env python
#encoding:utf-8

'''
字符串对象是不可改变的，也就是说在python创建一个字符串后，你不能把这个字符中的某一部分改变。
任何上面的函数改变了字符串后，都会返回一个新的字符串，原字串并没有变。
其实这也是有变通的办法的，可以用S=list(S)这个函数把S变为由单个字符为成员的list，
这样的话就可以使用S[3]='a'的方式改变值，然后再使用S=" ".join(S)还原成字符串
'''
#多重赋值
x = y =z=1
#多元赋值
x,y,z = 1,2,'string' #建议加上圆括号增加易读 (x,y,z = 1,2,'string') 

#字符串常量
#单引号和双引号是一样的
print 'spa''m' #单引号
print "spa'm" #双引号
print 'k"s',"k's" #不使用转译字符就可以实现在一个字符串中包含其余种类的引号
print "you"'can'"do it" #可以在任意表达式中合并相邻的字符串常量，尽管也可以用+操作符实现
print '''....spam....'''"""....spam...."""#三引号

#字符串的转译
print "s\tp\na\om"#转译字符 \t横向制表符 \n换行
#加入r可以不转译 ；打印原始字符串（Raw string）
print r's\tp\na\om' 

#加u代表unicode字符串；内建的str()函数和chr（）函数不能处理Unicode，它们只能处理常规ASCII编码的字符串
#如果一个Unicode字符串作为参数传给了str()函数，它会首先被转换成ASCII码字符串然后交给str（）函数。
print u'eggs\u0020spam' 


#长字符串，需要跨多行时，用三个引号代替普通引号
print '''
this is
a long
string
'''

#每一行的末尾增加 \,代表一个字符串被拆分成两行;;这种用法同样支持语句、字符串、表达式
print \
'hello\
world'
print 1+2\
+4+5

'''
标准类型操作符
>,<,>=,<=,==,!=,<>对象值得比较
注：做比较时字符串是按ASCII值的大小来比较的
is 对象身份比较
and,or,not 布尔类型 
'''

#一、标准内建函数
#1.1/type函数：判断类型<type 'str'>
print type('Jim') 
#1.2/cmp函数，制定字符串长度比较,两个值相等，返回0
print cmp('12345'[0:3],'123bc'[0:3]) 
#1.3/str函数,转换成字符串；repr(obj) 或反引号运算符(``) 可以方便的以字符串的方式获取对象的内容、类型、数值属性等信息。
#str()函数得到的字符串可读性好， 而repr()函数得到的字符串通常可以用来重新获得该对象, 通常情况下 obj == eval(repr(obj)) 这个等式是成立的
print type(str(1))
print int('42')
print str(42)
print repr(42),'42'
#1.4/判断对象的类型
print isinstance('jim', str)  #True
#字符串转换工具

#二、序列操作
#2.1、字符串连接方法
print 'Jim' + 'Green' #（1）用 “+” 来连接两个字符串，结果：'JimGreen'
print 'Jim', 'Green'  #（2）两个字符串用“逗号”隔开，那么这两个字符串将被连接，但是，字符串之间会多出一个空格 结果：Jim Green
print  'Jim' 'Green' #（3）只要把两个字符串放在一起，中间有空白或者没有空白：两个字符串自动连接为一个字符串 结果：JimGreen
#（4）格式化字符串：通过%实现，在%的左侧放置一个字符串，右侧放置希望格式化的值，可以是一个值、多个值、元组或者字典
#如果需要转换的元组作为表达式的一部分存在，那么必须把他用圆括号括起来，以免出错
print "hello,%s,%s enough"%('world','not')   #字符串是 %s;整数 %d;浮点数%f
#（5）join函数 是非常重要的字符串方法，是split的逆方法，用来在队列中添加元素。这个函数接受一个列表或者元组，然后用字符串依次连接列表中每一个元素
#join()方法也可以与内置的reversed()函数一起使用，以实现对字符串的反转。但是，通过步距也可以更精确地获取同样的结果，比如：s[::-1]
seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq) #在列表中增加连接符，第一个队列join，第二个队列join，依次进行 ；结果：1+2+3+4+5
print sep.join(reversed(seq)) #结果：5+4+3+2+1
dirs = '','usr','bin','env'
print '/'.join(dirs)  #  结果：/usr/bin/env
print 'C:'+'\\'.join(dirs) #结果C:\usr\bin\env
#（6）字符串乘法
print 'abc'*3  #结果：abcabcabc


#使用str.format()方法进行字符串格式化
print "{who} turned {age} this year".format(who="she", age=88)  #每个花括号有字段名标识 结果：she turned 88 this year
print "The {who} was {0} last week".format(12, who="boy") #名为0的字段被第一个参数所代替，名为1的字段则被第二个参数所代替 结果：The boy was 12 last week
stock = ["paper", "envelopes", "notepads", "pens"] 
print "we have {0[1]} and {0[2]} in stock".format(stock)  #字段名可以引用集合数据类型,字典中存储的key-value项，也可以用于str.format()方法。

#2.2、索引和切片
#python字符串中的字符通过索引来提取的，获得一个特定的字符串；python偏移量从0开始，并比字符串的长度小1，负偏移代表从结尾处反向计数
s = 'spam'

print s[0],s[-2] #获取第一个元素，获取倒数第二个元素s a
print s[1:3] #加:时包含下边界，不包含上边界；打印1和2位置的元素pa
print s[1:] #打印偏移为1到末尾的元素 pam
print s[:3] #打印首位到2的元素，不包含3spa
print s[:-1] #打印首位到末尾的元素，不包含末尾spa
print s[:] #打印首位到末尾的元素，包含末尾spam

#扩展分片，第三个限制值：增加第三个索引，用作步进X[I:J:K]表示：索引X对象中的元素，从偏移为I直到偏移为J-1，每隔K元素索引一次
d = 'abcdefghijklmnop'
print d[1:10:2] #从1开始，每隔2元素取一次，分别取1 3 5 7 9 结果：bdfhj
print d[::2] #从0开始到末尾，分别取0 2 4 6... 结果acegikmo
print d[::-1] #负数代表从末尾开始取，步长=1，结果为ponmlkjihgfedcba
print d[::-2] #步长=2，结果为pnljhfdb
print '12345'+'abcdef'[0:3] #给后面字符串分片，然后相加；结果12345abc

#2.3、成员操作符 in ，not in
#2.4、删除清空字符串 del aString aString=''

#三、序列函数

#3.1、len方法：返回字符串的长度
sStr1 = '12345678'
sStr2 = '456'
print len(sStr1 + sStr2) #返回长度11
print len(sStr1 and sStr2) #返回长度3
#3.2、enumerate(iter)：接受一个可迭代对象作为参数,用于遍历序列中的元素以及他们的下标
enmu = 'fo'
for i, t in enumerate(enmu):
    print i,t  #返回 0 f ；1 o
#3.3、max(),min()：返回最大或者最小的字符(按照ASCII 码值排列)
print max('lmn') #返回最大n
print min('xyz') #返回最小x
#3.4、zip() 接受序列作为参数，这些元素的第一个元素组成一个元组，第二个组成一个元组
z = 'foa'
print zip(z) #[('f',), ('o',), ('a',)]
print zip(z,enmu)  #[('f', 'f'), ('o', 'o')]
#3.5、reversed();接受一个序列作为参数,返回一个以逆序访问的迭代器
print sep.join(reversed(seq)) #结果：5+4+3+2+1
#3.6、sort(),sorted()：对元素进行排序；sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表
print sorted([5, 2, 3, 1, 4]) #结果[1, 2, 3, 4, 5]
L = [('b',2),('a',1),('c',3),('d',4)]
print sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))#cmp：用于比较的函数，比较什么由key决定,有默认值，迭代集合中的一项;结果[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))#key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项;[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print sorted([5, 2, 3, 1, 4], reverse=True) #reverse：排序规则. reverse = True 或者 reverse = False，有默认值 结果[5, 4, 3, 2, 1]
#3.7、sum处理的对象为数字，不能用在字符串

#四、只适用于字符串类型的函数
#4.1、raw_input()函数：raw_input()函数使用给定字符串提示用户输入并将这个输入返回
#raw_input()读取标准输入，输入默认按字符串形式；input()是按UI输入的确定，比如输入数字按数字判断，输入字符按字符判断
#4.2、str()  unicode()
#4.3、chr(), unichr(), ord()
#对于单个字符串（只能以长度为1的字符串作为参数），执行与ASCII码的转换
print ord('s') 
print chr(115)

#五、字符串对象的方法
#5.1删减 strip()   lstrip() rstrip() 
#strip方法：只会去除两侧的字符
#返回去除两侧（不包含内部）空格的字符串
print '   my name is king      '.strip()  #去除首尾的空格，结果：my name is king
#也可指定需要去除的字符，将它们列为参数即可
print '*** SPAM * for * everyone!!! ***'.strip(' *!') #同时去除首尾包含*和！的字符 结果：SPAM * for * everyone
print '*** SPAM * for * everyone!!! ***'.lstrip(' *!') #去除左侧包含的字符 结果：SPAM * for * everyone!!! ***
print '*** SPAM * for * everyone!!! ***'.rstrip(' *!') #去除右侧包含的字符 结果：*** SPAM * for * everyone
print '    ***SPAM * for * everyone!!! ***'.expandtabs(8)#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8

#5.2、切割split() splitlines() 
#split方法：他是join的逆方法，用来将字符串分割成序列，分割成列表
print '1+2+3+4+5'.split('+')  #把字符串按+分割，生成列表；结果：['1', '2', '3', '4', '5']
print 'C:\usr\bin\env'.split('\\') #必须用转移符\\ 结果：['C:', 'usr\x08in', 'env']
print 'Using the default'.split() #如果不提供任何分隔符，程序会把所有的空格作为分隔符；结果：['Using', 'the', 'default']
print '1+2+3+4+5'.split('+',3)  #3表示分割的次数：结果：['1', '2', '3', '4+5']
#splitlines() 按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.结果 ['1+2+3\n', '+4+5']
print '''1+2+3
+4+5'''. splitlines(1) 

#5.3、变形
#lower函数：转换为小写
print 'HDWUD HDJHS LKJDS'.lower()  #结果：hdwud hdjhs lkjds
#upper函数：转换为大写
print 'isAND'.upper() #结果：ISAND
#swapcase：大小写互换
print 'isAND'.swapcase()#结果ISand
#capitalize：首字母大写
print 'isAND'.capitalize() #结果Isand
#title：首字母大写，每个单词第一个大写,其他小写，title() 函数并不去除字符串两端的空白符也不会把连续的空白符替换为一个空格
#建议使用string 模块中的capwords(s)函数，它能够去除两端的空白符，再将连续的空白符用一个空格代替
print ' hello world!'.title() #结果： Hello World!

#5.4、连接
#join() 函数的高效率（相对于循环相加而言），使它成为最值得关注的字符串方法之一。它的功用是将可迭代的字符串序列连接成一条长字符串
conf = {'host':'127.0.0.1',
 'db':'spam',
 'user':'sa',
 'passwd':'eggs'}
print ';'.join("%s=%s"%(k, v) for k, v in conf.iteritems()) #结果;passwd=eggs;host=127.0.0.1;db=spam;user=sa

#5.5查找
#字符串方法
#find方法 可以在字符串中查找一个子字符串，它返回字符所在位置的最左端的索引位置；如果没有找到则返回-1
print d.find('cdefg')  #返回结果，为c的索引值2
print d.find('cdeefg')   #返回结果-1，因为没有找到
#这个方法可以接受可选的起始点和结束点作为参数
dd ='$$$ Get rich now!!! $$$'
print dd.find('$$$')  #从刚开始查找  结果0
print dd.rfind('$$$')  #反向查找  结果20
print dd.find('$$$',1) #从索引位置=1处开始查找 结果20
print dd.find('$$$',1,16) #从索引1和16的中间找，返回结果-1（没找到）
#index方法,同find，但找不到时会抛异常，而不是报负数
print  dd.index('Get')
print  dd.rindex('Get') #反向查找
#count计算出现的次数
print dd.count('$$$',0,50) #计算'$$$'在字符串中出现的次数 结果2次

#5.6、替换
#replace方法：返回某字符串的所有匹配项均替换后得到字符串
print 'this is a test'.replace('is', str(11)) #replace(old, new) ,old和new必须为字符串,不加参数是所有的替换： th11 11 a test
print 'this is a test'.replace('is', str(11),1) #S.replace(oldstr, newstr, [count]) ；加上count代表替换次数，替换一次 th11 is a test

#translate(table[,deletechars]) #使用上面的函数产后的翻译表，把S进行翻译，并把deletechars中有的字符删掉
#translate() 的参数 table 可以由 string.maketrans(frm, to) 生成
#translate() 对 unicode 对象的支持并不完备，建议不要使用
'''
字符串的mapping，这一功能包含两个函数 
String.maketrans(from, to) 
#返回一个256个字符组成的翻译表，其中from中的字符被一一对应地转换成to，所以from和to必须是等长的。 
S.translate(table[,deletechars]) 
# 使用上面的函数产后的翻译表，把S进行翻译，并把deletechars中有的字符删掉。
需要注意的是，如果S为unicode字符串，那么就不支持 deletechars参数，可以使用把某个字符翻译为None的方式实现相同的功能。
此外还可以使用codecs模块的功能来创建更加功能强大的翻译表。
import string
instr = 'abc'
outstr = '123'
table = string.maketrans(instr,outstr)
print table

instr = 'abcde'
outstr = '12345'
table = string.maketrans(instr,outstr)
astr = 'abcdefg-123' 
bstr = astr.translate(table,'123')
print bstr
'''
#5.7、判定
#字符串的测试、判断函数，这一类函数在string模块中没有，这些函数返回的都是bool值
print 'prefixdsadadsuffix'.startswith('prefix') #判断是否以prefix开头  True
print 'prefixdsadadsuffix'.startswith('prefix',10,11) #找位置10和11处，False  
print 'prefixdsadadsuffix'.endswith('suffix') #判断是否以suffix结尾 ，True
print 'prefixdsadadsuffia123'.isalnum() #是否全是字母和数字，并至少有一个字符  True
print 'prefixdsadadsuffix123'.isalpha() #是否全是字母，并至少有一个字符 False 
print 'prefixdsadadsuffix'.isdigit() #是否全是数字，并至少有一个字符 False
print '  '.isspace() #是否全是空白字符，并至少有一个字符  True
print 'prefixdsadadsuffix123'.islower() #S中的字母是否全是小写  True
print 'prefixdsadadsuffix123'.isupper() #S中的字母是否便是大写 False
print 'prefixdsadadsuffix'.istitle() #S是否是首字母大写的 False

#5.8、填充
#字符串在输出时的对齐
string1 = "Now I am here."
print string1.center( 20) #center(width[, fillchar]), 字符串中间对齐
print string1.ljust( 20 ) #字符串左对齐，不足部分用fillchar填充，默认的为空格
print string1.rjust( 20 ) #字符串右对齐，不足部分用fillchar填充，默认的为空格 
print string1.zfill(20) #把字符串变成width长，并在右对齐，不足部分用0补足
#expandtabs([tabsize])把字符串中的制表符（tab）转换为适当数量的空格
print '    ***SPAM * for * everyone!!! ***'.expandtabs(8)#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8
'''结果如下
   Now I am here.   
Now I am here.      
      Now I am here.
000000Now I am here.
'''
#5.9、编码和解码
#编码和解码的函数
# 其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持。
#errors默认值为"strict"，意思是UnicodeError。可能的值还有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 和所有的通过codecs.register_error注册的值。这一部分内容涉及codecs模块，不是特明白
#字符串在Python内部的表示是unicode编码.
#s='中文' 如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。
#这种情况下，要进行编码转换，都需要先用decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。 

#encode的作用是将unicode编码转换成其他编码的字符串， 
name=u'李雪'
print name.encode('gb2312')  #转换为gb2312  结果：��ѩ
print name.encode('utf-8')  #转换为utf-8 结果：

#decode的作用是将其他编码的字符串转换成unicode编码; 如果一个字符串已经是unicode了，再进行解码则将出错 因此通常要对其编码方式是否为unicode进行判断： 
print isinstance(name, unicode) #用来判断是否为unicode
#print name.decode('unicode')


#python 对反斜杠的处理
def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)

s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print s  #结果：John 'Johny' Doe (a.k.a. "Super Joe")\
print addslashes(s) #结果：John \'Johny\' Doe (a.k.a. \"Super Joe\")\\\

#只显示字母和数字
def OnlyCharNum(s,oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;

print(OnlyCharNum("a000 aa-b"))

'''
#字符串类型转换函数，这几个函数只在string模块中有
string.atoi(s[,base]) 
#base默认为10，如果为0,那么s就可以是012或0x23这种形式的字符串，如果是16那么s就只能是0x23或0X12这种形式的字符串 
string.atol(s[,base]) #转成long 
string.atof(s[,base]) #转成float
'''
