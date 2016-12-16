#!/user/bin/env python
#encoding:utf-8

'''
【一】函数编写
1、def函数中，可以嵌套def
2、global声明了一个模块级的变量并被赋值。
3、函数主题往往包含一个return语句（不是必须的），如果它没有出现，那么函数将会在控制流执行完函数主体时结束，没有返回值的函数自动返回了none对象
return可以在函数主体的任何地方出现，它表示函数调动的结束，并将结果返回至函数调用处
4、编写函数时的参数设置
（1）def func(name1,name2)    函数    常规参数：通过位置或变量名进行匹配
（2）def func(name=value)    函数    默认参数值：如果没有在调用中传递的话，就是用默认值，要放在常规函数的后面
（3）def func(*name)    函数    匹配并收集(在元组中）所有包含位置的参数 通过一个把元组（非关键字参数）作为参数组传递给函数
（4）def func(**name)    函数    匹配并收集（在字典中）所有包含位置的参数。过一个把字典（关键字参数）作为参数组传递给函数

#5、函数的属性：
#（1）函数属性本质上是函数本体作用域里的变量，包括函数内内嵌的函数。
#（2）函数属性是python另外一个使用了句号属性标识并拥有名字空间的领域
'''
def testjin():
    name='jin'

    testjin.__doc__ = 'test'
    testjin.version   ='0.1'

print testjin.__doc__
print testjin.version
print testjin.name  #打印时会报错，因为这个时候函数体还没有创建；先运行函数，再访问里面的变量也不能访问，这点和module、class不一样

'''
【二】作用域（变量作用域）：变量定义以及查找的地方。作用域也称之为命名空间
1、作用域法则：在代码中变量名被赋值的位置决定了这个变量名能被访问到的范围，一个函数所有变量名都与函数的命名空间相关联
（1）def内定义变量名def内使用
（2）def之中的变量名与def之外的变量名不发生冲突，使用别处相同的变量名也没问题
    x=99
    def func():
        x=88
2、函数定义了本地作用域，而模块定义了全局作用域，两作用域关系
（1）内嵌的模块时全局作用域：模块的全局变量就成为了一个模块对象的属性
（2）全局作用域的范围仅限单个文件：不要被全局迷惑，这里的全局是一个文件的顶层的变量名，仅对这个文件内部的代码而言是全局
（3）每次对函数的调用都创建了一个新的本地作用域
（4）赋值的变量名除声明为全局变量，否则均为本地变量
（5）所用的变量名都可以归纳为本地，全局，或者内置。（内置：python预定义的__builtin__模块提供的）
3、变量名解析：LEGB原则
LEGB含义解释：
L-Local(function)；函数内的名字空间
E-Enclosing function locals；外部嵌套函数的名字空间(例如closure)
G-Global(module)；函数定义所在模块（文件）的名字空间
B-Builtin(Python)；Python内置模块的名字空间
LEGB规定了查找一个名称的顺序为：local-->enclosing function locals-->global-->builtin
（1）变量名引用分为三个作用域进行查找：首先查找本地（函数内，如果有），之后全局，最后内置
（2）默认情况下，变量名赋值会创建或改变本地变量
（3）全局声明将赋值变量名映射到模块文件内部的作用域
4、内置作用域：需要导入__builtin__ 
import __builtin__
print dir(__builtin__)  ;['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
5、global
global语句包含关键字global
（1）全局变量是位于模块文件内部顶层的变量名
（2）全局变量如果是在函数内部被赋值的话，并需经过声明,方式 global 变量名
（3）全局变量名在函数的内部不经过声明也可以变引用
def testjin():
    global name
    name='jin'
testjin()  #这里需要注意：函数testjin()要执行后，函数内testjin()中局部变量name才会提升为全局变量，函数外才能访问。但是一般都不用这种临时的方式，全局的就在全局定义，局部的就在局部定义
print name
6、闭包（了解）
如果在一个内部函数内，对在外部作用域（但不在全局作用域）[也就是包含函数的函数作用域]的变量进行引用，那么内部函数就被认为是闭包closure
定义在外部函数内的但由内部函数引用或者使用的变量被称为[自由变量]
将函数1放到一个函数2中，函数2 return 函数1这个对象。函数1会引用函数2作用域中的变量【引用外部但不是全局作用域】
'''

