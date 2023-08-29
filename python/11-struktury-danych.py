## 1.LIST- lista elementów

#names_list = []
#names_list.append("Zosia")
#names_list.append("Marta")
#names_list.append("Marysia")

#names_list = ["Zosia", "Marta", "Marysia", "Ania", "Zosia"]


#names_list.reverse() #wyświetlenie listy od tyłu
#names_list.sort() #wyświetla alfabetycznie
#print(names_list)
#SORTOWANIE MOŻE BYĆ W DRUGA STRONĘ:
#names_list.sort(reverse=True) 
#print(names_list)

#print(names_list[3]) #wyświetla dany element listy


#duplikaty--> finkcja count liczy ile razy dany element się powtarza, funkcja len- podaje długość listy
#print(names_list.count("Zosia"))

#print(len(names_list))

#print(names_list)

##jeżeli chcemy wyświetlić poszczególne elementy z listy można skorzystać z pętli for

#for name in names_list:
#    print(name)

#METODA POP-zwraca dany element z listy i jednocześnie go usuwa:
#print(names_list.pop(2))

#print(names_list)

#METODA REMOVE-usuwa z listy bez zwracania danego elementu (jeśli są duplikaty, metoda ta usuwa pierwszy, na który się natknie):
#print(names_list.remove("Zosia"))


#METODA CLEAR- usuwa wszystkie elementy z listy
#names_list.clear()
#print(names_list)

#ŁĄCZENIE ZE SOBĄ LIST:
#names_list2 = ["Dominik"]
#names_list3 = names_list + names_list2

#print(names_list3)


##2.TUPLE- KROTKA- to struktura niezmienna (w przeciwieństwie do listy, którą można cały czas zmieniać), krotki używa się raczej do zgrupowania danych dotyczących pewnego konceptu (przykład z person)

#names_list = ("Zosia", "Marta", "Marysia", "Ania", "Zosia")

#print(names_list)

#person = ("Zosia", "Rybakowska", 20)

#print(person)

#print(len(person))

#print(person.count("Zosia"))

##3.SET-podobny do listy, ale nie można mieć w secie zduplikowanych danych
#names_set = {} #-->ten zapis stworzy anm słownik (dictionary)
#names_set = set () #tak tworzy się pusty set
#names_set = {"Zosia", "Marta", "Marysia", "Ania", "Zosia"}

#DODAWANIE ELEMENTÓW DO SETU:
#names_set.add("Artur")
#names_set.add("Dominik")

#names_set2 = {"Mariusz", "Tytus"}

#names_set3 = names_set.union(names_set2) #w taki sposób dodaaje się dwa sety
#names_set.update(names_set2) #modyfikacja istniejącego już setu, bez tworzenia nowego
#PORÓWNYWANIE SETÓW:
#names_set3 = names_set.difference(names_set2)

#names_set3 = names_set.intersection(names_set2)

#names_set3 = names_set.symmetric_difference(names_set2)

#names_set.clear()

#for name in names_set:
#    print(name)

#USUWANIE ELEMENTU Z SETU:
#names_set.remove("Zosia")

#names_set.discard("Marysia")
 

#print(names_set[0]) #--> to nie zadziała w secie

#jAK MOŻNA DODAĆ SET DO LISTY:

#names_list = ["Artur", "Rafał"]

#names_list.extend(names_set2) #dodawanie setu do listy

#rint(names_list)

#SŁOWNIK/DICTIONARY:

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}
countries_and_capitals['Czechia'] = "Prague" #dodawanie do słownika

#print(countries_and_capitals)

#for country, capitals in countries_and_capitals.items():
#    print(country + "-" + capitals)

#print(countries_and_capitals["USA"])
#print(countries_and_capitals.get("USA"))

#print(countries_and_capitals.setdefault("USA", "Washington DC"))

#countries_and_capitals.pop("Poland") #usuwa wartość ze słownika
#(countries_and_capitals.popitem())

#if "USA"in countries_and_capitals:
 #else:
#    print("Nie znaleziono!")

#print("USA" in countries_and_capitals) #Zwraca wartość true/false


countries_and_capitals.clear()
print(countries_and_capitals)