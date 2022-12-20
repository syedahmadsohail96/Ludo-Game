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
logo3 = PhotoImage(file="red.gif")                                                     #Loading all the image files that are required in the game.
logo4 = PhotoImage(file="blue side.gif")
logo5 = PhotoImage(file="green side.gif")
logo6 = PhotoImage(file="yellow side.gif")
logo7 = PhotoImage(file="center.gif")

logog = PhotoImage(file="greenbox.gif")
logogs = PhotoImage(file="greenstop.gif")
logoy = PhotoImage(file="yellowbox.gif")
logoys = PhotoImage(file="yellowstop.gif")
logob = PhotoImage(file="bluebox.gif")
logobs = PhotoImage(file="bluestop.gif")
logor = PhotoImage(file="redbox.gif")
logors = PhotoImage(file="redstop.gif")
logoh = PhotoImage(file="head.gif")
logot = PhotoImage(file="tail.gif")
logoh1 = PhotoImage(file="head1.gif")
logot1 = PhotoImage(file="tail1.gif")
logoh2 = PhotoImage(file="head2.gif")
logot2 = PhotoImage(file="tail2.gif")
logoh3 = PhotoImage(file="head3.gif")
logot3 = PhotoImage(file="tail3.gif")

Label(image=logo2, width=298, height=298).place(x=-1, y=-1 )
Label(image=logo4, width=300, height=300).place(x=(-2), y=(448 ))
Label(image=logo5, width=296, height=296).place(x=(450), y=(0 ))
Label(image=logo6, width=294, height=294).place(x=(450), y=(450 ))
Label(image=logo7, width=150, height=150).place(x=(298), y=(298 ))

c=0

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


    v = 0
    while (v != 250):

        Label(image=logog, width=46, height=46).place(x=(350), y=(50 + v))
        v = v + 50

    Label(image=logog, width=46, height=46).place(x=(300), y=(100))
    Label(image=logogs, width=46, height=46).place(x=(400), y=(50 ))

    v = 0
    while (v != 250):
        Label(image=logoy, width=46, height=46).place(x=(450 + v), y=(350))
        v = v + 50

    Label(image=logoy, width=46, height=46).place(x=(600), y=(300))
    Label(image=logoys, width=46, height=46).place(x=(650), y=(400))

    v = 0
    while (v != 250):
        Label(image=logor, width=46, height=46).place(x=(50 + v), y=(350))
        v = v + 50

    Label(image=logor, width=46, height=46).place(x=(100), y=(400))
    Label(image=logors, width=46, height=46).place(x=(50), y=(300))

    v = 0
    while (v != 250):
        Label(image=logob, width=46, height=46).place(x=(350 ), y=(450 + v))
        v = v + 50

    Label(image=logobs, width=46, height=46).place(x=(300), y=(650))
    Label(image=logob, width=46, height=46).place(x=(400), y=(600))

    Label(image=logoh, width=46, height=46).place(x= 250, y= 400)
    Label(image=logot, width=46, height=46).place(x= 300, y= 450)
    Label(image=logoh1, width=46, height=46).place(x=400, y=450)
    Label(image=logot1, width=46, height=46).place(x=450, y=400)
    Label(image=logoh2, width=46, height=46).place(x=450, y=300)
    Label(image=logot2, width=46, height=46).place(x=400, y=250)
    Label(image=logoh3, width=46, height=46).place(x=300, y=250)
    Label(image=logot3, width=46, height=46).place(x=250, y=300)



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

    global box

    if c == 0:

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

        Label(image=logo3, width=20, height=20).place(x= (box[26].x) + 13, y= (box[26].y) + 14)


    else: # HERE ALL THE GAME OCCURS ... IF WAGHAIRA, MOVEMENT IDHAR HOGI !!!


        Label(image=logo3, width=20, height=20).place(x= (box[-1 + c].x) + 13, y= (box[-1 + c].y) + 14)



main()










def leftClick(event):                         #Main play function is called on every left click.

    global c
    c=c+1
    x = root.winfo_pointerx() - root.winfo_rootx()  # This formula returns the x,y co-ordinates of the mouse pointer relative to the board.
    y = root.winfo_pointery() - root.winfo_rooty()

    print("Click at: ",x,y)
    main()

root.bind("<Button-1>", leftClick)


root.mainloop()


