# dist(), list(), tuple(), set()

lista = [1, False, "123", [1,2, 3, "123"], 4.0]

print (lista)

# enumerate
#for index, value in enumerate(lista):if index == -1:for element in value:



#for broj in range(1, 101, 2):
    #print(broj)



# lista vs tuple

lista = [1, 2, 3, 4, 5]
tapl = (1, 2, 3, 4, 5)

lista_2 = list(tapl)
#print(tapl)
#print(lista_2)


osoba = {
    "ime": "Marko",
    "prezime": "Marić",
    2 : "Pero",
    (1, 2, 3, 4) : False
}

print(osoba[2])


#for kljuc, vrijednost in osoba.items():
#    print(f"Kljuc {kljuc} : {vrijednost}")



# set

skup = {1,2,3,4,5}

skup_iz_liste = tuple(set(lista))

def kvadriraj (x):
    return x ** 2

#lambda arguments : expression
    #lambda x : x ** 2


def primijeni_na_sve(lista: list, funkcija:callable):
    
    nova_lista = []
    for element in lista:
        nova_Vrijednost = funkcija(element)
        nova_lista.append(nova_Vrijednost)
    return nova_lista

#lista = [1,2,3,4,5]

#print(primijeni_na_sve((lista, lambda x : x ** 2)))


lista_imena = ["Marko", "Mirko", "Ivan"]

#map(funckija, iterables)

print(list(map(lambda ime : len(ime),lista_imena)))


# filter funkcija - vraća reduciranu iterable/kolekciju
# Sintaksa
# filter(function, iterablers)

lista_brojeva = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x : x%2==0, lista_brojeva)))


#studenti = []
#    {"ime" : "Marko", "godina_rodenja": 2002},
 #   {"ime" : "Mirko", "godina_rodenja": 1999}
#]

#filter(list(filter(lambda x : x["godina_rodenja"]<2001, studenti)))


lista_brojeva = [2, 4, 12, 24, 44, 65+1]

print(all(map(lambda broj : broj%2==0, lista_brojeva)))