"""
    == -> isto
    =! -> razlicno
    < -> pomalo
    > -> pogolemo
    <= -> pomalo i ednakvo
    >= -> pogolemo i ednakvo

"""

#broj = int(input("Vnesi broj: "))
#if broj < 50:
    #print("Brojot e pomal od 50")
#else:
    #print("Brojot e pogolem od 50")
"""
broj1 = int(input("Vnesi broj eden: "))
broj2 = int(input("Vnesi broj dva: "))
plostina = broj1*broj2
print(f"Plostinata na broevite {broj1} i {broj2} e {plostina}")
perimetar = 2*broj1+2*broj2
print(f"Perimetarot na broevite {broj1} i {broj2} e {perimetar}")
zbir = plostina + perimetar
print(f"Zbirot na plostinata {plostina} i perimetrot {perimetar} e {zbir}")
if zbir <= 200:
    print("Brojot e pomal ili ednakov na 200")
else:
    print("Brojot ne e pomal od 200")

broj3 = int(input("Vnesi broj tri: "))

if broj3 % 2 == 0:
    print("Brojot e paren.")
else:
    print("Brojot e neparen.")

"""
"""

broj =  int(input("Vnesi broj: "))
if broj < 50:
    print("Brojot e pomal od 50")
elif broj < 100:
    print("Brojot e pogolem od 50 no pomal od 100")
elif broj < 200:
    print("Brojot e pogolem od 10 no pomal od 200")
else:
    print("Brojot e pogolem od 200")

    
    """
"""

agol = int(input("Vnesi golemina na agol: "))
if agol < 90:
    print("Ostar agol")
elif agol == 90:
    print("Prav agol")
elif agol <= 180:
    print("Tap agol")
else:
    print("Ramen ili refleksen agol")
   """

# and, or   
agol = int(input("Vnesi golemina na agol: "))
#if agol < 90 and agol % 2 == 0:
    #print("Ostar agol")
if agol < 90:
    if agol % 2 == 0:
        print("paren")
else:
    print("neparen")


