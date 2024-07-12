import asyncio
import random

async def cook_dish(dish_name):
    cook_time = 1 + random.random()
    print(f"({dish_name}) Cooking : {cook_time} seconds")
    await asyncio.sleep(cook_time)
    print("finish cooking")
    return dish_name, cook_time

async def main():
    tasks = [
        asyncio.create_task(cook_dish("Rice")),
        asyncio.create_task(cook_dish("Noodle")),
        asyncio.create_task(cook_dish("Curry")),
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for task in done:
        first_completed, time_taken = task.result()
        print(f'Completed task: 1\n - {first_completed} is completed in {time_taken:.17f}')

    print("Not Compelete tasks : ",len(pending))
   


asyncio.run(main())
