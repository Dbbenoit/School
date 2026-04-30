# name:str = input(str("Enter your name: "))
# print(name)


bookCount:int= 0
totalPages:int = 0

def displayBanner():
    print("LIBRARY CATALOG")

def initLibrary():
    global bookCount 
    bookCount = 0

def getLibrarianName():
    librarianName:str = input(str("Please enter your name"))
    while len(librarianName) < 2:
        print("invalid name, must be two characters")
        librarianName:str = input(str("Please enter your name"))
    return librarianName    

def getValidInt(prompt, low, high):
    prompt = int(prompt)
    while prompt < low or prompt > high:
        print("That is an invalid year")
        prompt:str=input(str("Enter Publication year: "))
        prompt = int(prompt)

def getValidPageCount():
    pageCount:int = int(input("Please enter the page count: "))
    while pageCount <= 0 or pageCount >= 2000:
        print("Invalid page count")
        pageCount = int(input("Please enter the page count: "))
    return pageCount

# def formatTitle(title:str):
#     newTitle:str 
#     print("newTitle is now " + title)
#     counter:int = 0
#     while counter<len(title):
#         print("counter = " + str(counter))
#         if counter == 0:
#             newTitle[0] = title[0].upper()
#         else:
#             newTitle[counter]= title[counter]
#         counter = counter + 1
#     return newTitle

def formatTitle(title:str):
    i:int = 1
    newTitle:str = title[0].upper()
    while i < len(title):
        newTitle= newTitle + title[i]
        i = i+1
    print("the proper format is " + str(newTitle))



def analyzeTitle(title:str):
    uppercase: int = 0
    lowercase: int = 0
    count = 0
    while count < len(title):
        if title[count].isupper():
            uppercase = uppercase + 1
        if title[count].islower():
            lowercase = lowercase + 1
        count = count + 1
    print("there are " + str(uppercase) + " upper, and " + str(lowercase) + " lower.")    

def catalogBook(title:str, pages:int):
    global bookCount
    bookCount = bookCount + 1
    global totalPages
    totalPages = totalPages + pages

def displayLibrarySummary():
    print("total pages: " + str(totalPages))
    print("total Book Count: " + str(bookCount))

def main():

    displayBanner()
    initLibrary()
    libName:str = getLibrarianName()
    print("Hello, " + libName.upper())
    while bookCount<4:
        print("Current book number: " + str(bookCount))
        title:str = input(str("Please enter the title: "))
        print("the title is " + str(title))
        formattedTitle:str =formatTitle(title)
        analyzeTitle(title)
        getValidInt(int(input("Enter publication year")), 1900, 2026)
        pages:int =getValidPageCount()
        catalogBook(formattedTitle, pages)
        response:str = input("catalog anbother book?" )
        if (response.lower() != "yes"):
            break
        
    displayLibrarySummary()



    


main()