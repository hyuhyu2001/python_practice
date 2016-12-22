#!/user/bin/env python
#encoding:utf-8

'''
在class语句内，任何赋值语句都产生类属性
class是复合语句，任何种类的语句都可以位于其主体内：print ,=,if,def等
【一】方法
方法位于class语句的主体内，是由def语句建立的函数对象。抽象角度，方法替实例对象提供了要继承的行为
self：类方法的第一个参数通常称为self。这个参数提供方法一个钩子，从而返回调用的主体，也就是实例对象，
    因为类可以产生许多实例对象，所以需要这个参数来管理每个实例彼此各不相同的数据。
1、调用超类的构造器
构造时，python会找出并只调用一个__init__
'''
class Super1:
    def __init__(self,x):
        self.x=x

class Sub1(Super1):
    def __init__(self,x,y):
        Super1.__init__(self,x)  ##调用父类的构造器，为了保证子类的构造方法也会执行超类构造器的逻辑
        self.y=y
I=Sub1(1,2)
print I.y


class Super3:
    def __init__(self):
        self.name='diege'

class Sub3(Super3):
    def setage(self,age): #实验证明子类的__init__方法也会继承，没有任何特殊，超类的任何属性子类都会继承
        self.age=age

X=Sub3() 
print X.name  #结果：diege
'''
2、继承：在Python中，当对对象进行点号运算时，就会发生继承，而且涉及到搜索属性定义树（一或多个命名空间）
object是”所有类之母“，如果你的类没有继承任何其他父类，object将作为默认的父类

3、多重继承：子类可以多重继承多个父类
class C(A,B)

　　...code...

方法解释顺序（MRO-Methon Resolution Order）.2.2版本以前是深度优先，从左至右搜索，取得在子类中使用的属性。
由于类，类型，内建类型的子类经过权限改造，有了新的结构，这种算法不再可行。
2.3使用C3算法。使用广度优先的方式，优先查找同胞兄弟，也就是先查找A，然后再查找B都没查找到再查找A,B更上级父类

4、属性树的构造
命名空间树构造以及填入变量名的方式，通常来说：
（1）实例属性是由对方法内self属性进行赋值运算而生成的
（2）类属性是通过class语句内顶层的语句（赋值语句）而生成的
（3）超类链接通过class语句首行的括号内列出类而生成的。

5、继承方法的专有化 -【重载】
继承树搜索模式，变成了将系统专有化的最好方式。因为继承会先在子类寻找变量名，然后才查找超类，
子类就可以对超类的属性重新定义来取代默认的行为。
把系统做成类的层次，再新增外部的子类来对其进行扩展，而不是在原处修改已存在的逻辑。重新定义继承变量名的概念因出了各种专有化技术
'''
#继承和重载实例
class Super2:
    def method(self):
        print 'in Super.method'

class Sub2(Super2):                 
    def method(self):             
        print 'start Sub.method'
        Super2.method(self)     #直接调用超类的方法
        print 'ending Sub.method'   
        
z = Super2()
print z.method() #结果：in Super.method

m = Sub2()
print m.method()  #结果：in Super.method     in Super.method      start Sub.method
#直接调用超类的方法是这里的重点。Sub2类以其专有化的版本取代了Super2的方法函数。但是取代时，Sub2又回调了Super2所导出的版本，从而实现了默认的行为，
#换句话说，Sub2.mothod只是扩展了Supe2r.mothod的行为，而不是完全取代他。这种扩展编码模式常常用于构造器方法。 也是重载

'''
6、类接口技术
'''
class Super:
    def method(self):
        print "in Super.method"
    def delegate(self):
        self.action()  #调用实例的方法
class Inheritor(Super):
    pass
class Replacer(Super):
    def method(self): #用自己的版本覆盖Super的method
        print "in Replacer.method"
class Extender(Super):
    def method(self):  #覆盖并回调默认的method，从而定制Super的method
        print "starting Extender.method"
        Super.method(self)
        print "ending Extender.method"
