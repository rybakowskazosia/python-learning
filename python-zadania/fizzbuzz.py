
for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


#Inna metoda: pętla for i lista
# for number in range (1,101):
#     output = 'Fizz'*(number % 3 == 0) + 'Buzz'*(number % 5 == 0)
#     print(output or number)
