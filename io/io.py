# open a file,as 'r'--'readable','w'--'writeable','a'--'append'
#'w'--- if file not exist, auto create the file
#'a'--- write content append orgin file
f = open('txt.txt','w')
f.write('dddd')

#with -- to auto close io
with open('txt.txt','r') as f:
    print f.read()

#try-catch
try:
    with open('test.txt','r') as f:
        print f.read()
except Exception,e:
    print e

#'rb' read binary file,like music,video,picture..
with open('images.jpg','rb') as f:
    print f.readline()

#open a not ASCII file,first open in binary and then encoded
with open('test.txt','rb') as f:
    u = f.read().decode('gbk')
    # u= f.read()
    print u

# can assign the coding mode when create a file through codecs
import codecs
with codecs.open('test.txt','r','gbk') as f:
    print f.readline()

# create/remove/rename a dir
import os
# os.mkdir('test')
# os.rmdir('test')
# os.rename('test','Test')

#get all files in dir
for f in os.listdir('.'):
    print f.lower()
print filter(lambda f:f.lower().endswith('.py'),os.listdir('.'))


#serialization cPickle and pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
print d


#json
import json
print json.dumps(d)
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

#json to obj/obj to json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return 'Student name:%s,age:%s,score:%s'%(self.name,self.age,self.score)

# obj to json: 1.delivery a function for transforming a str to a obj
def student2dict(std):
    return {'name':std.name,
            'age':std.age,
            'score':std.score}
s = Student('Bob',22,80)
print json.dumps(s,default=student2dict)

#obj to json:2 lambda+__dict__
print json.dumps(s,default=lambda obj:obj.__dict__)

#json to obj
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str, object_hook=dict2student)


