#we can bind field/function to a class/obj
class Student(object):
    pass

#bind a field to obj but other objs
s = Student()
s.name = 'Tom'
print s.name

#bind a function to obj but other objs
def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(20)
print s.age

#bind a function for all objs,todo doesn't work...
# def set_score(self,score):
#     self.score = score
# Student.set_score = MethodType(set_score,None,Student)
# s2 = Student()
# s2.set_score(80)
# print s.score
# s.set_score(100)
# print s2.score

#limit the field to add using '__slots__'
class Person(object):
    __slots__ = ('name','age')

p = Person()
p.name = 'Person1'
p.age = 12
#next code will be error
#p.job = 'Farmer'

#use '@property' let set/get simply
class Student(object):

    #like a decorator,---getter
    @property
    def score(self):
        return self._score
    #setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 80 #---> call function setter
print s.score # --> call function getter

#some particular function in Python,like '__xxx__' '__init__'
class Student(object):
    # init function,can be treaded as a constructor,self as 'this' and can be ignore when be called
    def __init__(self,name):
        self.name = name

    #this function like 'toString' in Java
    def __str__(self):
        return 'Student object (name:%s)'%(self.name)

    #this function is for deleloper like __str__
    __repr__ = __str__

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    #use in for ... in
    def __iter__(self):
        return self # this obj is a iterator

    def next(self):
        self.a,self.b=self.b,self.a+self.b # calc next number
        if self.a >100: #the condition to break the loop
            raise StopIteration();
        return self.a

    # use like a list ,list[n]
    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a,b = b,a+b
        return a
    # allow call from obj ,like f()
    def __call__(self, *args, **kwargs):
        print 'call from obj'
s = Student('Jerry')
print s
for n in Fib():
    print n
f = Fib()
print f[4]
f()
