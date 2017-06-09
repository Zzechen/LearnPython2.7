# -*- coding:utf-8 -*-

# dict: 字典，以key-value的形式存储，使用 {} 声明,对应的key是唯一的,内部存放无序
scores = {'A':80,'B':90,'C':100}
print scores

# 替换value
scores['A'] = 88
# 获取对应的value
print scores['A']
print scores.get('A')

# 添加
scores['D'] = 120
print scores
# 移除
scores.pop('A')
print scores

# 遍历
for key in scores:
    print 'key:%s -- value:%s ' % (key,scores[key])
#和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。


# set:无序，不重复的集合，使用 set([x,x])形式声明
s = set([1,2,3])
print s

# 添加
s.add(4)
s.add(3) # 自动过滤已存在元素
print s
# 删除
s.remove(4)
print s
# 交集
s2 = set([3,4,5])
print s & s2
# 并集
print s | s2