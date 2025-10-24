a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))

if a == 0: 
    if b == 0:
        print("Nieskończenie wiele rozwiązań")
    else:
        print ("Brak rozwiązań, równanie sprzeczne")
else: 
    x = - b / a        
    print("Rozwiązanie równania x  = ",x,)
