#!/user/bin/env python
#encoding:utf-8


#1、while循环：
while True:
    print '1'
    if  1==1:
        break  #跳出所在的循环，跳出整个循环语句
    if  1>1:
        continue #跳出最近所在循环的的开头处
    if 1<1:
        pass#什么也不做，只是空占位语句
else:#else，只有当循环正常离开时才会执行（也就是没有碰到break语句）
    print '2'
    
#2、for循环：for循环是通用的序列迭代器，可以遍历任何有序的序列对象内的元素。for语句可用于字符串、列表、元组、其他内置可迭代对象以及之后我们能够通过类所创建的新对象。
#for循环的首行定义了一个赋值目标，以及你想遍历的对象，首行后面是你想重复的语句
#当python运行for循环时，会逐个将序列元素中的元素赋值给目标，然后每个元素执行循环主体
#for支持多层嵌套
for i in range(10):
    print '1'
    if i==1:
        break
    if i==2:
        continue
else:
    print '2'
    
#3、三元表达式 
a,x,y,z=1,2,3,4
a=y if x else z  #只有x为真时才会执行表达式y，而只有当x为假时，才会执行表达式z

#4、迭代器
#for循环可以用在任何【可迭代的对象】。这些迭代工具包含了for循环、列表解析、in成员关系测试、以及map内置函数等
#4.1、文件迭代：next()文件迭代方法，无需将文件读取。逐行读取文本的最佳方法就是根本不要去读取，其替代的方法就是、让for循环在每轮自动调用next从而前进到下一行
for line in open('/etc/rc.conf'):
    print line.upper(),
#4.2、字典迭代：
D = {'1':'a','2':'b'}
for key in D: 
    print key,D[key]
#4.3、列表解析
[line.upper() for line in open('/etc/rc.conf')]
#4.4、in成员关系
#map内置函数以及其他内置工具（如sorted,sum）
map(str.upper,open('/etc/rc.conf'))
sorted(open('/etc/rc.conf')) 
sum([3,5,6,9]) #sum调用会计算任何可迭代对象内所有数字的和
#list和tuple内置函数（从可迭代对象创建新的对象），字符串join方法（在可迭代对象内字符串之间放入子字符串），以及序列赋值语句等
list(open('/etc/rc.conf'))
tuple(open('/etc/rc.conf'))
'&&'.join(open('/etc/rc.conf'))
a,d,c,d=open('/etc/rc.conf') 

#5、编写循环的技巧
#遍历序列时，首选for循环，for循环包括多数计数器式的循环，for比while容易写，执行时也比较快。
#5.1、python提供了两个内置函数，在for循环内定制迭代。内置range函数返回连续整数列表，可作为for中的索引。
range(5,10,2)  [5, 7, 9]
range(5,-5,-1) [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
#尽量使用简单的for循环，不要用while，并且不要在for循环中不要使用range调用，只将其作为最后的选择，更简单的办法总是更好。
for i in X:
    print i
for x in S[::2]:print x# 步长2的

#5.2、内置zip函数返回并行的元素元组的列表，可用于在for中遍历数个序列
#并行遍历：zip 和map
L1=[1,2,3,4]
L2=[5,6,7,8]
zip(L1,L2)
[(1, 5), (2, 6), (3, 7), (4, 8)]
for (x,y) in zip(L1,L2):
    print x,y,'--',x+y

#当参数长度不同时，zip会以最短序列的长度为准来截断所得到的元组：
#内置map函数，用类似的方式把序列的元素配对起来，但是如果参数长度，不同则会为较短的序列用None补齐。
map(None,S1,S2) 
[('A', 'x'), ('B', 'y'), ('C', 'z'), (None, '1'), (None, '2'), (None, '3')]

#5.3、使用zip构造字典
keys=['name','age','class']
vals=['diege',18,2012] 
dict(zip(keys,vals))
{'age': 18, 'name': 'diege', 'class': 2012}
D5=dict(zip(keys,vals))

#5.4、使用enumerate内置函数，同时产生下标序列和元素；
S='diege'
for (offset,item) in enumerate(S):
    print item,offset
#这个方法有个next方法，每次遍历列表时，会返回一个(index,value)的元组，而我们能在for中通过元组赋值运算将其分解
E=enumerate(S)
E.next()
(0, 'd')

#6、列表解析
#列表解析是写在方括号中的，因为它毕竟是一种创建新的列表的方式
#[【表达式】 for x in L【for循环行首】]
#列表解析
L=[1,2,3,4,5]
L=[x+10 for x in L]
#将列表中行的换行符去掉
lines=[line.rstrip() for line in open('/etc/rc.conf')]
lines=[line.rstrip() for line in lines]
#扩展列表解析，重复上一个例子，但我们只需开头不为#的文字行
lines=[line.rstrip() for line in open('/etc/rc.conf') if line[0]!='#']
#完整的语句可接纳任意数目的for分句，而每个分区都可以结合一个可选的if分句
[x+y for x in 'abc' for y in 'lmn']
['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
#对一个字符串中的每个x,以及另一个字符串中的每个y,创建x+y合并的列表。收集两个字符串字符的排列组合

