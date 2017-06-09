#!/usr/bin/env python
# -*- coding: utf-8 -*-
print u'中文'

#格式化字符串 %s + %
print 'Hello, %s' %('World')

#常用的占位符
# %d 整数
# %f 浮点型
# %s 字符串
# %x 十六进制整数

# 整数和浮点数可以指定是否补0和整数与小数的位数
print '%2d-%02d' % (3,2)
print '%.4f' % 3.141592657

# %s 会把任意类型转换为字符串
print 'Age:%s,Gender:%s' % (25,True)

# 使用Unicode时，最好保证替换的字符串也是Unicode
print u'Hi,%s,%s' % (u'小明',u'Tom')

# 使用%转义
print 'growth rate:%d %%' % 7