'''
【三】函数调用和传递参数
1、函数调用
func(value1,value2)    调用者    常规参数，通过位置进行匹配
func(name=value)    调用者    关键字参数，通过变量名匹配      默认参数值：如果没有在调用中传递的话，就是用默认值
func(*name)    调用者    可变长度的参数，以name传递所有的对象，并作为独立的基于位置的参数，通过一个把元组（非关键字参数）作为参数组传递给函数
func(**name)    调用者    可变长度的参数，以name成对的传递所有的关键字/值，并作为独立的关键字的参数，过一个把字典（关键字参数）作为参数组传递给函数

2、函数参数说明：
参数传递:传递给函数作为其输入对象的方式
（1）参数的传递是通过自动将对象赋值给本地变量来实现的。
（2）在函数内部的参数名的赋值不会影响调用者。
（3）改变函数的可变对象参数的值也许会对调用者有影响。
换句话说，因为参数是简单的通过赋值进行对象的传递，函数能够改变传入的可变对象，因此其结果会影响调用者。
（4）不可变参数是“通过值”进行传递。
像整数和字符串这样的对象是通过对象引用而不是拷贝进行传递的，但是因为你无论如何都不可能在原处改变不可变对象，
实际的效果就是很像创建了一份拷贝。
可变对象是通过“指针”进行传递的。
（5）默认情况下，参数是通过其位置进行匹配的，从左到右，而且必须精确地传递和函数头部参数名一样多的参数。还能够定义变量名进行匹配，
3、参数设置规则
(1)、位置参数
(2)、默认参数
(3)、关键字参数
可变长度参数
(4)、* 非关键字可变参数（元组）
(5)、** 关键字可变参数（字典）
###############################
【1】位置参数[行参]：从左到右进行匹配
【2】关键字参数：通过参数名进行匹配。【调用时】【调用者】可以定义那个函数接受这个值，通过在调用时使用参数的变量名，使用name=value这种语法。
【3】*默认参数：为没有传入值得参数定义参数值【定义函数时】如果调用时传入的值过于少的话，函数能够为参数定义接受的默认值，在函数定义中使用name=value
【4】*可变参数：收集任意多基于位置或关键字的参数
1)以*开头，收集任意多的额外参数
2)**可变参数：传递任意多的基于位置或关键字的参数。【调用时】

python 中用默认值声明变量的语法是所有的位置参数必须出现在任何一个默认参数之前。【注意】

4、任意参数
【1】非关键字可变长参数（元组）
当函数被调用的时候，所有的形参（必须的和默认的）都将值赋给了在函数声明中相对应的局部变量。剩下的非关键字参数按顺序插入到一个元组中便于访问
'''
def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    print 'formal arg 1:', arg1
    print 'formal arg 2:', arg2
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg
    
tupleVarArgs('abc')  #结果：formal arg 1: abc    formal arg 2: defaultB
tupleVarArgs(23, 4.56)  #结果：formal arg 1: 23  formal arg 2: 4.56
tupleVarArgs('abc', 123, 'xyz', 456.789) #结果： formal arg 1: abc  formal arg 2: 123  another arg: xyz   another arg: 456.789

'''
【2】关键字变量参数（Dictionary）
在我们有不定数目的或者额外集合的关键字的情况中，参数被放入一个字典中，字典中键为参数名，值为相应的参数值。为什么一定要是字典呢?因为为每个参数-参数的名字和参数值-
-都是成对给出---用字典来保存这些参数自然就最适合不过了
'''
def dictVarArgs(arg1, arg2='defaultB', **theRest):
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % (eachXtrArg, str(theRest[eachXtrArg]))

dictVarArgs(1220, 740.0, c='grail')
dictVarArgs(1220, 740.0) 
dictVarArgs(1220) 
dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))
#结果：formal arg1: one
#formal arg2: defaultB
#Xtra arg men: ('freud', 'gaudi')
#Xtra arg e: zoo
#Xtra arg d: 10

'''
【四】函数嵌套
函数嵌套
在函数体内创建另一个函数（对象）是完全合法的。这种函数叫内部/嵌套函数
最明显的创造内部函数的方法是在外部函数的定义体内定义函数（用def 关键字）
'''
def foo(): 
    def bar(): 
        print 'bar() called'
    print 'foo() called' 
    bar()

