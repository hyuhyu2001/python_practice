#!/user/bin/env python
#encoding:utf-8

'''
类的设计
【一】Python和OOP
Python和OOP实现可以概括为三个概念
（1）继承：继承是基于Python中属性查找（在X.name表达式中）
（2）多态：在X.method方法中，method的意义取决于X的类型（类）
（3）封装：方法和运算符实现行为，数据隐藏默认是一种惯例。
    封装指的是在Python中打包，也就是把实现的细节隐藏在对象接口之后。这并不代表有强制的私有性。封装可以让对象接口的现实出现变动时，不影响这个对象的用户。

1、不要通过调用标记进行重载
不要在同一个类中对同一个方法名定义两次，后面的会覆盖前面，也不要对对象类型进行测试。应该把程序代码写成预期的对象接口。而不是特定类型的数据类型。
2、类作为记录
通过类的实例来创建多个记录。
3、类和继承：是“一个”关系 （is a)
从程序员的角度来看，继承是由属性点号运算启动的，由此触发实例，类以及任何超类中变量名搜索。
从设计师的角度看，继承是一种定义集合成员关系的方式：类定义了一组内容属性，可由更具体的集合（子类）继承和定制。
子类和超类的继承是1对1的关系.
'''
#PizzaRobot是一种Chef,Chef是一种Employee.以OOP术语来看，我们称这些关系为“是一个连接”(is a)：机器人是个主厨，主厨是一个员工。

class Employee:
    def __init__(self,name,salary=0):
        self.name = name
        self.salary =  salary
    def giveRaise(self,percent):
        self.salary = self.salary + (self.salary*percent) 
    def work(self):
        print self.name,"does stuff"
    def __repr__(self):
        return "<Employee:name=%s,salary=%s>" % (self.name,self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 5000)
    def work(self):
        print self.name,"make food"
class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print self.name,"interface with customer"
class PizzaRobot(Chef):  
    def __init__(self,name):#有点想不明白，既然继承就够了，为什么还要在这里构造
        Chef.__init__(self,name) #Chef.__init__(self,name) =》Employee.__init__(self,name,5000)=>__init__(self,name,salary=0)
    def work(self):
        print self.name,"make pizza"
      
if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print bob
    bob.work()
    bob.giveRaise(0.20)
    print bob

'''
4、类和组合：”有一个“关系 （has a)
从程序员的角度来看，组合设计到把其他对象嵌入到容器对象内，并使其实现容器方法。
对设计师来说，组合是另一种表示问题领域中的关系的方法。
但是组合不是集合的成员关系，而是组件，也是整体的组成部分。
组合也反映了个组成部分之间的关系，通常称为“有一个”(has a)关系。Python中，“组合”（聚合）就是指内嵌对象集合体。
组合类一般都提供自己的接口，并通过内嵌的对象来实现接口。
现在，我们有了员工，把他们放到披萨店。我们的披萨店是一个组合对象，有烤炉，也有服务员和主厨这些员工。
当顾客来下单时，店里的组件就开始行动：服务员接下订单，主厨制作披萨等。。pizzashop.py模拟
'''
#from employees import PizzaRobot,Server
class Customer:
    def __init__(self,name):
        self.name = name
    def order(self,server):
        print self.name,"orders from",server
    def pay(self,server):
        print self.name,"pays for item to",server
        
class Oven:
    def bake(self):
        print  "oven bakes"

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    def order(self,name):
        customer = Customer(name)
        customer.order(self.name)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)
        
if __name__=="__main__":
    try:
        customer=getargv[1]
    except IndexError:
        print "please give argv as customer!"
    else:
        scene=PizzaShop()
        scene.order(customer)
        print '...'
        
#5、重访流处理器

# vim streams.py

class Processor:
    def __init__(self,reader,writer):
        self.reader=reader
        self.writer=writer
    def process(self):
        while 1:
            data=self.reader.readline()
            if not data:
                break #这里有错误是not
            data=self.converter(data)
            self.writer.write(data)  #这里有错误write
    def converter(self,data):
        assert 0,'converter must be defined'
    

