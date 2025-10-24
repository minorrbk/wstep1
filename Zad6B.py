import random

cena = float(input("Podaj cene za litr paliwa: "))
spalanie = float(input("Podaj spalanie na 100km: "))
los = random.randint(1, 1000)

print("Wylosowany dystans: ",los,)

zużyciepaliwa = los * spalanie / 100 
cenapaliwa = los * spalanie * cena / 100
print (f"Zużycie paliwa wynosi:",round (zużyciepaliwa, 2),"litrów")
print (f"Cena paliwa wynosi:",round (cenapaliwa, 2),"PLN")