"""
program gools
add items to list (ints)
offer the user a choice of actions
pull the valuses stored at spisifec indexes
convert inputs to int

"""
def mainProgram():
    myList = []
    print("hi there lest work with lists")
    print("coose from the folowing options type the number of the choice ")
    choice = input("add to a list 2 return a valuse at a list ")
    if choice == "1":
        addToList ()
    elif choice == "2":
        indexValues()
        
def addToList():
    print("adding to list")
    newItem = input("type an integerhere            ")
    myList.append(int(newItem))
    #think abt airs
    

def indexValues():




if __name__ =="__main__":
    main program()
