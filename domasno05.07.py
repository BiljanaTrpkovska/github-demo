
#1. Count Occurrences of an Element
lista_broj = [1,2,3,1,5,6,9,8,8,9,1,1,3]
broj = int(input("Vnesete broj koj sakate da se prebroi: "))
count = lista_broj.count(broj)
print(f"Brojot {broj} se pojavia {count} vo listata")

#2.Filter Even and Odd Numbers
lista = []
for n in range (10):
    number = int(input(f"Vnesete broj {n+1}: "))
    lista.append(number)
even_numbers = []
odd_numbers = []
for number in lista:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Parni broevi se: ", even_numbers)
print("Neparni broevi se: ", odd_numbers)

#3.Calculate the Average of a List
lista2 = []
for i in range(5):
    broj = int(input(f"Vnesi broj {i+1}: "))
    lista2.append(broj)
total = 0
for broj in lista2:
    total = total + broj
average = total / len(lista2)

print("Vnesenite broevi se:", lista2)
print("Zbirot na broevite e :",total)
print("Prosekot na vnesenite broevi e:", average)

#4.Remove Duplicates from a List

lista3 = []

for i in range(10):
    broj = int(input(f"Vnesi broj {i+1}: "))
    lista3.append(broj)
unique_list = list(set(lista3))

print("Orginalnata lista e:", lista3)
print("Lista bez duplikati:", unique_list)

#5 Shopping List Manager
shopping_list = {}   
for i in range(5):
    product = input("Vnesi proizvod: ")
    price = int(input(f"Vnesi cena za {product}: "))
    shopping_list[product] = price

print("Shopping lista")
zbir = 0
for product, price in shopping_list.items():
    print(f"{product} - {price} denari")
    zbir += price

print("Vkupno za plakjanje:", zbir, "denari")

