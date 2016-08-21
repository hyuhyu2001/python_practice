#!/user/bin/env python
#encoding:utf-8

'''
python核心编程第四章练习


4-1.Python对象。与所有Python对象有关的三个属性是什么？请简单的描述一下。 
所有的Python对象都拥有三个特性：身份，类型和值。 
（1）身份：每一个对象都有一个唯一的身份标识自己，任何对象的身份可以使用内建函数id()来得到。这个值可以被认为是该对象的内存地址。 
（2）类型：对象的类型决定了该对象可以保存什么类型的值，可以进行什么样的操作，以及遵循什么样的规则。可以使用内建函数type()查看对象的类型。
在Python中类型也是对象。 
（3）值：对象标识的数据项。  

4-2.类型。不可更改（immutable）指的是什么？Python的哪些类型是可更改（mutable）的，哪些不是？ 
不可更改指对象创建以后值不可以更新。 immutable的类型：数字，字符串，元组 mutable的类型：列表，字典  

4-3.类型。哪些Python类型是按照顺序访问的，他们和映射类型的不同是什么？ 
string,tuple,list是按照顺序访问的。 
字典是映射访问。字典中的元素，他们的索引并不使用顺序的数字偏移量取值，它的元素无序存放，通过一个唯一的键来访问。 

4-4.type()。内建函数type()作什么？type()返回的对象是什么？ 
答案：内建函数type()返回任意Ptrhon对象的数据类型，而不局限于标准类型。 type()返回的值是一个类型对象。 
 
4-5.str()和repr()。内建函数str()与repr()之间的不同是什么？哪一个等价于反引号（``）操作符？ 
内建函数str()和repr()或反引号操作符('')可以方便的以字符串的方式获取对象的内容、类型、数值属性等信息。
str()函数得到的字符串可读性好，而repr()函数得到的字符串通常可以用来重新获得该对象，通常情况下obj == eval(repr(obj))这个等式是成立的。
这两个函数接受一个对象作为其参数，返回适当的字符串。 
repr()输出对Python比较友好，而str()的输出对用户比较友好。 
str()致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于eval()求值。 '' == repr()，但反引号('')操作符已经不鼓励继续使用。 

eval()函数十分强大，官方demo解释为：将字符串str当成有效的表达式来求值并返回计算结果。 
eval参数是一个字符串，可以把这个字符串当成表达式来求值。比如有一个变量A=1，evil（A+1），结果就是2

4-6.对象相等。你认为type(a) == type(b)和type(a) is type(b)之间的不同是什么？为什么会选者后者？函数isinstance()与这有什么关系？ 
“==”比较的是值，is比较的是对象。因为每个对象只可能有一种类型的值，所以可以直接比较他们的ID，而不用先计算值再做比较。 
函数isinstance()用来确定这个对象是否属于这个类型，或者实例是否属于某个类。

4-7、dir()函数，声明对象的函数

4-8.列表和元组。列表和元组的相同点是什么？不同点是什么？ 
list是处理一组有序项目的数据结构，即你可以在一个列表中存储一个序列的项目。
列表中的项目应该包括在[]中，这样python就知道你是在指明一个列表。一旦你创建了一个列表，你就可以添加，删除，或者是搜索列表中的项目。
由于你可以增加或删除项目，我们说列表是可变的数据类型，即这种类型是可以被改变的。 列表是可以嵌套的。  
元组和列表十分相似，不过元组是不可变的。即你不能修改元组。元组通过()中用逗号分隔的项目定义。 
元组通常用在使语句或用户定义的函数能够安全的采用一组值的时候，即被使用的元组的值不会改变。元组可以嵌套
'''

#检查类型函数，最有方案
def displayNumType(num):
    print num,'is',
    if isinstance(num,(int,long,float,complex)): #isinstance()接受一个类型对象的元组作为参数
        print 'a number of type:',type(num).__name__ #通过type()函数确认数值的类型
    else:
        print 'not a number at all!'
    
displayNumType(-69)
displayNumType(999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')

def display_Number_Worst(number):   
    print number,'is'  
    if type(number)==type(0):   
        print 'a number of type:',type(0).__name__   
    elif type(number)==type(0L):   
        print 'a number of type:',type(0L).__name__   
    elif type(number)==type(0.0):   
        print 'a number of type:',type(0.0).__name__   
    elif type(number)==type(0.0+0.0j):   
        print 'a number of type:',type(0.0+0.0j).__name__   
    else :   
        print 'not a number at all'  
def display_Number_Better(number):   
    print number,'is'  
    if type(number) is IntType:   
        print 'a number of type: int'  
    elif type(number) is FloatType:   
        print 'a number of type:float'  
    elif type(number) is LongType:   
        print 'a number of type:Long'  
    elif type(number) is ComplexType:   
        print 'a number of type:Complex'  
    else:   
        print 'not a number at all'  
def display_Number_Good(number):   
    print number,'is'  
    if type(number) == IntType:   
        print 'a number of type: int'  
    elif type(number) == FloatType:   
        print 'a number of type:float'  
    elif type(number) == LongType:   
        print 'a number of type:Long'  
    elif type(number) == ComplexType:   
        print 'a number of type:Complex'  
    else:   
        print 'not a number at all'         
if __name__=='__main__':    
#    display_Number_Worst(554454)   
#    display_Number_Worst(10.11)   
#    display_Number_Worst(10.0+10.0j)   
#    display_Number_Worst("sdfsdfsd")       
#    display_Number_Better(45654)   
#    display_Number_Better(10.0)   
#    display_Number_Better(10.0+10.0j)   
#    display_Number_Better(8888888888888888)   
#    display_Number_Better('xxx')   
#    display_Number_Good(21554)   
#    display_Number_Good(8888888888888888888888888)   
#    display_Number_Good(10.0)   
#    display_Number_Good(10.0+10.0j)   
#    display_Number_Good('my')   

