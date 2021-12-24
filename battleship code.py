"""
Battleship Project
Name:
Roll No:
"""

from typing import Counter
import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["boardsize"]=500
    data["cellsize"]=(int(data["boardsize"]/data["rows"]))
    data["numberofships"]=5
    data["winner"]=None
    data["maxturns"]=50
    data["temporaryShips"]=[]
    data["currentturns"]=0
    data["userShips"]=0

    temp=emptyGrid(data["rows"],data["cols"])
    data["userboard"]=emptyGrid(data["rows"], data["cols"])

    data["computerboard"]=addShips(temp,data["numberofships"])

    return data




'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["userboard"], True)
    drawGrid(data,compCanvas,data["computerboard"], False)
    drawShip(data,userCanvas,data["temporaryShips"])
    drawGameOver(data, userCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if  event.keysym == 'Return':
        makeModel(data)
        return False
    


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    #if (data["winner"] != None):
     #   return None
    rc = getClickedCell(data, event)
    if board=="user": 
        clickUserBoard(data, rc[0], rc[1])
    else:
        runGameTurn(data, rc[0], rc[1])
        
    

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    a=[]
    for i in range(rows):
        b=[]
        for j in range(cols):
            b.append(EMPTY_UNCLICKED)
        a.append(b)
    return a



'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    r=random.randint(1,8)
    c=random.randint(1,8)
    b=random.randint(0,1)
    if b == 0:
        ship=[[r-1,c],[r,c],[r+1,c]]
    else:
        ship=[[r,c-1],[r,c],[r,c+1]]
    return ship





'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in range(len(ship)):
        if grid[ship[i][0]][ship[i][1]]!=EMPTY_UNCLICKED:
            return False
    return True



'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numships):
    count=0
    while count<numships*3:
        create=createShip()
        check=checkShip(grid, create)
        if check == True:
            for j in create:
                grid[j[0]][j[1]] = 2
                count=count+1
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["rows"]):
        for cols in range(data["cols"]):
            if grid[row][cols]== SHIP_UNCLICKED:
                if showShips:
                    canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],(cols+1)*data["cellsize"], (row+1)*data["cellsize"], fill="yellow")
                else:
                   canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],(cols+1)*data["cellsize"], (row+1)*data["cellsize"], fill="blue")
            elif grid[row][cols]==SHIP_CLICKED:
                  canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],(cols+1)*data["cellsize"], (row+1)*data["cellsize"], fill="red")
            #elif
                #canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],(cols+1)*data["cellsize"], (row+1)*data["cellsize"], fill="blue")
            elif grid[row][cols]==EMPTY_CLICKED:
                 canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],(cols+1)*data["cellsize"], (row+1)*data["cellsize"], fill="white")
            else:
                canvas.create_rectangle(cols*data["cellsize"],row*data["cellsize"],(cols+1)*data["cellsize"], (row+1)*data["cellsize"], fill="blue")    

    canvas.pack()
    return None


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    row=0
    if ship[row][1]==ship[row+1][1]==ship[row+2][1]:
        ship.sort()
        if ship[row+1][0]-ship[row][0]==1 and ship[row+2][0]-ship[row+1][0]==1:
           return True
    return False   


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    row=0
    if ship[row][0]==ship[row+1][0]==ship[row+2][0]:
        ship.sort()
        if ship[row+1][1]-ship[row][1]==1 and ship[row+2][1]-ship[row+1][1]==1:
           return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    cell=data["cellsize"]
    return[int(event.y/cell),int(event.x/cell)]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    #canvas.create_rectangle(j*data["cols"]*data["cellsize"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="blue")
    print(ship)      
    for i in ship:
        x=i[0]
        y=i[1]
        canvas.create_rectangle(y*data["cellsize"], x*data["cellsize"], (y+1)*data["cellsize"], (x+1)*data["cellsize"],fill="white")

  
    canvas.pack()
    return 
   
    


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
   v=isVertical(ship) 
   h=isHorizontal(ship) 
   if(checkShip(grid,ship) and ((h)|(v)==True) and len(ship)==3): 
       return True 
   return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    k=data["userboard"]
    if shipIsValid(k,data["temporaryShips"]):    
        for i in data["temporaryShips"]:
            k[i[0]][i[1]]=SHIP_UNCLICKED
        data["userShips"]=data["userShips"]+1
    else:        
        print("Ship is not valid")
    data["temporaryShips"]=[]
    return 


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if(data["userShips"]==data["numberofships"]):
        return None
    k=data["userboard"]
    if k[row][col]==SHIP_UNCLICKED:
        return
    data["temporaryShips"].append([row,col])
    if len(data["temporaryShips"])==3:
        print(data["temporaryShips"])
        placeShip(data)
    if data["userShips"]==5:
        print("You can start the game")
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if (board[row][col]==SHIP_UNCLICKED):
        board[row][col]=SHIP_CLICKED
    if(board[row][col]==EMPTY_UNCLICKED):
        board[row][col]=EMPTY_CLICKED
    if (isGameOver(board)==True):
        data["winner"]=player



    return    


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):

    r=data["computerboard"]
    if ((r[row][col]==SHIP_CLICKED) or (r[row][col]==EMPTY_CLICKED)):
        return
    else:
        updateBoard(data, r, row, col, "user")
    [r,c]=getComputerGuess(data["userboard"])
    updateBoard(data, data["userboard"], r, c, "comp")
    data["currentturns"]=data["currentturns"]+1
    if (data["currentturns"]==data["maxturns"]):
        data["winner"] = "draw"

    


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    row = random.randint(0,9)
    col = random.randint(0,9)
    while ((board[row][col] == SHIP_CLICKED) or (board[row][col] == EMPTY_CLICKED)):
        row = random.randint(0,9)
        col = random.randint(0,9)
    return [row, col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j]==SHIP_UNCLICKED:
         return False
    return True   

    


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if (data["winner"]=="user"):
        canvas.create_text(250, 150, text="congratulations", fill="gold", font=("Arial","24","bold italic"))
        canvas.create_text(250, 250, text="PRESS ENTER IF YOU WANT TO PLAY", fill="black", font=("Arial","16","bold italic"))
    if (data["winner"]=="comp"):
        canvas.create_text(250, 150, text="YOU LOSE", fill="brown", font=("Arial","24","bold italic")) 
        canvas.create_text(250, 250, text="PRESS ENTER IF YOU WANT TO PLAY", fill="black", font=("Arial","16","bold italic"))
    if (data["winner"]=="draw"):
        canvas.create_text(250, 150, text="OUT OF MOVES", fill="silver", font=("Arial","24","bold italic"))
        canvas.create_text(250, 250, text="PRESS ENTER IF YOU WANT TO PLAY", fill="black", font=("Arial","16","bold italic"))       
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###
  
# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testEmptyGrid()
    test.testCheckShip() 
    test.testCreateShip() 
    test.testAddShips() 
    test.testMakeModel() 
    test.testDrawGrid() 
    test.testGrid() 
    test.testDrawShip() 
    test.testUpdateBoard()
    test.testGetComputerGuess() 
    test.testIsGameOver() 
    test.testDrawGameOver()

    ## Finally, run the simulation to test it manually ##
    
    runSimulation(500, 500)

    
    
    


