from tkinter import *

root = Tk()


#root.resizable(width=False, height=False)
root.geometry('1000x1000')                                #This intitallizes the game window



canvas = Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()
canvas2 = Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas2.grid()


logo = PhotoImage(file="Ludo Board.gif")                  #Load the game board
logo2 = PhotoImage(file="Browng.gif")

Label(image=logo2, width=60, height=60, relief=SUNKEN).place(x=100, y=100)



Label(canvas2, image=logo).pack(side="left")                  #Adjusting to optimum position

def callback(event):
    draw(event.x, event.y)

def draw(x, y):
    paint.coords(circle, x-20, y-20, x+20, y+20)


paint = Canvas(canvas2)
paint.bind('<Motion>', callback)
paint.pack()

circle = paint.create_oval(0, 0, 0, 0)



#root.config(menu=menubar)
root.mainloop()