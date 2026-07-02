# Задача 1:
"""
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
"""
# Задача 3

def zbir_do_n():
    n = int(input("Vnesete broj: "))   
    zbir = 0                         
    for i in range(1, n + 1):          
        zbir += i                     
    print(f"Zbirot na broevite od 1 do {n} e: {zbir}")

zbir_do_n()