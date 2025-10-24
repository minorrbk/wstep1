#ZAD 6 A)

cena = 6.5
dystans = float(input("Podaj dystant: "))
spalanie = float(input("Podaj spalanie na 100km: "))

zużyciepaliwa = dystans * spalanie / 100 
cenapaliwa = dystans * spalanie * cena / 100
print ("Zużycie paliwa wynosi: ",zużyciepaliwa, "litrów")
print ("Cena paliwa wynosi: ",cenapaliwa, "PLN)")