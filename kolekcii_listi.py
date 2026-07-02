# List, Tuple, Set, Dictionary

#lista = [1,2,3,4,"python", "ovosje", "ponedelnik", True, 3.14]
#print(lista)
#print(lista[4]) pozitivno indeksiranje, od napred pocnuvajki od 0
#print(lista[-1]) negatinvo indeksiranje, od nazad od -1
#print(lista[4:7])prviot indeks vleguva, posledniot indeks ne vleguva

#lista = [100,200,400,"prolet", "leto", "esen", "zima", 1.2, 100,200]
#print(lista[6])
#print(lista[-3])
#print(lista[1:7]

#lista.append("nov element") # dodadi novo vo lista, na posledno mesto
#lista.insert(2,333) #2 e indeksot i na toa mesto go stava noviot element, a drugite gi pomestuva ponataka
#lista[5] = "Jabolki" # indekosot 5 se menuva od python vo jabolki, broenjeto e posle promenata na dodaden element

#lista.remove("ponedelnik") #brisenje samo po vrednost ne po indeks
#lista.pop(4) # brise spored indeks
#lista.pop()#se brise posledniot element
#lista.clear() # gi brise site elementi vo listata no ne i listata, taa si stoi

#lista_broevi = [1,2,3,4,5,12,13,11]
#for broj in lista_broevi: #na sekoe povtoruvanje ciklusot pominuva niz nov element i moze na sekoj element da se pristapuva posebno
#    dupliran_broj = broj*2
#    if dupliran_broj %2 == 0 :
#        print(f"Brojot {broj} pomnozen so 2 e paren broj")
#    else:
#        print(F"Brojot {broj} pomnozen so 2 e neparen broj")

#lista = []
#br_elementi = int(input("Kolku elementi sakate da vnesete:"))
#for element in range(br_elementi):
#    element = input(f"Vnesete elementi: ")
#    lista.append (element)
#    print("Listata e: ", lista)

#parni = []
#neparni = []
#for broj in range (10):
#    broj = int(input(f"Vnesete broj: "))
#    if broj % 2 == 0:
#        parni.append (broj)
#    else:
#        neparni.append(broj)
#print("Parni broevi:", parni)
#print("Neparni broevi:", neparni)

#zbir = 0
#for ocena in range (5):
#    ocena = int(input(f"Vnesi ocena: "))
#    zbir = zbir + ocena
#prosek = zbir/5
#print ("Prosekot e:", prosek)

#lista = [1,2,3,4,"python", "ovosje", "ponedelnik", True, 3.14, 3, 4, 4]
#br_na_4ki = lista.count(4) # treba da se zacuva rezulattot
#print(br_na_4ki)
#indeks_element = lista.index("python")# ni go pronagoa mestoto na odreden element
#print(indeks_element)
#dolzina = len(lista) #kolku elementi ima vo listata
#lista.sort() # default e ascending; reverse=true - descending, ovde vo ovaa lista ne moze da sortiraa zosto vo listata ima i broj i teks, treba da ili samo broevi ili zamo tekst
#print(lista)

oceni = []
ocenka = int(input("Kolku oceni sakate da vnesete: "))
for borj in range (ocenka):
    ocenka = int(input(f"Vnesi ocenka: "))
    oceni.append(ocenka)
zbir = sum(oceni)
broj_5 = oceni.count(5)
broj_4 = oceni.count(5)
prosek=zbir/len(oceni)
print("Prosekot e:", prosek)
print("Prosekot e:", prosek)
print("Broj na 5ki:", broj_5)
print("Broj na 4ki:", broj_4)