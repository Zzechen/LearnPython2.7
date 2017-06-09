# a Student class who extends Object
class Student(object):
    # a field for class,like a field modified by 'static' in Java
    state = 'healthy'
    #a method for class,like a method modified by 'static' in Java,but it must be modified by @classmethod in Python
    @classmethod
    def healthy_state(cls):
        print cls.state

    # like a constructor,self like 'this' in Java,but can be ignore when call
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__age=age
    def print_msg(self):
        print 'name:%s --- age:%s' % (self.name,self.age)

    def __privat(self):
        print 'this is a private method'

    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0 and age <100:
            self.__age = age
        else:
            self.__age =0
# create a object for Student
s = Student('xiaoming',20)
print 'name:%s\nage:%s' % (s.name,s.age)
s.print_msg()

# add field for the object but not all object for Student
s.gender = 1
print 'name:%s -- gender:%s' % (s.name,s.gender)

#call a class field
print s.state
# or
print Student.state

#call a class method
Student.healthy_state()

# add a class field,and is available for all Student's obj
Student.height = 170
print s.height

# when the obj'field is same with class'field,obj' field is preferential
s2 = Student('daming',15)
s.state = 14
print 's.state',s.state
print 's2.state',s2.state
print 'Student.state',Student.state

# a private field or method is named begin with '__',and next code is error
# s.__private
# print s.__age

# can use set_xx/get_xx methods
s.set_age(10)
print s.get_age()

# note.txt:

