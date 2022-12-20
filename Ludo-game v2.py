from tkinter import *                                                                         #Tkinter is used as the GUI.
from tkinter import messagebox
import sys
import os

root = Tk()


root.resizable(width=False, height=False)                                                      #The window size of the game.
root.geometry('1000x750')
root.configure(background='green')
root.title("Checkers")

logo = PhotoImage(file="whitebox.gif")                                                     #Loading all the image files that are required in the game.
logo2 = PhotoImage(file="red side.gif")                                                     #Loading all the image files that are required in the game.
redpiece = PhotoImage(file="red.gif")                                                     #Loading all the image files that are required in the game.
logo4 = PhotoImage(file="blue side.gif")
logo5 = PhotoImage(file="green side.gif")
logo6 = PhotoImage(file="yellow side.gif")
logo7 = PhotoImage(file="center.gif")
greenpiece = PhotoImage(file="green.gif")
bluepiece = PhotoImage(file="blue.gif")
yellowpiece = PhotoImage(file="yellow.gif")

Label(image=logo2, width=298, height=298).place(x=-1, y=-1 )
Label(image=logo4, width=300, height=300).place(x=(-2), y=(448 ))
Label(image=logo5, width=296, height=296).place(x=(450), y=(0 ))
Label(image=logo6, width=294, height=294).place(x=(450), y=(450 ))
Label(image=logo7, width=150, height=150).place(x=(298), y=(298 ))

def board():
    v = 0
    z=0

    while (v != 300):
        z=0
        while (z != 150):

            Label(image=logo, width=46, height=46).place(x=(300 + z), y=(0 + v))
            z=z + 50
        v= v + 50

    z=0
    v=0
    while (v != 300):
        z=0
        while (z != 150):

            Label(image=logo, width=46, height=46).place(x=(0 + v), y=(300 + z))
            z=z + 50
        v= v + 50

    #####################

    v = 0
    z=0

    while (v != 300):
        z=0
        while (z != 150):

            Label(image=logo, width=46, height=46).place(x=(300 + z), y=(450 + v))
            z=z + 50
        v= v + 50

    z=0
    v=0
    while (v != 300):
        z=0
        while (z != 150):

            Label(image=logo, width=46, height=46).place(x=(450 + v), y=(300 + z))
            z=z + 50
        v= v + 50

class Box:

    def __init__(self, num=0, x=0, y=0):

        self.num = num
        self.x = x
        self.y = y



    #def run(self):
     #   print("{} the dog runs".format(self.name))

    #def eat(self):
     #   print("{} the dog eats".format(self.name))

    #def bark(self):
     #   print("{} the dog barks".format(self.name))


def main():

    board()

    box = [Box() for i in range(52)]
    redbox = [Box() for i in range(7)]
    bluebox = [Box() for i in range(7)]
    greenbox = [Box() for i in range(7)]
    yellowbox = [Box() for i in range(7)]

    for i in range(7):
        redbox[i].x = (0 + (50*i))
        redbox[i].y = 350
        bluebox[i].x = 350
        bluebox[i].y = (700 - (50*i))
        yellowbox[i].x = (700 - (50*i))
        yellowbox[i].y = (350)
        greenbox[i].x = 350
        greenbox[i].y = (0 + (50*i))

    for i in range(6):
        box[i].x = 300
        box[i].y = (700 - (50*i))

    for i in range(6,12):
        box[i].x = (250 - (50*(i-6)))
        box[i].y = (400)

    box[12].x = 0
    box[12].y = 350

    for i in range(13,19):
        box[i].x = (0 + (50*(i-13)))
        box[i].y = (300)

    for i in range(19,25):
        box[i].x = (300)
        box[i].y = (250 - (50*(i-19)))

    box[25].x = 350
    box[25].y = 0

    for i in range(26,32):
        box[i].x = (400)
        box[i].y = (0 + (50*(i-26)))

    for i in range(32,38):
        box[i].x = (450 + (50*(i-32)))
        box[i].y = (300)

    box[38].x = 700
    box[38].y = 350

    for i in range(39,45):
        box[i].x = (700 - (50*(i-39)))
        box[i].y = (400)

    for i in range(45,51):
        box[i].x = (400)
        box[i].y = (450 + (50*(i-45)))

    box[51].x = 350
    box[51].y = 700

    class RollTheDice:
        def __init__(self, parent):
            self.dieParent = parent
            self.dieContainer = Frame(parent).pack()

            self.dieLabel = Label(background="orange", text="YOU HAVE A DICE CLICK TO ", fg="black")
            self.dieLabel.place(x=800, y=100)

            #self.dieEntry = Entry(self.dieContainer)
            #self.dieEntry.place(x=800, y=60)

            self.sideLabel = Label(background="orange",text="ROLL AND FIND YOUR NUMBER",fg="black")
            self.sideLabel.place(x=800, y=130)

            #self.sideEntry = Entry(self.dieContainer)
            #self.sideEntry.place(x=800, y=160)

            global rolldisp
            rolldisp = StringVar()
            self.rollResult = Label(self.dieContainer, textvariable=rolldisp)
            self.rollResult.place(x=850, y=500)

            self.diceButton = Button(self.dieContainer)
            self.diceButton.configure(text="Roll the Dice!", background="orangered1")
            self.diceButton.place(x=800, y=200)
            self.diceButton.bind("<Button-1>", self.diceButtonClick)
            self.diceButton.bind("<Return>", self.diceButtonClick)

            self.quitButton = Button(self.dieContainer)
            self.quitButton.configure(text="Quit", background="blue")
            self.quitButton.place(x=890, y=200)
            self.quitButton.bind("<Button-1>", self.quitButtonClick)
            self.quitButton.bind("<Return>", self.quitButtonClick)

        def diceButtonClick(self, event):
            die = int(1)
            side = int(6)
            DieRoll(die, side)

        def quitButtonClick(self, event):
            self.dieParent.destroy()

    def DieRoll(dice, sides):
        import random
        rollnumber = 1
        runningtotal = 0
        endresult = ""
        while rollnumber <= dice:
            roll = random.randint(1, sides)
            s= str(roll)
            endresult += "YOUR NUMBER IS: "
            endresult += str(rollnumber)
            endresult += ": "
            endresult += str(roll)
            endresult += "\n"
            #runningtotal += roll
            rollnumber += 1
        finalresult = ""
        finalresult += endresult
        rolldisp.set(finalresult)
        print (s)


    root.title("Die Roller")
    myapp = RollTheDice(root)

    Label(image=redpiece, width=20, height=20).place(x= (box[s].x) + 13, y= (box[s].y) + 14)
    Label(image=greenpiece, width=20, height=20).place(x=(box[14].x) + 13, y=(box[14].y) + 14)
    Label(image=bluepiece, width=20, height=20).place(x=(box[15].x) + 13, y=(box[15].y) + 14)
    Label(image=yellowpiece, width=20, height=20).place(x=(box[1].x) + 13, y=(box[1].y) + 14)



main()










def leftClick(event):                         #Main play function is called on every left click.
    x = root.winfo_pointerx() - root.winfo_rootx()  # This formula returns the x,y co-ordinates of the mouse pointer relative to the board.
    y = root.winfo_pointery() - root.winfo_rooty()

    print("Click at: ",x,y)

root.bind("<Button-1>", leftClick)


root.mainloop()


