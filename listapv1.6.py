"""
program gools

put all actons in while loop 
pull the valuses stored at spisifec indexes
convert inputs to int
add exsit option 


"""
import random
myList = []
unique_list = []
def mainProgram():
    while True:
        print("hi there lest work with lists")
        print("coose from the folowing options type the number of the choice ")
        choice = input("""1. add to a list,
2 return a valuse in a list
random srtch
5 liniar shertch 
3add a bunthc of numbers
print list
3.exet """)
        if choice == "1":
            addToList ()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABuntch ()
        elif choice == "4":
            linearSearch()
        elif choice == "5":
            randomSearch()
        elif choice == "6":
            sortList (myList)
        elif choice == "7":
           printLists ()
       
            
        else:
            break
        
def addToList():
    print("adding to list")
    newItem = input("type an integer here            ")
    myList.append(int(newItem))
    #think abt airs


def addABuntch():
    print ("lets add some numbers")
    numToAdd = input ("how many intigers would you like to add         ")
    numRange = input ("and how many nubers would you like to add")
    for x in range (0, int (numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print ("your list is complete!")


def linearSearch() :
    print ("we are going to go though this one etem at a time")
    seartchValue = input ("what are you looking for           ")
    for x in range (len(myList)) :
        if myList [x] == int (seartchValue) :
            print("your item is at index pozition {}".format(x))
    
    
def randomSearch ():
    print("oh im so random")
    print (mylist[random.randint(0, len (myList)-1)])

def indexValues():
    print("at what index point do you want to surtch")
    indexPos = input("type an index pozition here :                   ")
    print(mylist[int(indexPos)])

def sortList (myList):
    #my list is the argument this function takes
    for x in myList:
        if x not in unique_list:
            unique_list.append (x)
    unique_list.sort ()
    showMe = input("whana see your sorted list      y/n ")
    if showMe.lower () =="y ":
        print (unique_list)
        
def printList () :
    if len (unique_list) == 0:
        print (myList)
    else:
        witchOne = input ("witch list do you whant to see sorted or unsorted ")
        if witchOne.lower () == "sorted":
            print (unique_list)

if __name__ == "__main__" :
    mainProgram ()
