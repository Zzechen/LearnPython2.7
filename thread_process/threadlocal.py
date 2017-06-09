# is same as ThreadLocal in Java, used to save variant by thread,a variant is available in thread
import threading

local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' %(local_school.student,threading.current_thread().name)

def process_thread(name):
    # bind a student to Threadlocal
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


# you can understander a ThreadLocal obj is a dict,and the key is a thread obj,but you can't get the value of thread A in thread B
