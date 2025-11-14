import asyncio
import time

'''
def korutina ():
    print("nesto")
    time.sleep(3)
    print("jos nesto")
    return "nesto trece"

asyncio.run(korutina())



async def korutina(param : int):
    print(f"Korutina pozvana ... {param}")
    return param

async def main():
    await korutina(3)

asyncio.run(main())
'''

'''
def fetch_data(parametar):
    print(f"Delam nesto sa {parametar}")
    time.sleep(parametar)
    print("Zavrsavam funkciju...")
    return f"fetch_data rezultat: {parametar}"

def main():
    print("Izvrsavam main funckiju")
    rezultat_1 = fetch_data(3)
    rezultat_2 = fetch_data(2)
    print("Zavrsavam funckiju...")
    return rezultat_1, rezultat_2

t1 = time.perf_counter()
main()
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja je: {round(t2 - t1, 2)}sekundi")
'''


async def fetch_data(parametar):
    print(f"Delam nesto sa {parametar}")
    await asyncio.sleep(parametar)
    print("Zavrsavam fetch_data funkciju...")
    return f"fetch_data rezultat: {parametar}"

async def main():
    print("Izvrsavam main funckiju")
    task1 = asyncio.create_task(fetch_data(2)) #schedule
    task2 = asyncio.create_task(fetch_data(3)) #schedule
    rezultat_2 = await task2 #run!!!
    rezultat_1 = await task1
    print("Zavrsavam main funckiju...")
    return rezultat_1, rezultat_2 #Tuple str1, str2

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja je: {round(t2 - t1, 2)}sekundi")