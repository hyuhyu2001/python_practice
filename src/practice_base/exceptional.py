#!/user/bin/env python
#encoding:utf-8

'''
【一】
try/except：
捕捉由代码中的异常并恢复，匹配except里面的错误，并自行except中定义的代码，后继续执行程序
（发生异常后，由except捕捉到异常后，不会中断程序，继续执行try语句后面的程序）
try/finally: 无论异常是否发生，都执行清理行为 （发生异常时程序会中断程序，只不过会执行finally后的代码）
raise：手动在代码中触发异常
assert：有条件的在程序代码中触发异常
with/as：在python2.6和后续版本中实现环境管理器
用户定义的异常要写成类的实例，而不是字符串。。。
finally和except和else可以出现在相同的try语句中
'''

#1、异常的角色
x = 'abcde'
def fetcher(obj,index):
    return obj[index]  
'''
#fetcher(x,5) #由于没有第5个下标，报错：IndexError: string index out of range
#修改为
try:
    fetcher(x,5)   #尝试抓取第5个字符
except IndexError: #如果发生异常【指出引发的异常名称】
    print fetcher(x,-1) #那就抓取最后一个字符,结果：e
'''
    
try:
    print fetcher(x,4)   
finally: 
    print 'after fetch' #没有发生异常，也会执行finally的语句；；即使发生异常，也会执行finally里的语句
#总结：try/except的组合可用于捕捉异常并从中恢复，而try/finally的组合则很方便，可以确保无论try代码块内的代码是否发生异常，终止行为一定会运行。
#如，try/except来捕捉第三方库导入的代码所引发的错误，然后以try/finally来确保关闭文件，或者终止服务器连接等调用。
#可以在同一个try语句内混合except和finally分句:finally一定回执行，无论是否有异常引发，而且不也不关异常是否被except分句捕捉到

#2、try/except/else语句
#else是可选的；try首行底下的代码块代表此语句的主要动作：试着执行的程序代码。except分句定义try代码块内引发的异常处理器，而else分句（如果有）则是提供没有发生异常时候要执行的处理器
#也就是说except分句会捕捉try代码块执行时所有发生的任何异常，而else分句只在try代码执行没有发生异常时才执行，finally分句无法释放发生异常都执行 


'''
3、try语句分句形式
except:    捕捉所有（其他）异常类型
except name:    只捕捉特定的异常
except name,value:    捕捉所有的异常和其额外的数据（或实例）
except (name1,name2) 捕捉任何列出的异常
except (name1,name2),value: 捕捉任何列出的异常，并取得其额外数据
else:    如果没有引发异常，就运行
finally:    总是会运行此代码块，无论是否发生异常
except:用在想不到异常情况，在except:前面可以定义可以想到的异常：except name1: except name2:

4、统一try/except/finally分句
try:
    main-action:
except Exception1,e:
    hander1
    print e
except Exception2:
    hander2
...
else:
    else-block
finally:
    finally-block
这语句中main-action代码会先执行。如果该程序代码（main-action）引发异常，那么except代码块都会逐一测试，寻找与抛出的异常相符的语句。
如果引发异常的是Exception1则会执行hander1代码块，如果引发异常的是Exception2，则会执行hander2代码块。以此类推。
如果没有引发异常，将会执行else-block代码块。
无论前面发生什么，当main-action代码块完成时。finally-block都会执行
try语句里可以嵌套try语句
4.1、通过嵌套合并except和finally
try:
    try:
        main-action:
    except Exception1:
        hander1
    except Exception2:
        hander2
    ...
    else:
        else-block
finally:
    finally-block

#5、raise语句
要故意触发异常，可以使用raise语句。raise语句组成是： raise关键字，后面跟着要引发的异常名称（选用），以及一个可选的额外的数据项，后可随着异常传递
raise <name>
raise <name>,<data>
raise
注意：<name>需要预先定义好，不然会由未定义错误。
第二种形式随着异常传递额外的数据项，在raise语句中，数据是列在异常名称的后面的；在try语句中，取得该数据是通过引入一个进行接收
它的变量实现的。例如，如果try引入一个exceptname,X:语句，则变量X就会被赋值为raise内所列出的额外的数据项,如果没有定义默认接受到
的就是特殊对象None。一旦被程序中任意的except分句捕捉，异常就死了（也就是说，不会传递给另一个try），除非又被另一个raise语句或
错误所引发。现在用户定义的异常应该是类实例对象。

rasie 语法 描述
raise exclass 触发一个异常,从exclass 生成一个实例(不含任何异常参数)
raise exclass() 同上,除了现在不是类;通过函数调用操作符(function calloperator:
"()")作用于类名生成一个新的exclass 实例,同样也没有异常参数
raise exclass, args 同上,但同时提供的异常参数args,可以是一个参数也可以元组
raise exclass(args) 同上
raise exclass,args, tb 同上,但提供一个追踪(traceback)对象tb 供使用
raise exclass,instance 通过实例触发异常(通常是exclass 的实例);如果实例是exclass
的子类实例,那么这个新异常的类型会是子类的类型(而不是
exclass);如果实例既不是exclass 的实例也不是exclass 子类的
实例,那么会复制此实例为异常参数去生成一个新的exclass 实例.
raise instance 通过实例触发异常: 异常类型是实例的类型; 等价于raise
instance.__class__, instance (同上).
raise string (过时的) 触发字符串异常
raise string, args 同上,但触发伴随着args
raise string, args, tb 同上,但提供了一个追踪(traceback)对象tb 供使用
raise (1.5 新增)重新触发前一个异常,如果之前没有异常,触发TypeError
'''
    
