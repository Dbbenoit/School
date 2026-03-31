# Daniel Benoit COMI1150 practive problemsDan

x:str= input("Please enter a username: ")
print("You have entered " + x + ".")

num:int = int(input("Please enter a number: "))
confirm:str = input("You have chosen "+ str(num) + ", is this correct? y/n")
while (confirm != "y" and confirm != "Y" and confirm != "n" + confirm != "N"):
    print("I don't understand")
    confirm = input("You have chosen "+ str(num) + ", is this correct? y/n")
print("You have endered " + confirm)

print("Now that we have picked a number, lets pick another number to multiply it by")
secondnum:int = int(input("Go on, give me a second integer: "))
confirm = input("You have entered " + str(secondnum) + ", is this correct? y/n")
insultNecessary = "n"
while(confirm != str("y") and confirm != str("Y") and confirm != str("n") and confirm != str("N")):
    print("Youre not paying attention, are you")
    confirm = input("""You have entered " """ + confirm + """ ", is this correct? y/n """)
    insultNecessary:str = "y"
if (insultNecessary == "y"):
    print("Great job, you finally followed instructions")
    print("You enetered " + confirm + ".")
else:
    print("You entered " + confirm + ".")

        


