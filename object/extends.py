class Animal(object):
    def __init__(self,name):
        self.name = name
    def run(self):
        print 'Animal is running...'

#class Dog extends Animal
class Suckler(Animal):
    #override __init__
    def __init__(self,name):
        # call parent __init__ method
        Animal.__init__(self,name)

    # override run
    def run(self):
        print 'Suckler %s is running...'%(self.name)
    pass

class Dog(Suckler):
    def __init__(self,name):
        Suckler.__init__(self,name)

    def run(self):
        print "Dog %s is running..."%(self.name)

dog = Dog('2ha')
dog.run()

# Python allow multiple extends
class Fly(object):
    def __init__(self,fly):
        self.fly = fly
    def canfly(self):
        print "I %s fly" % ('can'if self.fly else'can not')

    def fly(self):
        print "I %s fly" % ('can'if self.fly else'can not')

class Cat(Fly,Animal):
    def __init__(self,name,fly):
        Fly.__init__(self,fly)
        Animal.__init__(self,name)

cat = Cat('tom',False)
cat.canfly()
cat.run()
#note.txt field'name is same as a method'name is error when call,now I can't solve it,like this
#cat.fly()

# judge type use isinstance() like this
print isinstance(cat,Cat)
print isinstance(cat,Animal)

# advance type,use types module
import types
print 'add is instance of String type:',type('add') == types.StringType
print type(cat)

#get all fields for a obj -- dir() ,include all __xxx__ particular methods,like __len__
print dir(cat)

# get or set obj' fields use getattr()/setattr()
setattr(cat,'name','Jerry')
print getattr(cat,'name')



