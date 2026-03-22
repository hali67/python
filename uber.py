print("Welcome to Uber!")
print("Select your ride: ")
print("1. Bike")
print("2. Car")


choice = int( input("Enter your choice: ") )


if( choice == 1):
    print( "what type of bike? ")
    print("1.Suron\n")
    print("2.GT 650\n")


    choice2=int(input("Enter you choice2: "))
    if choice2==1: 
        print("You have selected Suron.")
    else:
        print("You have selected GT 650.")


elif( choice == 2):
    print( "what type of car?" )
    print("1. Nissan GTR")
    print("2. Mustang 1969")
    choice3=int(input("enter your choice3: "))

    if choice3==1:
      print("You have selected Nissan GTR")
    else:
        print("You have selected Mustang 1969")
else:
    print("Wrong Choice!")
print("Hand Crafted By Meredith")