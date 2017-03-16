import sys, time, os, threading
from parse import *

'''
class scheduler is incharge of printing to the screen and maintaining a string buffer
we launch Threads to keep the track of time for each of the keys (of format [startTime, EndTime, content])
using subThreadRoutine function such that it changes the buffer's state.
the check of program termination is the thread count is 1  
'''
class scheduler :
    def __init__(self):
        self.buffer = []
    
    def update(self, key):
        self.buffer.append(key)
        self.blit()

    def blit(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for key in self.buffer:
            print key
    
    def expire(self, key):
        self.buffer.remove(key)
        self.blit()

def subThreadRoutine(key):
    
    global Subs_devil
    while (key[0] > time.clock()):
        pass
    print time.clock()
    os.system('cls' if os.name == 'nt' else 'clear')
    Subs_devil.update(key[2])

    while (key[1] > time.clock()):
        pass
    Subs_devil.expire(key[2])

try:
    file = open(sys.argv[len(sys.argv) - 1], 'r')
    parsed = parse(file.readlines(),1)
    file.close()
    global Subs_devil
    Subs_devil = scheduler() 
    time.clock()
    print '<start>'

    for key in parsed :
        threading.Thread(target=subThreadRoutine,args=(key,)).start()
    
    while(threading.activeCount() > 1):
        pass
    
    print "<end>"

        
except:
    print ("an unknown error occured")