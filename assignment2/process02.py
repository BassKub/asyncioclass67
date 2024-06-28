# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources
import os
import multiprocessing

from time import sleep, ctime, time

# Basket of sharing
class Basket:
    def __init__(self):
        self.eggs = 50  # Initial number of eggs

    def use_eggs (self, index):
        print(f"({ctime()} Kitchen-{index} : Chef-{index} has lock with eggs remaining {self.eggs}")
        self.eggs -= 1  # Adjust the number of eggs used for cooking
        print(f"{ctime()} Kitchen-{index} : Chef-{index} has released lock with eggs remaining {self.eggs}")

# chef cooking

#chef use eggs for cooking
def cooking (index, basket):   
    basket.use_eggs (index)
    sleep (2)  # Simulate cooking time


#kitchen cooking

def kitchen (index, share_eggs):
    print(f'{ctime()} Kitchen-{index} : Begin Cooking...PID {os.getpid()}')
    cooking(index, share_eggs)
    cooking_time = time()
    duration = time() - cooking_time
    print(f'({ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds!')
    

if __name__=="__main__":

    #Begin of main thread
    print(f'{ctime()} Main : Start Cooking... PID {os.getpid()}')
    start_time = time()

    basket = Basket()

    #Multi processes.
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process (target=kitchen, args=(index, basket))
        kitchens.append(p)

        p.start()

    for index, p in enumerate(kitchens):
        p.join()

    print(f"{ctime()} Main : Basket eggs remaining {basket.eggs}")
    duration= time() - start_time
    print(f"{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds")
