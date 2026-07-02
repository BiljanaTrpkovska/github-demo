#ciklusi za povtoruvanje so broenje
#ciklusi za povtoruvanje so uslov
"""
for brojac in range(5): #range(n) -> 0,1,2,3,4,5,  n-1
    print("Zdravo")
    print(f"Brojac: {brojac}")
"""
"""
zbir = 0
for brojac in range(5): 
    broj = int(input("Vnesete broj:"))
    zbir = zbir + broj #zbir += broj
print(f"Zbirot na broevite koi gi vnesove e: {zbir}")
"""
"""
for brojac in range (7):
    broj = int(input("Vnesete broj: "))
    if broj %2 == 0:
       print("Brojot e paren")
    else:
       print("Brojot e neparen.")    
"""
"""
for brojac in range (4):
    broj1 = int(input("Vnesete go prviot broj "))
    broj2 = int(input("Vnesete go vtoriot broj "))
    perimetar = 2*broj1+2*broj2
    plostina = broj1*broj2
    zbir = plostina + perimetar
    if zbir %2 == 0:
     print(f"Perimetarot e {perimetar}, postinata e {plostina} i borjot e paren")
    else:
     print(f"Perimetarot e {perimetar}, postinata e {plostina} i borjot e paren")

"""
"""
zbir = 0
br_povtrouranja = int(input("Kolku pati sakate da se izvrsi ciklusot: "))
for brojac in range(br_povtrouranja):
    broj = int(input("Vnesete broj:"))
    zbir = zbir + broj #zbir += broj
print(f"Zbirot na broevite koi gi vnesove e: {zbir}")
"""
#broj = 0
#while broj % 2 == 0:
#    broj = int(input("Vnesete paren broj"))
#print("Vnesovte neparen broj")

while True:
    broj = int(input("Vnesete paren broj: "))

    nov_broj = input("Dali sakate da vnesete nov borj: (DA/NE)")
    if nov_broj.upper() == "NE":
        break
    if broj % 2 !=0:
        print("Vnesovte neparen broj")
        break
    if broj > 100:
        print("Vnesovte broj pogolem od 100")
        break