#6、assert语句 断言
#assert可以有条件地在程序代码中触发异常，可以认为是有条件的raise
#牢记：assert几乎都是用来收集用户定义的约束条件，而不是捕捉内在的程序设计错误。因为Python会自动收集程序的设计错误，通常咩有必要写assert去捕捉超出索引值，类型不匹配以及除数为0之类的事
#引发的异常为:AssertionError。如果没有被try捕捉到，就会终止程序。
#该语句形式:assert <test>,<data>  

def f(x):
    assert x>0,'x must be great zerot'  #assert后面的表达式为真，则什么都不做，如果不为真，就会抛出AssertionErro异常
    return x**2
try:
    f(-1)  #结果：AssertionError: x must be great zerot
except AssertionError,e:
    print e   #结果：x must be great zerot

#高级示例2：
try:
    assert 1 == 0,'one does not equal zero'
except AssertionError,args:
    print '%s:%s' % (args.__class__.__name__,args)  #结果：AssertionError:one does not equal zero
    
'''
【二】with/as环境管理
python2.6引入新的异常相关语句，with以及可选的as语句。这个语句的设计是为了和环境管理器对象（支持新的方法协议）一起工作
简而言之：with/as语句的设计作为常见try/finally用法模式的替代方案，就像try/finally语句， with/as语句也用于定义必须执行的
终止或“清理"行为,无论步骤中是否发生异常。
和try/finally不同的是，with语句支持更丰富的基于对象的协议，可以代码块定义支持进入和离开动作。
with语句基本格式：
with expression [as variable]:
with block

    
with open('/etc/rc.conf') as myfile:
    for line in myfile:
        line=line.upper()
        print line
'''     
'''
【三】异常对象
基于类的异常可以创建各种异常类，有附加状态信息，而且支持继承。尽量都适用类异常。类异常有如下特点
（1）、提供类型分类，对今后的修改有更好的支持：以后增加新异常时，通常不需要在try语句中进行修改。
（2）、同了存储在try处理器中所使用的环境信息的合理地点：这样的话，可以拥有状态信息，以及可调用的方法，并且可通过实例进行读取。
（3）、  允许异常参与继承层次，从而可获得共同的行为。例如，继承的显示方法可提供通用的错误消息外观。
注意：基于字符串异常，2.7版以及不在支持了
'''
#2、基于类的异常
class General:
    pass
class Spec1(General):
    pass 
class Spec2(General):
    pass 
def raiseer0():
    X=General() 
    raise X
def raiseer1(): 
    X=Spec1() 
    raise X 
def raiseer2(): 
    X=Spec2() 
    raise X

for func in (raiseer0,raiseer1,raiseer2):
    try:
        func()
    except General:#使用异常的超类General，这样子类也捕捉到，可以在未来增加函数异常（在子类里)，而不影响程序。
        import sys
        print 'caught:',sys.exc_info()[0]
#在try语句中，捕捉其超类就会捕捉这个类，以及类树中超类下的所有子类：超类会变成异常分类的名称，而子类会变成该分类中特定的异常类型。
#Python2.5以后版本将每个异常都写成类（必须),从异常树顶层继承Exception（非必须）

'''
3、内置Exception类
Python把内置异常组织成层次，来支持各种捕捉模式
Exception：    异常的顶层根超类
StandardError:    所有内置错误异常的超类
ArithmeticError:    所有数值错误的超类
OverflowError:    识别特定的数值错误的子类
'''
#可以在Python库手册或exceptionsn模块的帮助文本中查阅。
import exceptions
help(exceptions) 

#4、定义异常文本
#对基于类的异常而已，其结果中第一个元素就是引发异常类，而第二个是实际引发的实例。

#5、发送额外数据和实例行为
#把环境信息附加在基于类的异常的办法是：在引发的实例对象中填写实例的属性，通常是在类的构造器方法中。
#在异常处理器中，是列出要赋值为引发的实例的变量，然后通过这个变量名来读取附加的转改信息，并且调用任何基础的类方法。【很强大的功能】

class FormatError:
    def __init__(self,line,file):
        self.line=line
        self.file=file
        def parser():
            raise FormatError(42,file='diege.txt') #手动定义异常，基于类的异常，类构造函数传递两个数据。
        try:
            parser()
        except FormatError,X: #定义接受异常(类的实例-异常引发时产生的实例)传递过来数据的变量。
            print 'Error at',X.file,X.line #显示实例传递过来的数据
            

#【四】异常的设计

#1、嵌套异常处理器:
#(1)把内部的try写成函数来嵌套
def action2():
    print 1+[]
def action1():
    try:
        action2()
    except TypeError:
        print "inner try"
try:
    action1() 
except TypeError:
    print "outer try"

#(2)、使用语法嵌套
try:
    action2() 
except TypeError:
    print "inner try" 
except TypeError:
    print "outer try"
    
'''
【五】异常和sys模块
另一种获取异常信息的途径是通过sys 模块中exc_info()函数. 此功能提供了一个3 元组(3-tuple)的信息, 多于我们单纯用异常参数所能获得. 让我们看看如何用sys.exc_info() 

在旧版本中的Python 中, 这三个值分别存在于sys 模块, 为sys.exc_type , sys.exc_value ,
sys.exc_traceback . 不幸的是, 这三者是全局变量而不是线程安全的. 我们建议亡羊补牢, 用
sys.exc_info()来代替. 在未来版本Python 中,所有这三个变量都将被逐步停用,并最终移除
'''
try:
    float('abc123')
except:
    import sys
    exc_tuple = sys.exc_info()

for eachItem in exc_tuple:
    print eachItem
    
'''
【六】、异常相关模块
exceptions 内建异常(永远不用导入这个模块)
contextliba 为使用with 语句的上下文对象工具
sys 包含各种异常相关的对象和函数(见sys.ex*)

'''
