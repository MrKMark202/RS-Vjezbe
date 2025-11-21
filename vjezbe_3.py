'''
import asyncio

async def timer(sec: int):
    print("Zapocinjem")
    await asyncio.sleep(sec)
    print(f"Zavrsavam za {sec}")
    return "123"


async def main():
    #timer_cor_1 = timer(1)
    #timer_cor_2 = timer(2)
    #timer_cor_3 = timer(3)
    #task_1 = asyncio.create_task(timer_cor_1) #schedule
    #task_2 = asyncio.create_task(timer_cor_2) #schedule
    #task_3 = asyncio.create_task(timer_cor_3) #schedule


    lista_korutina = [asyncio.create_task(timer(n) for n in range(1,6))]

    rezultat = await asyncio.gather(*lista_korutina) #schedule and run
    print(rezultat)

#event loop
asyncio.run(main())
'''


import requests

rezultat = requests.get("http://www.google.com")

print(rezultat.text)