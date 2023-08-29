user_choice = -1
user_choice = int(input("Wybierz liczbę: "))
print(user_choice)


tasks = []
tasks.append("Wynieść śmieci")
tasks.append("Posprzątać biurko")

while user_choice != 5:
    if user_choice == 1:
        print(tasks)

    if user_choice == 2:
        task = input("Wpisz treść zadania: ")
        tasks.append(task)

    #if user_choice == 3:


    print() 
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")

    break

