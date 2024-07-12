# example of waiting for all tasks to be completed with a timeout
# example of waiting for the first task to complete
# example of waiting for all tasks to complete
from random import random
import asyncio

async def task_coro(arg):
    value = random() * 10
    await asyncio.sleep(value)
    print(f'>task {arg} done with {value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    done, pending = await asyncio.wait(tasks, timeout=5)
    print(f'Done, {len(done)} tasks completed in time')
   


asyncio.run(main())
