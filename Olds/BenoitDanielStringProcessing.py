def main():

    userName:str= str(input("Please enter your name: "))
    print("Welcome, " + str(userName))
    roundsLeft:int = 0
    print()
    displayMenu()
    while (roundsLeft<10):
        userChoice:int = int(input(userName + ", what would you like to do? "))
        while (userChoice !=0 and userChoice != 1 and userChoice !=2 and userChoice !=3 and userChoice !=4 ):
            print("Invalid choice")
            displayMenu()
            userChoice: int = int(input(userName + ", what would you like to do? "))
            # roundsLeft = roundsLeft + 1

        if (userChoice == 1):
            s:str = input(str("OK, enter a test value to provide to the isUYes function: "))
            print(isYes(s))
            print()
            roundsLeft = roundsLeft + 1

        elif (userChoice ==2):
            password:str = input(str("Enter your password.  Ill tell you if its complex: " ))
            print( str(isComplexPassword(password)))
            print()
            roundsLeft = roundsLeft + 1

        elif (userChoice == 3):
            s1:str = input(str("Please enter your first string:"))
            s2: str = input(str("Please enter your second string:"))
            returnResult:str = calcWordSimilarity(s1, s2)
            print("back in the main function")
            print("# " + str(returnResult) + " because " + str(int(returnResult * len(s1))) + "/" + str(len(s1)) + " match")
            print()
            roundsLeft = roundsLeft + 1

        else:
            roundsLeft = 10


    print("Thanks for playing")


def displayMenu():
    print("1. Test the Yes Function")
    print("2. Test the isComplexPassword function")
    print("3. Test the calcWordSimilarity function")
    print("4. Test the computeGCPercentage function (if done)")
    print("Press 0 to exit")

def isYes(s):
    if len(s) ==1:
        yString:str= "yY"
        if s in yString:
            return True
    elif len(s) == 3:
        s=s.upper()
        if s == "YES":
            return True
    else:
        return False


    s = s.upper()
    goodChars:str = "YES"
    return s in (s.upper())

def isComplexPassword(password):
    meetsLengthRequirement: bool = False
    hasCapitolLetter:bool = False
    hasNumber:bool = False
    symbolList:str = "!#$"
    hasSymbol:bool = False
    i: int = 0

    if len(password) > 7:
        meetsLengthRequirement = True
        print("password is long enough")

    while i < len(password):
        if password[i].isupper():
            hasCapitolLetter = True
            # print("password has a capital letter")
        if password[i].isdigit():
            hasNumber = True
            # print("password has a number")
        if password[i] in symbolList:
            hasSymbol = True
            # print("password has a symbol")
        i = i + 1

    if (hasCapitolLetter == True and hasNumber == True and hasSymbol == True and meetsLengthRequirement == True):
        return True
    else:
        return False

def calcWordSimilarity(s1, s2):
    print("function started")
    i = 0
    if (len(s1) != len(s2)):
        return 0
    numberOfMatches:int = 0

    print("second part of function started")
    while(i < len(s1)):
        if  s1[i] == s2[i]:
            numberOfMatches = numberOfMatches + 1
            print("Number of matches +1")
        i = i + 1

    return (numberOfMatches / len(s1))

main()