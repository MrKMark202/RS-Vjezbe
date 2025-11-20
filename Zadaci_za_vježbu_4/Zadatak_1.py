import time

def korutina(parametar):
    time.sleep(parametar)
    lista_brojeva = [x for x in range(1, 11)]
    print("Dohvaceni podaci")
    return print(lista_brojeva)

def main():
    print("Krece funkcija")
    korutina(3)


t1 = time.perf_counter()
main()
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja je: {round(t2 - t1, 2)} sekundi")