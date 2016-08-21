#!/user/bin/env python
#encoding:utf-8


'''
    数学上,，把set称做由不同的元素组成的集合，集合（set）的成员通常被称做集合元素（set elements）。
Python把这个概念引入到它的集合类型对象里。集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键。
数学集合转为Python的集合对象很有效，集合关系测试和union、intersection等操作符在Python里也同样如我们所预想地那样工作。
    和其他容器类型一样，集合支持用in和not in操作符检查成员，由len()内建函数得到集合的基数(大小)， 用 for 循环迭代集合的成员。
    但是因为集合本身是无序的，不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中元素的值。
    集合(sets)有两种不同的类型：可变集合(set)和不可变集合(frozenset)。对可变集合(set)，可以添加和删除元素，
    对不可变集合(frozenset)则不允许这样做。注意：可变集合(set)不是可哈希的，因此既不能用做字典的键也不能做其他集合中的元素。
    不可变集合(frozenset)则正好相反，即它们有哈希值，能被用做字典的键或是作为集合中的一个成员。
'''

# 集合与列表( [ ] )和字典( { } ) 不同，没有特别的语法格式。列表和字典可以分别用他们自己的工厂方法 list() 和 dict() 创建
#这也是集合被创建的唯一方法：用集合的工厂方法set()和frozenset()。
s =  set('cheeseshop')
print s #结果：set(['c', 'e', 'h', 'o', 'p', 's'])
t = frozenset('bookshop')
print t #结果： frozenset(['b', 'h', 'k', 'o', 'p', 's'])

#    
s.add('z') #集合add方法：是把要传入的元素做为一个整个添加到集合中
print s #结果：set(['c', 'e', 'h', 'o', 'p', 's', 'z'])
#t.add('z')，不可变集合不支持add
s.update('pypi')  #集合update方法：是把要传入的元素拆分，做为个体传入到集合中
print s  #结果：set(['c', 'e', 'i', 'h', 'o', 'p', 's', 'y', 'z'])
s.remove('z')
print s #结果： set(['c', 'e', 'i', 'h', 'o', 'p', 's', 'y'])
s -= set('pypi')
print s #结果：set(['c', 'e', 'h', 'o', 's'])

#删除集合
#del s

#成员关系（in ； not in）
print 'k' in s #False
print 'c' not in t  #True

#集合等价，不等价
print s == t #False
print s != t  #True
print set('posh') == set('shop')  #True

print len(s) #结果：5

#遍历访问集合中的值
for i in s:
    print i
