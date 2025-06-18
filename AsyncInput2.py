import asyncio

async def get_input():
    return input("Please enter something: ")

async def main():
    input_future = asyncio.ensure_future(get_input())
    other_task = asyncio.ensure_future(some_other_task())

    done, pending = await asyncio.wait(
        [input_future, other_task],
        return_when=asyncio.FIRST_COMPLETED
    )

    if input_future in done:
        print(f"You entered: {input_future.result()}")
    else:
        print("You didn't enter anything, but other tasks completed.")

async def some_other_task():
    await asyncio.sleep(2)
    print("Some other task completed.")

# Depending on your Python version and environment, you might run this event loop differently.
asyncio.run(main())