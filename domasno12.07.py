# Задача 1:

def vozrast():
    vozrast = int(input("Vnesete ja vasata vozrast: "))
    if vozrast < 18:
        print("Vie ste maloletno lice")
    else:
        print("Vie ste polnoletno lice")
vozrast()

# Задача 2
def broj():
    broj = int(input("Vnesete broj: "))
    if broj > 0:
        print("Brojot e pozitiven")
    elif broj <0:
        print("Brojot e negativen")
    else:
        print("Brojot e nula")
broj ()

# Задача 3

def zbir_do_n():
    n = int(input("Vnesete broj: "))   
    zbir = 0                         
    for i in range(1, n + 1):          
        zbir += i                     
    print(f"Zbirot na broevite od 1 do {n} e: {zbir}")

zbir_do_n()


# Задача 4

def obraten_tekst():
    tekst = input("Vnesete tekst: ")
    obraten = tekst[::-1] 
    print("Tekstot vo obraten redosled e:", obraten)

obraten_tekst()



# Задача 6

def br_samoglaski():
    recenica = input("Vnesete recenica: ")
    samoglaski = "aeiouAEIOU"
    count = 0
    for bukva in recenica:
        if bukva in samoglaski:
            count += 1
    print(f"Brojot na samoglaski vo recenicata e: {count}")

br_samoglaski()



# Задача 7

def br_bukvi():
    recenica = input("Vnesete recenica: ")
    recenica = recenica.lower()   
    bukvi = {}                   

    for glas in recenica:
        if glas.isalpha():    
            if glas in bukvi:
                bukvi[glas] += 1
            else:
                bukvi[glas] = 1

    print("\nBroj na pojavuvanja na sekoja bukva:")
    for bukva, broj in bukvi.items():
        print(f"{bukva}: {broj}")

br_bukvi()



# Задача 8

def zbir_pozitivni():
    total = 0
    while True:
        broj = int(input("Vnesete broj: "))
        if broj < 0:  
            break
        total += broj 
    print("Zbirot na pozitivnite broevi e:", total)

zbir_pozitivni()



# БОНУС

import random

def najgolem_broj():
    
    listab = [random.randint(1, 100) for _ in range(10)]
    
    print("Listata na slucajni borevi od 1 do 100 e:", listab)
    print("Najgolem broj vo listata e:", max(listab))

najgolem_broj()