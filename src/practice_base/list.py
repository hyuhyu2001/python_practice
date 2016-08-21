#!/user/bin/env python
#encoding:utf-8

'''
列表是Python中最基本的数据结构，列表是最常用的Python数据类型，列表的数据项不需要具有相同的类型。
列表中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
'''

#创建列表方法
Ed = ["Gumby",42] #直接声明
AD = 'hello','world'#通过list()创建  list(AD)=['hello', 'world']
print list('hello') #['h', 'e', 'l', 'l', 'o']
AED= [Ed,AD,list(AD),("Smith",50)]#列表里可以存储其他序列：比如内嵌字符串、列表、元组、字典等
print AED
print [1,2,3] + [4,5,6]#使用加号可以进行序列的连接操作[1, 2, 3, 4, 5, 6]
print [42] * 5 #数字x乘以一个序列会生成新的序列[42,42,42,42,42]
print []#空列表
print  [None] * 10#但是如果想创建一个占用十个元素空间，却不包括任何有用内容的列表，我们就需要一个值来代表空值
#用in检查某个值是否在序列中

#更新列表方法
AED[2] = 'upt' #将下标2的元素更新为”upt“
print AED  #结果：[['Gumby', 42], ('hello', 'world'), 'upt', ('Smith', 50)]
#append()
AED.append('last') #最后插入一行
print AED #[['Gumby', 42], ('hello', 'world'), 'upt', ('Smith', 50), 'last']
#删除列表元素
del AED[2]#删除下标2的元素
print AED #[['Gumby', 42], ('hello', 'world'), 'upt', ('Smith', 50), 'last']
#del AED #删除列表
#访问列表方法
print AED[0] #同字符串，下标从0开始
print AED[::-1] #列表截取，同字符串


#Python列表操作的函数和方法
#列表操作包含以下函数:
print len(AED)
print cmp(AED, list(AD))#比较两个列表的元素  结果：-1
print len(AED)#列表元素个数 结果： 5
print max(AED)#返回列表元素最大值 结果： ('hello', 'world')
print min(AED)#返回列表元素最小值  结果：['Gumby', 42]
print list(('Smith',50))#将元组转换为列表  结果：['Smith', 50]


#列表操作包含以下方法:
AED.append('last') #最后插入一行
print AED
print AED.count('last')#统计某个元素在列表中出现的次数 2
AED.extend(['1','2','3','4'])#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print AED
#注：extend方法和连接操作（+）最主要的区别在于：extend方法修改了被扩展的序列，而连接操作会返回一个全新的列表
print AED.index('last')#从列表中找出某个值第一个匹配项的索引位置 ,当匹配项没有被找到时，会引发一个异常。结果：3
AED.insert(2,'ins') #在下标2的位置插入新元素
print AED # [['Gumby', 42], ('hello', 'world'), 'ins', 'upt', ('Smith', 50), 'last']
print AED.pop(2)#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值，按下标序号进行删除：结果ins
AED.remove('last')#移除列表中某个值的第一个匹配项,如不存在则报错
print AED
AED.reverse()#将列表中的元素反向存放
print AED
AED.sort()#sort方法用于在原位置对列表进行排序，意味着改变原来的列表，而不是简单地返回一个已排序的列表副本
print AED

#列表复制
print id(AED)
y = AED[:] #y=x[:]，分片是一种很有效率的复制整个列表的方法。如果简单地把x赋值给y是没有的（y=x），因为这样做就让x和y指向同一个列表了
print id(y)
#一、标准内建函数：同字符串
#二、序列类型操作符：同字符串
#三、序列类型函数：同字符串
#四、列表类型的内建函数
#4.1、list函数将字符串转成列表
#4.2、改变元素的值
#4.3、分片赋值（第一个参数是开始分片的起始位置，第二个参数是结束分片的下一个位置）
#4.4、添加元素 append 和 extend 
#4.5、删除pop,del,remove
#4.6、插入insert
#4.7、排序L.sort() ； L.reverse()；使用sorted函数(返回一个已排序的副本，不改变原序列)
#4.8、索引index()
#4.9、计数count()
#五、列表特殊强大的功能
print [ i * 2 for i in [8, -2, 5] ] #[16, -4, 10]
print [ i for i in range(8) if i % 2 == 0 ] #[0, 2, 4, 6]
