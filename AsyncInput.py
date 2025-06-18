import asyncio

async def get_input(prompt):
    loop = asyncio.get_event_loop()
    # await loop.run_in_executor(None, input, prompt)
    return await loop.run_in_executor(None, input, prompt)

0