foo() 
#内部函数一个有趣的方面在于整个函数体都在外部函数的作用域之内，如果没有任何对bar()的外部引用，那么除了函数体内，任何地方都不能对其进行调用。

'''
【五】函数式编程（了解）
掌握lambda、filter()、map()、reduce()即可
1、匿名函数与lambda
python允许用lambda关键字创建匿名函数，匿名是因为不需要用标准的方式来声明（标准方式一般是def声明）
'''
def add(x, y): return x + y 
lambda x, y: x + y

'''
2、内建函数apply()、filter()、map()、reduce()
map/filter/reduce/都是对一个集合进行处理，filter是用于过滤，map用于映射、reduce用于归并
apply(func[, nkw][, kw])【已淘汰】
filter(func, seq) 【部分功能被列表取代】调用一个布尔函数func 来迭代遍历每个seq 中的元素； 返回一个使func 返回值为ture 的元素的序列
map(func, seq1[,seq2...])【部分功能被列表取代】 将函数func用于给定序列（s)的每个元素，并用一个列表来提供返回值；
reduce(func, seq[, init]) 将二元函数作用于seq 序列的元素，每次携带一对（先前的结果以及下一个序列元素），连续的将现有的结果和下雨给值作用在获
得的随后的结果上，最后减少我们的序列为一个单一的返回值；如果初始值init 给定，第一个比较会是init 和第一个序列元素而不是序列的头两个元素。
（1）filter(func, seq) 
说明：通过一个函数对一个序列操作，返回一个操作为真的序列
目的：基于某一个测试函数过滤出一些元素
#列表模拟
'''
from random import randint as ri
print [n for n in [ri(1,99) for i in range(9)] if n%2]
print range(-5,5)
print filter((lambda x:x>0),range(-5,5))  #结果：[1, 2, 3, 4]

'''
（2）map(func, seq1[,seq2...])   map（函数，传入函数的序列对象）
说明：多个序列相同位置组成的元组作参数传递给函数，返回函数处理后的返回值组成的列表
为每一个元素一次调用function(item)并将返回值组成一个链表返回
'''
#用法1：map()会并行地迭代每个序列。将每个序列相同位置的元素组成一个元组传递给函数
def inc(x):return x+10
L = [1,2,3,4,5]
print map(inc, L)  #结果：[11, 12, 13, 14, 15]
#用法2：map函数另外一个用法，把序列的元素配对起来，但是如果参数长度，不同则会为较短的序列用None补齐
#map(None, seq1,seq2) 最简单的形式
aList=[1,2,3]
bList=['a','b','c']
print map(None,aList,bList)  #结果 [(1, 'a'), (2, 'b'), (3, 'c')]
#用法3：map嵌套lambda
print map((lambda x:x+3),L) #结果：[4, 5, 6, 7, 8]
  
'''
  （3）reduce 使用了一个二元函数（一个接收带两个值作为输入，进行了一些计算然后返回【一个值】作为输出），一个序列，和一个可选的初始化器，卓有成
效地将那个列表的内容“减少”为一个单一的值，如同它的名字一样。在其他的语言中，这种概念也被称作为折叠。
说明：通过一个函数对一个序列操作返回一个值，对每对元素都应用函数并运行到最后结果
返回一个单值, 首先以序列的前两个元素调用函数, 再以返回的值和第三个参数调用, 一次执行下去
'''
print reduce((lambda x,y:x+y),[1,2,3,4]) #结果：10

'''
【六】递归
如果函数包含了对自身的调用，该函数就是递归的

【七】迭代器
1、iterator是迭代器的意思，它的作用是一次产生一个数据项，直到没有为止。这样for循环就可以对他进行循环处理了。
iterator一次只返回一个数据项，占用极少的内存，但它需要记住当前的状态，以便返回下一个数据项，它是一个有着next()方法的对象。
条目全部取出后, 会引发一个 StopIteration 异常, 这并不表示错误发生, 只是告诉外部调用者, 迭代完成.
迭代器的两个基本方法：
（1）next方法：返回容器的下一个元素
（2）__iter__方法：返回迭代器自身
'''

