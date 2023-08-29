# countries_information = {}
# countries_information["Polska"] = ("Warszawa", 37.97)
# countries_information["Niemcy"] = ("Berlin", 83.02)
# countries_information["Słowacja"] = ("Bratysława", 5.45)

# def show_country_info(country):
#     country_information = countries_information.get(country)

#     print()
#     print(country)
#     print("-------")
#     print("Stolica: " + country_information[0])
#     print("Liczba mieszkańców (mln):" + str(country_information[2]))


# for country in countries_information.keys():
#     print(country)

# country = input("Informacje o jakim kraju chcesz wyświetlić? ")
# show_country_info(country)

# country_information = countries_information.get(country)

def display_sum(a, b):
    print(a+b)              #ta funkcja przyjmuje dwa arguenty i wyświetla ich sumę

def calculate_sum(a, b):
    return a + b            #ta finkcja przyjmuje dwa argumenty i zwraca!! ich sumę 
def print_message():
    print("To jest super wiadomość!")

#print_message()                         #ta funkcja ani niczego nie przyjmuje, ani niczego nie zwraca, po prostu wyświetla cos w konsoli.

# sum = calculate_sum(2,3) 
# print(sum)

sum = display_sum(2, 3)
print(sum)
