import asyncio
from aioconsole import ainput

async def gsleep(i:float)->str:
    ui = await ainput("> ")
    return await asyncio.sleep(i,result = ui)


async def main()->None:
    while True:
        print("Выполняем...")
        # user_input = await ainput("> ")
        # print(f"Вы ввели: {user_input}")
        a = await gsleep(1)
        if a.strip().lower() == 'q':break

asyncio.run(main())
input(' :-)> ')
