# Set elementite nemaat svoja rezervirana pozicija kako kaj listite, ne moze da ima duplikati, ne moze da se koristat indeksite, ako se printa nekolku pati, sekogas razlicno ke se isprinta

#x_set = {"ponedelnik",1,2,3,4,"python", "ovosje", "ponedelnik", 3.14}
#print(x_set)
#print(x_set)
#x_set.add("Nov element")
#print(x_set)
#x_set.remove(3.14)
#print(x_set)

lista_duplikati = [1,1,1,2,3,3,3,3,4,4,5,6,101,100,102,102]
set_duplikati=set(lista_duplikati)
lista_cisti = list(set_duplikati)
print(lista_cisti)