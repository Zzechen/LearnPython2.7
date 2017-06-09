# higher-order function,a function can be received a function as a param
def add(x,y,f):
    return f(x)+f(y)
print add(2,-5,abs)

# map : calc all element in list to f,and receive the result
# define the standar for calc all ths elements in list
def f(x):
    return x*x
print map(f,[1,2,3,4,5,6])

#reduce:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# define a result of calc for all the elements in list
def fn(x,y):
    return x*10+y
print reduce(fn,[1,2,3,4,5])

#filter:
def is_2(n):
    return n%2==0
print filter(is_2,[1,2,3,4,5])

#sorted:
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# return a function
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,2,3,4,5)
print f
print f()

#closure
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(),f2(),f3()

#lambda,only has one expression and can't use 'return'
print map(lambda x:x*x,[1,2,3,4,5])

#decorator
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2013-12-25'
now()

#partial function
#int('1234',base = 2)
# -->
# def int2(x,base=2):
#     return int(x,base)
import functools
int2 = functools.partial(int,base=2)
print int2('100001')
