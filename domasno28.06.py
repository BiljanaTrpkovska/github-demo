# Zadaca broj 1

broj1 = int(input("Vnesi go prviot broj: "))
broj2 = int(input("Vnesi go vtoriot broj: "))

zbir = broj1 + broj2

if zbir < 100:
    print("Zbirot e pomal od 100.")
else:
    print("Zbirot ne e pomal od 100.")


# Zadaca broj 2

godina_ragjanje = int(input("Vnesi godina na ragjanje: "))
vozrast = 2026 - godina_ragjanje
print(f"Ti imas {vozrast} godini")
if vozrast < 18:
    print("Liceto e maloletno")
else:
    print("Liceto e polnoletno")


# Zadaca broj 3

a1 = int(input("Vnesi ja dolzinata na prviot pravoagolnik: "))
b1 = int(input("Vnesi ja sirinata na prviot pravoagolnik: "))
a2 = int(input("Vnesi ja dolzinata na vtoriot pravoagolnik: "))
b2 = int(input("Vnesi ja sirinata na vtoriot pravoagolnik: "))
plostina1 = a1*b1
plostina2 = a2*b2
print(f"Plostinata na prviot pravoagolnik e {plostina1}")
print(f"Plostinata na vtoriot pravoagolnik e {plostina2}")
if plostina1 > plostina2:
    print("Prviot pravoagolnik e pogolem")
elif plostina2 > plostina1:
    print("Vtoriot pravoagolnik e pogolem")
else:
    print("Dvata pravoagolnici se isti")

# Zadaca broj 4

agol1 = int(input("Vnesi go prviot agol: "))
agol2 = int(input("Vnesi go vtoriot agol: "))
agol3 = int(input("Vnesi go tretiot agol: "))

zbir = agol1 + agol2 + agol3

if zbir == 180 and agol1 > 0 and agol2 > 0 and agol3 > 0:
    print("So ovie agli moze da se kreira triagolnik")
else:
    print("So ovie agli ne moze da se kreira triagolnik")

# Zadaca broj 5

broj = int(input("Vnesi eden broj: "))
if broj %2 == 0:
    print("Brojot e paren")
else:
    print("Brojot e neparen")

