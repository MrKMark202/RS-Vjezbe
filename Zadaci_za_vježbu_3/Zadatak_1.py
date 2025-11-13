# Kvadriranje

kvadriraj = lambda x : x** 2
print(kvadriraj(5))

# Zbroji pa kvadiraj

zbroji_pa_kvadriraj = lambda a,b : (a+b) ** 2
print(zbroji_pa_kvadriraj(3,5))

# Kvadriraj duljinu niza

lista_brojeva = [1, 2, 5, 7, 12]
kvadriraj = list(map(lambda x : x ** 2, lista_brojeva))
print(kvadriraj)

# Pomnoži vrijednost s 5 pa potenciraj na x

pomnozi_pa_potenciraj = lambda x, y : (y * 5) ** x
print(pomnozi_pa_potenciraj(2,4))

# Vrati True ako je broj paran, inače vrati None

paran_broj = lambda x : x%2==0
print(paran_broj(3))