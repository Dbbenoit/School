namVar:str
checkingBalance:float
savingsBalance:float
pinNumber:int 


def ATMSetup():
    global namVar
    global checkingBalance
    global savingsBalance
    global pinNumber 
    pinNumber = 0

    print()
    nameVar = input("Please enter your name: ")
    confirmation = "n"
    
    while (confirmation !="y" and confirmation != "Y"):
        confirmation:str = input("You have entered  " + nameVar + ", is this correct? (y/n)" )

        print()

        if(confirmation == "n" or confirmation == "N"):
            nameVar = input("ok, please enter your name: ")
    
        if (confirmation != "y" and confirmation != "Y" and confirmation != "n" and confirmation != "N"):
            print("Invalid entry")

        if (confirmation == "y" or  confirmation == "Y"):
            print("Name saved as " + nameVar)

    print()
    print()
    checkingBalance = float(input("Please enter starting balance of Checking account: "))
    savingsBalance = float(input("Please enter starting balance for Savings account: "))

    print("Checking Account balance: " + str(checkingBalance))
    print("Savings Account balance: " + str(savingsBalance))
    print()


    
    doubleCheckPin:int = 1
    while ( pinNumber != doubleCheckPin):
        pinNumber = int(input("Please enter a Pin number: "))
        doubleCheckPin:int = int(input("Please reenter your pin: "))
        if (pinNumber != doubleCheckPin):
            print("Pin Numbers do not match")
            print()
    print("PIN Number Matches, Keep it safe")   
    print()     




    
def main():
    ATMSetup()
    

main()
print("The PIN selected is " + str(pinNumber))