class Provider(Super):
    def action(self):  # 现实Super的delegate方法预期的action方法.这里有点不好理解
        print "in Provider.method"
'''
Provider继承了Super的method和delegate方法并增加了action方法，而delegate方法是调用实例的action方法实现的。
尾部的自我测试程序代码在for循环中建立了三个不同的实例。因为类是对象，可以将他们放入元组中，并可以通过这样的方式创建实例。
类有特殊的属性__name__类的名字，就像模块一样有__name__属性模块的名字。类中默认为类行首行中的类名称的字符串
'''

if __name__ == '__main__':
    for c in(Inheritor,Replacer,Extender):
        print '\n' + c.__name__ + '...'
        
        c().method() #C后面的括号表面是类时实例，这里是创建实例和方法调用一起了。分解C=Inheritor(),C.method()
        
        print '\nProvider...'
        x = Provider() #创建实例对象
        x.delegate()  #实例对象条用delegate方法，delegate方法通过实例的action方法实现
'''
结果：
Inheritor...
in Super.method

Provider...
in Provider.method

Replacer...
in Replacer.method

Provider...
in Provider.method

Extender...
starting Extender.method
in Super.method
ending Extender.method
'''

'''
7、抽象超类
上例中Provider类如何工作的？当通过Provider类的实例调用delegate方法时,两个独立的继承搜索会发生：
（1）最初x.delegate的调用中，Python会搜索Provider实例和它上层的对象。知道在Super中找到delegate方法。实例x会像往常一样传递给这个方法self参数
（2）Super.delegate方法中,self.action会对self及其它上层的对象启动新的独立继承搜索，因为self指的是Provider实例，就会找到Provider中的action方法。

抽象类就是会调用方法的类，但没有继承或定义该方法，而是期待该方法由子类填补。
当行为无法预测，非得等到更为具体的子类编写时才知道，通过可用这种方式把类通用话。

这种“填空”的代码结构一般就是OOP软件的框架。从delegate方法的角度来看，这个例子中的超类有时也称作是抽象类--
也就是类的部分行为默认是由其子类所提供的。如果预期的方法没有在子类定义，当继承搜索失败时，Python会引发为定义变量名的异常。
类的编写者偶尔会使用assert语句，使这种子类需求更为明显，或者引发内置的异常NotImplementedError
'''
class Super4:
    def method(self):
        print "in Super.method"
    def delegate(self):
        self.action()
    def action(self):
        assert 0, 'action must be defind'
#如果表达式运算结构为假，就会引发带有错误信息的异常。在这里表达式总是为假(0）。因为如果没有方法重新定义，继承就会找到这里的版本，触发错误信息。

'''
【二】类属性、实例、实例属性
1、类属性：
属性就是属另一个对象的数据或者函数元素
类属性就是与其被定义的类绑定
python所有方法的步骤：定义类（和方法）-- 创建一个实例 -- 用这个实例调用这个方法
（1）类的数据属性：仅仅是类的变量，这个变量要么在由类中的方法来更新，要么在主程序其他什么地方被更新。
这种数据位静态数据，或静态变量。它们表示这些数据和它们所属的类对象绑定的，不依赖于任何类实例。
（2）查看类的属性
dir()方法或者访问类字典属性__dict__.
dir(Class)返回的仅是对象属性的一个名字列表,没有属性对应的值，也就是__dict__属性的健。
Class.__dict__ 返回一个字典，它的键(key)是属性名，键值(value)是相应的属性对象的数据值。
（3）特殊的类属性
对任何类Ｃ，显示了类Ｃ的所有特殊属性：
C.__name__ 类Ｃ的名字（字符串）
C.__doc__ 类Ｃ的文档字符串
C.__bases__ 类Ｃ的所有父类构成的元组
C.__dict__ 类Ｃ的属性
C.__module__ 类Ｃ定义所在的模块（1.5 版本新增）
C.__class__ 实例Ｃ对应的类（仅新式类中

2、实例
如果说类是一种数据结构定义类型，那么实例则声明了一个这种类型的变量。
(1)初始化
class MyClass(object): # define class 定义类
... pass
mc = MyClass() # instantiate class 初始化类
(2)__init__() "构造器"方法
(3)__new__() “构造器”方法
(4)__del__() "解构器"方法

3、实例属性
构造器是最早可以设置实例属性的地方，因为__init__()是实例创建后第一个被调用的方法。再没有比这更早的可以设置实例属性的机会了。
一旦__init__()执行完毕，返回实例对象，即完成了实例化过程

4、实例属性 vs 类属性
类属性仅是与类相关的数据值，和实例属性不同，类属性和实例无关。这些值像静态成员那样被引用，即使在多次实例化中调用类，它们的值都保持不变。
不管如何，静态成员不会因为实例而改变它们的值，除非实例中显式改变它们的值。（实例属性与类属性的比较，类似于自动变量和静态变量
类和实例都是名字空间。类是类属性的名字空间，实例则是实例属性的。你可采用类来访问类属性，如果实例没有同名的属性的话，你也可以用实例来访问。
'''
#（1）访问类属性
class C(object): # define class 定义类
    version = 1.2 # static member 静态成员  

