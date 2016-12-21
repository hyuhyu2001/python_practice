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
'''
        