# Keep your code DRY - Don't Repeat Yourself
"""
def pecati_zdravo(): # vaka se kreira funkcijata
    print("Zdravo od funkcija")
pecati_zdravo() # vaka se povikuva funkcijata


def soberi_broevi(broj1, broj2, broj3=1):#broj 3 ako dolu vo red 14 ne dademe vrednost togas od tuka ke ja zeme vrednosta
    zbir = (broj1 + broj2)*broj3
    print(f"Zbirot e {zbir}")
brojot1 = 10
brojot2 = 18

soberi_broevi(broj3=2,broj1=brojot1,broj2=brojot2)
"""
"""
#Da se napravi funkcija koja ke prima ime kako argument i treba da pecati poraka Zdravo i imeto sto e isprateno.
def pozdrav(ime):
    print(f"Zdravo {ime}")
pozdrav("Biljana")



#Da se napravi funckija koja ke prima 2 argumenti, ime i godini. Da se proveri dali liceto e polnoletno ili maloletno I da se ispecati soodvetna poraka
def proverka(ime, godini):
    if godini >= 18:
        print(f"{ime} e polnoleten.")
    else:
        print(f"{ime} e maloleten")
proverka("Biljana",41)
proverka("Dimitar",10)
"""

def pecati_zdravo(): # vaka se kreira funkcijata
    print("Zdravo od funkcija")
pecati_zdravo() # vaka se povikuva funkcijata


def soberi_broevi(broj1:int, broj2:int, broj3:int=1):#broj 3 ako dolu vo red 14 ne dademe vrednost togas od tuka ke ja zeme vrednosta
    """
    Dokumentacija za funkicjata soberi broevi prima dva zadolzitelni broevi i eden nezadolzitelen.
    Ako ne dademe vrednost za broj 3 default ke bide 1
    Kako rezutat se vraka zbirot kako int tip na podatok
    """
    zbir = (broj1 + broj2)*broj3
    print(f"Zbirot e {zbir}")
    return zbir  #rezultaot e zacuvan
brojot1 = 10
brojot2 = 18

zbir = soberi_broevi(broj1=brojot1,broj2=brojot2)
print(f"Zbir od rezultaot od funkcijate e: {zbir}")