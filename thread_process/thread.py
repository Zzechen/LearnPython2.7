#Thread in Python is real Posix Thread and not be mocked
#thread:a base module
#threading:a advanced module,packaging for thread module

#create a new Thread,delivery a function and create the Thread,start the thread through start()
import time,threading

#the new thread execting
def loop():
    print 'thread %s is running ...' %threading.current_thread().name
    n=0
    while n<5:
        n+=1
        print 'thread %s >>> %s'%(threading.current_thread().name,n)
        time.sleep(1)
    print 'thread %s ended.'%threading.current_thread().name

print 'thread %s is running...' %threading.current_thread().name
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended' % threading.current_thread().name


#multiple thread
#will be a problem such as Java-- Thread Safety
import time, threading

# a share value
balance = 0

def change_it(n):
    # reduce and add ,result should be 0,but...
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance

# the result must be not 0,because chage_it is not a atom exection
# from example, balance = balance +n can be treated as
# x = balance +n
# balance = x
# and x is a local field,every thread has their own x,so the result is not 0
# now we use a Lock,and not allow change_it be interrupted
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # get a lock
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

#