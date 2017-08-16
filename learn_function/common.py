# some common functions to cast obj
print int('124')
print int(12.33)
print float('23.1234565789')
print str(12335)
print unicode(100)
print bool(1)
print bool(0)

# function is a obj too,and can be assign to a obj,like this
a = abs
print a(-123)

#define a function by use 'def',like
def add(a,b):
    return a+b
print add(1,2)

#you can use 'pass' define a none function,like
def nothing():
    pass

#in python,function can return multiple value,in fact it returns a tuple
def add_avg(a,b):
    return a+b,(a+b)/2

print add_avg(3,4)
x,y = add_avg(4,6)
print x,y

#any functions will hava a result,if there is no 'return' in function ,it will be return 'None'
print nothing()

#set default value for same params,and you can ignore this param when call
def split(s,len=1):
    return s[0:len]
print split('add')
print split('addd',2)
print split('abcdef',len=4)

#a problem in default value,like
def add_end(L=[]):
    L.append('End')
    return L
#when you call it twice,the problem is appear
print add_end()
print add_end()
#reason:when defining the function,the default value L is calculate,that is [],which is a obj and L is related to this obj,so the obj is changed
#so when you use the default value,that the value must be a can't changed obj

# changed params is supported in Python and use the symbol '*',like arg.. in Java
def calc(*numbers):
    sum=0
    for number in numbers:
        sum = sum+number
    print 'the result is',sum
calc()
calc(1,2,3,4,5)
# in fact,the params will be packaged a tuple
# can use a tuple or list directly,but need to add '*'
nums=[1,2,3]
calc(*nums)

# there is supported key-params,use '**kw' define
def person(name,age,**kw):
    print 'name:',name,'age:',age,kw

d = {'city':'Beijing','job':'Engineer'}
person('Bob',20,**d)

# a complex function in params
def func(a,b,c=0,*args,**kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
#you can call this like
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

# even,you can call like
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

# so ,for any method you can call it through xxx(*args,**kw)

# recursion
def fact(n):
    if n ==1 :
        return 1
    else:
        return n*fact(n-1)

print fact(5)
# the process of the calc is
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120