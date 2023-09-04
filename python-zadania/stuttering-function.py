def stuttered_word(word):
    if len(word) < 2:
        return "Word has to be at least two letters long!"
    
#fstring

    stuttered = f"{word[:2]}...{word}?"
    print(stuttered)

input_word = input("Enter the word: ").lower()

result = stuttered_word(input_word)
print("Stuttered word: ", result)

