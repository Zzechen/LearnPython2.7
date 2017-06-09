# -*- coding:utf-8 -*-

# list:一种有序的集合,使用 [] 声明
# 创建一个list
classmates = ['A','B','C']
print classmates

# 获取长度
print len(classmates)

# 根据下标获取元素 正向从0开始
print classmates[1]
# 使用负数获取倒数第几个，反向从-1开始
print classmates[-1]

# 遍历
for item in classmates:
    print item

# 追加
classmates.append('D')
print len(classmates)

# 插入
classmates.insert(1,'Tom')
print classmates

# 删除
classmates.pop(1)
print classmates

# 替换
classmates[1] = 'Tom'
print classmates

# 可以存储不同类型的元素
list = [1,'a',0.1,100L]
print list


# tuple:不可变的list，包括长度和元素，使用 () 声明。
# 可以将元素指定为list，从而达到变相可变
t = (1,2)
print t

# 当定义一个元素时，需要这样.
t = (1,)
print t
# 因为 () 既可以表示tuple，有可以表示数学公式中的小括号，由于歧义的存在，所以1个元素的tuple定义是需要多加个','

# 实现一个”可变“的tuple
t = (1,2,[2,3,4])
print  t[2]
t[2].append(5)
print t