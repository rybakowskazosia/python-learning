name = "Zosia"

#print(len(name)) #len- (długość) ilośc liter w słowie

##Metody:
#print(name.capitalize()) #metoda 1- CAPITALIZE- nie przyjmuje argumentów, wstawia wielkie litery tam gdzie trzeba?
#print(name.upper())     # metoda 2- UPPER-zamienia wszystkie litery na wielkie
#print(name.lower())     # metoda 3- LOWER- zammienia wszytskie litery na małe  
#print(name[0])          # metoda 4- wyświetlanie danej litery, indeksy liter liczymy od 0!
#print(name[0:2])        # ile liter chcemy wyświetlić
#print(name[3:]) 
#print(name[-3:]) 


#channel = "JAk nauczyć się programowania"
#print(channel.split(" "))   # metoda 5- SPLIT- podział na słowa, ta metoda zawiera argument, w tym przypadku argumentem jest spacja


#join_string = " "
#print(join_string.join(["JAk", "nauczyć", "się", "programowania"])) # metoda 6- JOIN- odwrotne d split- łączy wyrazy, zawiera argument.


#print(name.startswith("Z"))
#print(name.startswith("z")) # zwraca wartości true/false

#print(name.endswith("A"))
#print(name.endswith("a"))    # zwraca wartości true/false
      
#print(name.rstrip("a"))     # usuwa ostatnią literę wyrazu
#print(name.lstrip("Z"))     # usuwa pierwszą literę wyrazu
#print(name.strip("Z"))      # usuwa litery i z lewej i zprawej strony
#print(name.strip("a"))


#first_name = "Zosia"
#last_name = "Rybakowska"

#print(first_name + " "+ last_name)

#join_string = " "
#print(join_string.join([first_name,last_name]))

james_bond = 7
print(str(james_bond).zfill(3))