import time
import asyncio


async def korutina1(parametar):
    print("Zapocinjem dohvat korisnika")
    korisnici = ["Marko", "Mirko", "Martin"]
    await asyncio.sleep(parametar)
    print("Korisnici dohvaceni")
    return print(korisnici)

async def korutina2(parametar):
    print("Zapocinjem dohvat proizvoda")
    proizvodi = ["Graficka", "Maticna", "Napajanje"]
    await asyncio.sleep(parametar)
    print("Proizvodi dohvaceni")
    return print(proizvodi)

async def main():
    print("Pocinjem main")
    kor1 = asyncio.gather(korutina1(3))
    kor2 = asyncio.gather(korutina2(5))
    korisnici = await kor1
    proizvodi = await kor2
    print("Zavrsavam  funkciju... ")
    return korisnici, proizvodi

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja je: {round(t2 - t1, 2)} sekundi")