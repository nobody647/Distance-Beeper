import asyncio
import random

bleh = 0

async def myCouroutine(id):
	global bleh
	time = random.randint(1, 5)

	await asyncio.sleep(time)
	bleh += 1
	print("I ({}) just got my data after {} seconds. Bleh is {}".format(id, time, bleh))




async def main():
	tasks = []

	for i in range (10):
		tasks.append(asyncio.ensure_future(myCouroutine(i)))

	await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()

loop.run_until_complete(main())
loop.close()
