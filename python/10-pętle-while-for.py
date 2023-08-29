#number = 1

#while number < 6:
#    print(number)
#    number += 2

for number in range(0,10):
    if number == 5:
        continue #przerywa aktualne wykonywanie pętli i przechodzi do kolejnej (tutaj doszło od 0-4, na 5 przerwało i kontynuowało od 6 do 9)
    print(number)
    