#2、创建迭代器：
#iter()函数创建，对一个对象调用iter()就可以得到他的迭代器，语法如下：iter(obj);iter(func,sentinel)
#如果你创建一个参数给iter(),它会检查你传递的是不是一个序列，如果是，则根据索引从0一直迭代到序列结束
i = iter('abc')
print i.next()  #结果：a
print i.next()  #结果：b
print i.next()  #结果：c
print i.next()  #结果： Traceback (most recent call last)  StopIteration

#3、另一个创建迭代器的方法是使用类：
#一个实现了__iter__()和next()方法的类可以作为迭代器使用。
#class中__init__()方法执行前述的赋值操作。__iter__()仅返回self，这就是如何将一个对象声明为迭代器的方式。
#最后，调用next()来得到迭代器中连续的值。next()控制怎么返回下一个值，顺序，倒序，多个步进，随机等。StopIteration异常需要在next抛出。
class Fib():
    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1
    
    def  __iter__(self):
        return self
    
    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a,self.b =  self.b,self.a+self.b
        return fib

for n in Fib(1000):
    print n

'''
【八】生成器        
1、什么是生成器
当协调程序暂停的时候，我们能从其中获得一个中间的返回值，当调用回到程序中时，能够传入额外或者改变了的参数，但仍然能够从我们上次离开的地方继续，并且所有状态完整。
挂起返回中间值并多次继续的协同程序被称为生成器，那就是python真正在做的事。
生成器是这样一个函数，它记住上一次返回时在函数体中的位置。对生成器函数的第二次（或第 n 次）调用跳转至该函数中间，而上次调用的所有局部变量都保持不变。
生成器不仅“记住”了它数据状态；生成器还“记住”了它在流控制构造（在命令式编程中，这种构造不只是数据值）中的位置。
生成器就是一个带yield语句的功能，返回一个值给调用者并暂停执行，当生成器的next()方法被调用的时候，它会准确地从离开地方继续（当它返回[一个值以及]控制给调用者时）

2、简单的生成器特性
与迭代器相似，生成器以另外的方式来运作：当到达一个真正的返回或者函数结束没有更多的值返回（当调用next())，一个StopIteration 异常就会抛出。
'''
#示例1
def simpleGen():
    yield 1
    yield '2---> punch!'

myG=simpleGen()
print myG.next() #结果：1
print myG.next() #结果：2---> punch!
print myG.next() #结果：Traceback (most recent call last): StopIteration

#示例2
def fib(max): 
    a, b = 0, 1 
    while a < max: 
        yield a 
        a, b = b, a + b

for n in fib(1000): 
    print n

#示例3：我们将要创建一个带序列并从那个序列中返回一个随机元素的随机迭代器
from random import randint
def randGen(aList):
    while len(aList)>0:
        yield aList.pop(randint(0,len(aList)-1))
        
for item in randGen(['rock', 'paper', 'scissors']):
    print item

#使用生成器最好的地方就是当你正迭代穿越一个巨大的数据集合，而重复迭代这个数据集合是一个很麻烦的事，比如一个巨大的磁盘文件，或者一个复杂的数据库查询。
#对于每行的数据，你希望执行非元素的操作以及处理，但当正指向和迭代过它的时候，你“不想失去你的地盘“

'''
2、加强的生成器特性
一些加强特性加入到生成器中，所以除了next()来获得下个生成的值，用户可以将值回送给生成器[send()]，在生成器中抛出异常，以及要求生成器退出[close()]
由于双向的动作涉及到叫做 send()的代码来向生成器发送值（以及生成器返回的值发送回来），
现在yield 语句必须是一个表达式，因为当回到生成器中继续执行的时候，你或许正在接收一个进入的对象
'''

def counter(start_at=0):
    count = start_at
    while True:
        val=(yield count) #直接返回初始值 同时将值赋给val
        if val is not None: #如yield count返回的不是None 则count=val
            count=val
        else:#是None的情况 count加1，也就是yield coun没有东西返回的时候count加以
            count+=1

count=counter(5)
print count.next()  #结果:5
print count.next()  #结果:5
print count.send(9) #结果：9  将9的值送给生成器
print count.next()  #结果：10
count.close()  
print count.next()  #结果：StopIteration

count=counter() 
print count.next() #结果：0

#生成器和迭代器
#生成器是迭代器，同时也并不仅仅是迭代器，不过迭代器之外的用途实在是不多，所以我们可以大声地说：生成器提供了非常方便的自定义迭代器的途径