c = C() # instantiation 实例化
print C.version # access via class 通过类来访问    1.2
print c.version # access via instance 通过实例来访问  1.2
C.version += 0.1 # update (only) via class 通过类（只能这样）来更新
print C.version # class access 类访问 1.3 
print c.version # instance access, which 实例访问它，其值已被改变# also reflected change   1.3

'''
（2）从实例中访问类属性需谨慎
与通常Python 变量一样，任何对实例属性的赋值都会创建一个实例属性（如果不存在的话）并且对其赋值。
如果类属性中存在同名的属性，有趣的副作用即产生。（经典类和新式类都存在）
类属性在不可变的情况下正常。
'''
#在类属性可变的情况下，一切都不同了
class Foo(object):
    x = {2003: 'poe2'}

foo = Foo()
print foo.x #{2003: 'poe2'}
foo.x[2004] = 'valid path'
print foo.x  #{2003: 'poe2', 2004: 'valid path'}
print Foo.x # it works!!! 生效了 {2003: 'poe2', 2004: 'valid path'}
#del foo.x # no shadow so cannot delete 没有遮蔽所以不能删除掉

'''
(3)类属性持久性
静态成员，如其名所言，任凭整个实例（及其属性）的如何进展，它都不理不采（因此独立于实例）。
同时，当一个实例在类属性被修改后才创建，那么更新的值就将生效。类属性的修改会影响到所有的实例
注意：使用类属性来修改自身（不是实例属性）
正如上面所看到的那样，使用实例属性来试着修改类属性是很危险的。
原因在于实例拥有它们自已的属性集，在Python 中没有明确的方法来指示你想要修改同名的类属性。修改类属性需要使用类名，而不是实例名。
'''

