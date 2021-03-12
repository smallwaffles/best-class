"""
program gools

put all actons in while loop 
pull the valuses stored at spisifec indexes
convert inputs to int
add exsit option 


"""
import random

myList = []
def mainProgram():
    while True:
        print("hi there lest work with lists")
        print("coose from the folowing options type the number of the choice ")
        choice = input("""1. add to a list,
2 return a valuse in a list
random srtch
3.exet """)
        if choice == "1":
            addToList ()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch ()
        else:
            break
        
def addToList():
    print("adding to list")
    newItem = input("type an integerhere            ")
    myList.append(int(newItem))
    #think abt airs
    
def randomSearch ():
    print("oh im so random")
    my list[random.randint(0, len (myList)-1)])
    

def indexValues():
    print("at what index point do you want to surtch")
    indexPos = input("type an index pozition here :                   ")
    print(mylist[int(indexPos)])




if __name__ =="__main__" :
    mainProgram ()
