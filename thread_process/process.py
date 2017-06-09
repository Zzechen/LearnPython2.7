# in Linux/Unix,create a new process(Mac belong in Unix)
#and next codes doesn't work in Windows
# import os
# print 'Process(%s) start ...' % os.getpid()
# pid = os.fork()
# if pid ==0:
#     print 'I\'m child process (%s) and my parent is %s'%(os.getpid(),os.getppid())
# else:
#     print 'I(%s) just created a child process (%s).'%(os.getpid(),pid)

#in Windows,use Process in multiprocessing
from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s) ...'%(name,os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' %os.getpid()
    p = Process(target=run_proc,args=('test',))
    print 'Process will start.'
    p.start()
    p.join() # wait for the end of the child process,and do next,used to sync in processes
    print 'Process end.'

#use Pool manage several child processes
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print 'Run task %s (%s) ...' %(name,os.getpid())
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name,(end - start))

if __name__ =='__main__':
    print 'Parent process %s.'%os.getpid()
    p = Pool()
    for i in range(9):# system run the number of task is deponded on the number of CPU
        p.apply_async(long_time_task,args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'


# conmunicate in process:Queue,Pipe
#this is a sample using Queue
from multiprocessing import Process,Queue
import os,time,random
#write data
def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue...' %value
        q.put(value)
        time.sleep(random.random())

#read data
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.'%value

if __name__ == '__main__':
    #parent process create the Queue,and send to child processes
    q = Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #start child process--pw,write data
    pw.start()
    #start child process--pr,read data
    pr.start()
    #wait for the end of pw
    pw.join()
    #there is a loop,need manual stop it
    pr.terminate()
