countries_and_capitals = {'Poland': 'Warsaw', 'Czechia': 'Prague', 'Germany': 'Berlin'}
#print(countries_and_capitals['USA']) ##zbiór nie zawiera USA, więć wyświetla się error, zastosować wyjątek z try i except:
try:
    print(2 / 2)
   # print(countries_and_capitals['USA'])

# except KeyError:
#     print("Klucz nie został znalezionu :(")
# except ZeroDivisionError:
#     print("Nie można dzielić przez 0")

##Można też tak:
except:
    print("Wystąpił wyjątek")
finally:
    print("To wykona się zawsze")

print("Jestem tutaj")