'''
【四】绑定和方法调用
1）显式传入self为非绑定方法
2）隐式传入slef参数为绑定方法，即通过实例来调用方法。
首先，方法仅仅是类内部定义的函数。(这意味着方法是类属性而不是实例属性)。
其次，方法只有在其所属的类拥有实例时，才能被调用。当存在一个实例时，方法才被认为是绑定到那个实例了。没有实例时方法就是未绑定的。
最后，任何一个方法定义中的第一个参数都是变量self，它表示调用此方法的实例对象。

关于self
self 变量用于在类实例方法中引用方法所绑定的实例。因为方法的实例在任何方法调用中总是作为第一个参数传递的，self 被选中用来代表实例。
你必须在方法声明中放上self，但可以在方法中不使用实例(self)。
如果你的方法中没有用到self , 那么请考虑创建一个常规函数，除非你有特别的原因，比如子类继承需要重载父类的方法。

1、调用绑定方法
方法，不管绑定与否，都是由相同的代码组成的。唯一的不同在于是否存在一个实例可以调用此方法。
记得self 在每一个方法声明中都是作为第一个参数传递的。当你在实例中调用一个绑定的方法时，self 不需要明确地传入了。
这算是"必须声明self 作为第一个参数"对你的报酬。当你还没有一个实例并且需要调用一个非绑定方法的时候你必须传递self 参数

2、调用非绑定方法
调用非绑定方法并不经常用到。
需要调用一个还没有任何实例的类中的方法的一个主要的场景是:你在派生一个子类,而且你要覆盖父类的方法，这时你需要调用那个父类中想要覆盖掉的构造方法。
重载父类构造器__init__
class EmplAddrBookEntry(AddrBookEntry):
    #'Employee Address Book Entry class' # 员工地址记录条目
    def __init__(self, nm, ph, em):
        AddrBookEntry.__init__(self, nm, ph) #要继承类的构造器，然后再增加其他类实例的属性。
        self.empid = id
        self.email = em
'''

'''
【五】静态方法和类方法
'''
#1、staticmethod()和classmethod()内建函数
#看一下在经典类中创建静态方法和类方法的一些例子：
class TestStaticMethod:
    def foo():
        print 'calling static method foo()'
    foo = staticmethod(foo)

class TestClassMethod:
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__
    foo = classmethod(foo)

#2、使用函数修饰符【可以考虑使用】
class TestStaticMethod1:
    @staticmethod
    def foo():
        print 'calling static method foo()'


class TestClassMethod1:
    @classmethod
    def foo(cls):
        print 'calling class method foo()'
        print 'foo() is part of class:', cls.__name__
        
'''
【六】类、实例和其他对象的内建函数

内建函数 描述
issubclass(sub, sup)　　如果类sub是类sup的子类,则返回True,反之,为False。
isinstance(obj1, obj2)　　如果实例obj1是类obj2,或者obj2子类的一个实例；或者如果obj1是obj2的类型,则返回True；反之,为False。
hasattr(obj, attr)　　　　如果obj有属性attr(用字符串给出),返回True,反之,返回False
getattr(obj, attr[, default])　　获取obj的attr属性；与返回obj.attr 类似；如果提供了默认值，则返回默认值；如果attr不是obj的属性，就会引发一个AttributeError 异常。会在你试图读取一个不存在的属性时，引发AttributeError 异常，除非给出那个可选的默认参数。

setattr(obj, attr, val) 设置obj的attr属性值为val,替换任何已存在的属性值；不然，就创建属性；类似于obj.attr=val
delattr(obj, attr) 从obj中删除属性attr(以字符串给出)；类似于del obj.attr。
dir(obj=None) 返回obj的属性的一个列表；如果没有给定obj，dir()则显示局部名字空间空间中的属性，也就是locals().keys()
super(type, obj=None) 返回一个表示父类类型的代理对象；如果没有传入obj，则返回的super对象是非绑定的；反之，如果obj 是一个type,issubclass(obj,type)必为True:否则，isinstance(obj,type)就必为True。
vars(obj=None) 返回obj的属性及其值的一个字典；如果没有给出obj，vars()显示局部名字空间字典（属性及其值），也就是locals()

dir()补充
(1)dir()作用在实例上（经典类或新式类）时，显示实例变量，还有在实例所在的类及所有它的基类中定义的方法和类属性。
(2)dir()作用在类上（经典类或新式类）时，则显示类以及它的所有基类的__dict__中的内容。但它不会显示定义在元类（metaclass）中的类属性。
(3)dir()作用在模块上时，则显示模块的__dict__的内容。（这没改动）。
(4)dir()不带参数时，则显示调用者的局部变量。（也没改动）。
(5)关于更多细节:对于那些覆盖了__dict__或__class__属性的对象，就使用它们；出于向后兼容的考虑，如果已定义了__members__和__methods__，则使用它们。

【七】运算符重载
【八】命名空间:完整的内容
 
'''