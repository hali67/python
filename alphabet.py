char = input("Enter the Alphabet: ")

if char.isalpha() and len(char) == 1:
    print("It is an Alphabet")
else:
    print("It is not an Alphabet.")