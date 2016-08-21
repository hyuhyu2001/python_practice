#!/user/bin/env python
#encoding:utf-8

'''
字典是另一种可变容器模型，且可存储任意类型对象。
典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示
d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''
#创建字典
#1、空字典
d1 = {} 
D2={'name':{'first':'diege','last':'wang'},'age':18} #字典可以嵌套字典、元组、列表等
print D2['name']    #结果：{'last': 'wang', 'first': 'diege'} 
print D2['name'] ['last'] #嵌套中的子查询结果：wang

#2、直接创建，适合事先拼凑整个字典
dict1 = {
    'name':'jacky',
    'age':'29',
    'job':'Engineer'
}

#3、dict()方法 ；dict([(’key1','value1'),(key2','value2')]) ；适合需要在程序运行时把键和值逐步建成序列
print dict([('name','gumby'),('age','42')]) #dict()转化 {'age': '42', 'name': 'gumby'}

#4、dict()方法，dict(key1='value1',key2='value2')；直接用key=value赋值注意这里name,age没有 ’‘括起来，因为这里是变量。
#一次动态地建立字典的一个字段；适合关键字形式所需的代码比常量少，【但是键必须是都是字符串才可行】
dict3 = dict(name='kelly',age=19)
print dict3  #结果：{'age': 19, 'name': 'kelly'}
 
#5、zip转换序列；dict(zip(keyslist,valslist))；zip函数把程序运行动态获得的键和值列表合并在一起（例如分析数据文件字段）
keyslist=['shell','sql']
valslist=[['s1','k1','all'],['s1','k1','all']]
d = zip(keyslist,valslist) 
print d  #结果：[('shell', ['s1', 'k1', 'all']), ('sql', ['s1', 'k1', 'all'])]
dict4 = dict(zip(keyslist,valslist)) 
print dict4 #结果：{'shell': ['s1', 'k1', 'all'], 'sql': ['s1', 'k1', 'all']}

#6、fromkeys()
#dict.fromkeys(seq,val=None)    创建并返回一个新字典，以seq中的元素做该字典的键的列表，val 做该字典中所有键对应的初始值(如果不提供此值，则默认为None)
#dict.fromkeys 可以从一个列表读取字典的key 值默认为空，可指定初始值.两个参数一个是KEY列表，一个初始值
#适合：如果所有键的值都相同，可以使用特殊形式对字典进行初始化。简单传入一个键列表，以及所有键的初始值（默认为空
print dict.fromkeys(['a','b','c'],0) #结果：{'a': 0, 'c': 0, 'b': 0}
print dict.fromkeys(['name','age'])  #结果：{'age': None, 'name': None}

#一、基本字典操作
print len(dict1) #返回字典中项（键-值对）的数量 结果：3
print list(dict1)  #获取这个字典的的KEY作为一个列表，结果：['job', 'age', 'name']
print dict1['name'] #返回关联到键name上的值，结果jacky
dict1['name'] = 'king' #更新键name对应的value的值，结果：king
print dict1['name']  
print ('name' in dict1) #判断键name是否在字典中，结果：True  
#表达式k in d（d为字典）查找的是键，而不是值。表达式v in l（l为列表）则用来查找值，而不是索引
del dict1['name'] #删除键name的值
print dict1  #结果：{'job': 'Engineer', 'age': '29'}


#二、字典方法
#2.1、clear()方法清除字典中所有的项，这是个原地操作，所以无返回值
#dict1.clear()
#print dict1 #结果：{}

#2.2、copy():返回一个具有相同键-值对的新字典（这个方法实现的是浅拷贝）
dict2 = dict1.copy()
print dict2
print id(dict1)  #41599168
print id(dict2)  #41097952

#2.3、fromkeys()方法使用给定的键建立新的字典，每个键默认对应的值为None
print {}.fromkeys(['name','age']) #结果：   {'age': None, 'name': None}
print {}.fromkeys('name','age') #结果：{'a': 'age', 'e': 'age', 'm': 'age', 'n': 'age'}

#2.4、get()方法 更宽松的访问字典项的方法。一般而言，如果不用get，如果试图访问字典中不存在的项时就会出错
print dict1.get('name')  #key中不存在name，结果：None
print dict1.get('job')   #结果：Engineer

#2.5、has_key()方法 可以检测字典中的某个键是否给出值，表达式d.has_key(k)相当于表达式k in d
print dict1.has_key('name') #结果：False
print dict1.has_key('job') #结果：True

#2.6、items()和iteritems()
#items方法将所有的字典项以列表的方式返回，这些列表项中的每一项都来自于（键，值），但是项在返回时并没有特殊的顺序
print dict1.items()  #结果：[('job', 'Engineer'), ('age', '29')]
#iteritems方法的作用大致相同，但是会返回一个迭代器对象而不是列表：
print dict1.iteritems()   #结果：<dictionary-itemiterator object at 0x023E5480>
print list(dict1.iteritems())#通过list转换后，结果：[('job', 'Engineer'), ('age', '29')]

#2.7、values和itervalues
#values方法以列表的形式返回字典中的值（itervalues返回值的迭代器），与返回键的列表不同的是，返回值的列表中可以包含重复的元素：
print dict1.values()  #结果：['Engineer', 45, 'king']
print dict1.itervalues()   #结果<dictionary-valueiterator object at 0x02765480>

#2.8、pop()方法用来获得对应于给定键的值，然后将这个键-值对从字典中移除,并返回值的结果
#print dict1.pop('age') #结果29
#print dict1

#2.9、popitem()方法类似于list.pop(),pop()会弹出列表删除的元素，而popitem()是弹出随机的项
#dict1.popitem()  #随机返回并删除字典中的一对键和值（项）。为什么是随机删除呢？因为字典是无序的，没有所谓的“最后一项”或是其它顺序。在工作时如果遇到需要逐一删除项的工作，用popitem()方法效率很高。
#print dict1

#2.10、setdefault()方法在某种程度上类似于get方法，除此之外，setdefault还能在字典中不含有给定键的情况下设定相应的键值，给定默认值，如果有值则不更新
dict1.setdefault('name','king')
dict1.setdefault('age',39)
print dict1  #结果{'job': 'Engineer', 'age': '29', 'name': 'king'}

#2.11、update()方法可以利用一个字典项更新另一个字典项；
#D2.update(D1)    方法：合并。D1合并到D2,D1没有变化，D2变化。注意和字符串、列表的合并操作”+“不同
#dict2有多个键时如何更新？
dict2 = {'age':45}
dict1.update(dict2)
print dict1#结果： {'job': 'Engineer', 'age': 45, 'name': 'king'}


