def find_the_highest(numbers_list):
    if len(numbers_list) == 1:
        return numbers_list[0]
    
    if len(numbers_list) == 0:
        return None
    
## podział listy na pół:

    mid = len(numbers_list) // 2
    left_half = numbers_list[:mid]
    right_half = numbers_list[mid:]

    max_left = find_the_highest(left_half)
    max_right = find_the_highest(right_half)

    return max(max_left, max_right)

input_str = input("Specify a list of integers: ")

##w razie błędu:
try:
    input_list= [int(a) for a in input_str.split()] #zmiana tekstu na listę liczb całkowitych
except:
    print("The numbers entered are incorrect. Make sure they are integers.")
else:
    highest = find_the_highest(input_list)
    print("The highest integer in the list is: ", highest)

