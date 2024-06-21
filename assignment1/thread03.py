# extending the Thread class
# running a function in another thread
from time import sleep, ctime
from threading import Thread

class CustomThread(Thread):
    def run(self):
        sleep(1)
        print(f'{ctime()} This is from another thread')

thread = CustomThread()

thread.start()

print(f'{ctime()} Waiting for the thread to finish')
thread.join()