'''
【二】OOP和委托
所谓的委托，通常就是指控制器对象内嵌其他对象，而把运算请求传给那些对象。控制器负责管理工作
在Python中，委托通常是以__getattr__钩子方法实现的，因为这个方法会拦截对不存在属性的读取，包装类（代理类）可以使用
__getattr__把任意读取转发给包装的对象。包装类包有被包括对象的接口。而且自己也可以增加其他运算。
'''      
class wrapper:
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self,attrname):#__getattr__点号运算，这里重载内置getattr方法打印传入类执行的方法，并把属性请求传入给对象，使用对象默认的方法。委托
        print 'Trace:',attrname
        return getattr(self.wrapped,attrname)
'''
__getattr__会获得属性名称字符串。这个程序代码利用getattr内置函数，以变量名字符串从包裹对象取出属性：getattr(X,Z)
就像X.N，只不过N是表达式，可以在运行时计算出字符串，而不是变量。getattr(X,Z)类似于X.__dict__[N].
可以使用这个模块包装类的做法，管理人和带有属性的对象的存取：列表，字典甚至是类和实例。
在这里wrapper类只是在每个属性读取时打印跟踪信息，【并把属性请求委托给嵌入的wrapped对象。（对象自己的方法）】
'''
x=wrapper([1,2,3])
x.append(4)
x.wrapped #[1, 2, 3, 4]
x.__dict__ #{'wrapped': [1, 2, 3, 4]}

y=wrapper({"a":1,"b":2})
y.keys() #['a', 'b']
y.__dict_  #{'wrapped': {'a': 1, 'b': 2}}

'''
【三】多重继承
最新版本是广度优先
在class语句中，首行括号内可以列出一个以上的超类。当这么做时，就在使用所谓的多重继承：类和其实例继承了列出的所有超类的变量。
搜索属性时，Python会由左到右搜索类首行中的超类，直到找到相符者。【纵向搜索】
通常意义上讲，多重继承是模拟属于一个集合以上的对象的好办法，例如一个人可以是工程师，作家，音乐家。因为，可以继承这些集合的特性。
多重继承最常见的用户是作为“混合”超类的通用方法。这类超类一般都称呼混合类：他们提供方法，可以通过继承将其加入应用类。

【四】类是对象：通用对象的工厂
类是对象，因此它很容易在程序中进行传递，保存在数据库结构中。也可以把类传给产生任意种类对象的函数。
这类函数在OOP设计领域偶尔称为工厂。
工厂式的函数或程序代码，在一些情况下很方便，因为他们可以让我们取出并传入没有预先在程序代码中硬编码的类。
实际上，这些类在编写程序时可能还不存在。抽象类

【五】方法是对象：绑定或无绑定
方法也是一种对象，很像函数。类方法能有实例或类来读取。实际上Python中就有两种方式。

1、无绑定类方法对象：无self
   通过对类进行点号运算从而获取类的函数属性，会传回无绑定(unboud)方法对象。调用该方法时，【必须明确提供实例对象】作为第一个参数。
2、绑定实例方法对象：self+函数对
   通过对实例进行全运算从而获取类的函数属性，会传回绑定（bound)方法对象。Python在绑定方法对象中自动把实例和函数打包，所以，不用传递实例去调用该方法。实例已拥有该方法。

这两种方法都是功能齐全的对象，可四处传递，保持在列表内等。执行时两者都需要第一参数的实例（也就是self的值）
调用绑定方法对象时，Python会自动提供实例来创建绑定方法对象的实例。
也就是说绑定方法对象通常都可以和简单函数对象互换，而且对原本就是针对函数而编写的接口而言，非常用有。

【六】类和模块
都是命名空间
模块
    * 是数据/逻辑套件        
    * 由Python文件或C扩展编写成
    * 通过导入使用

类
    *实现新的对象
    *由class语句创建
    *通过调用使用
    *总是存在于模块中。
类支持其他模块不支持的功能。例如，运算符重载，产生多个实例以及继承。

小结：

委托：把对象包装在代理类中
组合：控制嵌入的对象
继承：从其他类中获取行为
多重继承，绑定方法，工厂函数
'''
