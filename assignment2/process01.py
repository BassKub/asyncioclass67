# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time 

def cooking(index):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index} : Cooking done!')


def kitchen(index):
    cooking(index)


if __name__=="__main__":
    print(f'{ctime()} Main : Start Cooking...PID {os.getpid()}')
    start_time = time()


    kitchens = list()
    for index in range(100):
        p = multiprocessing.Process(target=kitchen, args=(index, ))
        kitchens.append(p)
        p.start()

    for index, p in enumerate(kitchens):
        p.join()

    duration = time() - start_time
    print(f"{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds")