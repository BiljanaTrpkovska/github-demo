# nie go definirame indeksot i vrednosta index:value
#x_dict = {} #prazen

#x_dict = {
#    "ime":"Stojan",
#    "prezime":"Stojanov",
#    "pol":"maski",
#    "email":["mail1@example.com", "mail2@excamle.com"],
#    "tel_broj":{
#        "privaten":"070259129",
#        "sluzben":"071243559"
#    }
#}
#print(x_dict["ime"])  # moze da zemame samo po eden indeks, ne poveke
#print(f"{x_dict["ime"]} {x_dict["prezime"]}")
#print(x_dict["tel_broj"])
#print(type(x_dict["tel_broj"]))

#dodavanje i update
#x_dict["grad"]="Skopje" # za dodavanje ili update eden element -  koga odi porgaramata i koga ke stigne do ovoj indeks ke proveri dali go ima ili ne. ako go ima ke go update, a ako go nema ke go dodade
#x_dict.update({"grad":"Skopje", "prezime":"Jovanov"}) #za dodavanje ili update na poveke podatoci od ednas

#Brisenje
#x_dict.pop("pol")
#del x_dict["pol"] # ova e opasen nacin, treba pazenje, zosto ako ne se stavi indeks togas cel dict ke se izbrise
#print(x_dict)

#for index in x_dict.keys(): # ova pravi lista od site indeksi
# print(x_dict[index]) # se pominuva ni sekoj podatok poseno i se printa

#for value in x_dict.values(): # lista od site vrednosti
#    print(value)

#for indeks, value in x_dict.items(): #lista od listi [indeks1, value1],[indeks2, value2]...
#    print("-------")
#    print(indeks)
#    print(value)
#    print("--------")

#vezbi Da se kreira dictioray vo koj ke imame ime prezi i godin na nekoj korisnik. Da se proveri dali korisnikot e polnoleten ili maloleten I zavisno rezultatot da se zacuva vo nov index “dali_polnoleten” da ili ne.
"""
korisnik_dict = {
   "ime":"Biljana",
    "prezime":"Dameska",
    "godini":41
}
print(korisnik_dict)
if korisnik_dict["godini"]>18:
    korisnik_dict["Dali e polnoleten"] = "DA"
    print("Korisnikot e polnoleten")
else:
    korisnik_dict["Dali e polnoleten"] = "NE"
    print("Korisnikot e maloleten")
print(korisnik_dict)
"""

#vezba2 Da se kreira prazen dictionary, korisnikot da moze da vnese 2 broevi koi ke se zacuvaat vo dictionary. Da se presmetaat operaciite +, -, *, / I rezultatite da se zacuvaat vo novi indexi. Na krajot da se ispecatat rezultatite pregledno
broj_dict = {}
broj_dict["broj1"] = int(input("Vensete broj 1: "))
broj_dict["broj2"] = int(input("Vensete broj 1: "))

broj_dict["zbir"] = broj_dict["broj1"]+broj_dict["broj2"]
broj_dict["odzemanje"] = broj_dict["broj1"]-broj_dict["broj2"]
broj_dict["mnozenje"] = broj_dict["broj1"]*broj_dict["broj2"]
broj_dict["delenje"] = broj_dict["broj1"]/broj_dict["broj2"]

print("Zbirot e:",broj_dict["zbir"])
print("Razlikata e:",broj_dict["odzemanje"])
print("Prizvdot e:",broj_dict["mnozenje"])
print("Kolicnikot e:",broj_dict["delenje"])