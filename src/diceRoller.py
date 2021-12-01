import tkinter
from PIL import Image, ImageTk
import random

#main window of the app
dieWindow = tkinter.Tk()
dieWindow.geometry('600x600')
dieWindow.title('Dice Roller')

blankLine = tkinter.Label(dieWindow, text = '')
blankLine.pack()

#adds text label to the widget
heading = tkinter.Label(dieWindow, text = 'Press the button to roll the die')
heading.pack()

#loads images and chooses at random an image of a die
mainDie = ['Die1.png', 'Die2.png', 'Die3.png', 'Die4.png', 'Die5.png', 'Die6.png', ]
dieImage = ImageTk.PhotoImage(Image.open(random.choice(mainDie)))

showDie = tkinter.Label(dieWindow, image=dieImage)
showDie.image = dieImage
showDie.pack(expand = True)

#function to reroll the die
def reroll_die():
    newRoll =  ImageTk.PhotoImage(Image.open(random.choice(mainDie)))
    showDie.configure(image = newRoll)
    showDie.image = newRoll

#making and defining the button
rerollBtn = tkinter.Button(dieWindow, text = 'Reroll', fg='green', command = reroll_die)
rerollBtn.pack(expand = True)

#calls Tk() at the top and keeps the window open
dieWindow.mainloop()
