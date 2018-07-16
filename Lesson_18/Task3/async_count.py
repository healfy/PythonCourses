import asyncio
from datetime import datetime


async def count(number):
    print(number ** (10 ** 6))


start_time = datetime.now()

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(count(6)),
    loop.create_task(count(7)),
    loop.create_task(count(8)),
    loop.create_task(count(9)),

]
loop.run_until_complete(asyncio.wait(tasks))

loop.close()

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))
