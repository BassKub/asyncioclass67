# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    start = time.perf_counter()
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    elapsed2 = time.perf_counter() - start
    return elapsed2
    
    
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
    
 
 
# entry point coroutine
async def main():
    start = time.perf_counter()
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    pt = await asyncio.gather(producer(queue), consumer(queue))
    elapsed = time.perf_counter() - start
    print(f"{time.ctime()} -Producer Done in", pt[0], "seconds.")
    print(f"{time.ctime()} -Done in", elapsed, "seconds.")
 
# start the asyncio program
asyncio.run(main())