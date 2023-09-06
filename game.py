# author: Grant Bellotti
# date: March 17th, 2023
# file: game.py a Python program that allows users to play the fifteen puzzle game with a UI
# input: user buttons
# output: interactive board
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen

# get the buttons in the order of the board
def getButtons():
    importedButtons = game.get_tiles()
    entrybox = Entry(gui, width=36, borderwidth=5)
    b1 = addButton(gui,entrybox, str(importedButtons[0]))
    b2 = addButton(gui,entrybox, str(importedButtons[1]))
    b3 = addButton(gui,entrybox, str(importedButtons[2]))
    b4 = addButton(gui,entrybox, str(importedButtons[3]))
    b5 = addButton(gui,entrybox, str(importedButtons[4]))
    b6 = addButton(gui,entrybox, str(importedButtons[5]))
    b7 = addButton(gui,entrybox, str(importedButtons[6]))
    b8 = addButton(gui,entrybox, str(importedButtons[7]))
    b9 = addButton(gui,entrybox, str(importedButtons[8]))
    b10 = addButton(gui,entrybox, str(importedButtons[9]))
    b11 = addButton(gui,entrybox, str(importedButtons[10]))
    b12 = addButton(gui,entrybox, str(importedButtons[11]))
    b13 = addButton(gui,entrybox, str(importedButtons[12]))
    b14 = addButton(gui,entrybox, str(importedButtons[13]))
    b15 = addButton(gui,entrybox, str(importedButtons[14]))
    b0 = addButton(gui,entrybox, str(importedButtons[15]))
    shuffle = addButton(gui,entrybox,'shuffle')

    # add buttons to the grid
    buttons =[ b1, b2, b3, b4, 
               b5, b6, b7, b8, 
               b9, b10, b11, b12, 
               b13,b14, b15, b0]
    buttons.append(shuffle)
    return buttons

# creates button
def addButton(gui, entrybox, value):
    font2 = font.Font(family='Helveca', size='25', weight='bold')
    if value == "0":
        return Button(gui, text='', bg='tan', fg='black', font=font2, height=2, width=5, command = lambda: clickButton(entrybox, value))
    elif value == 'shuffle':
        return Button(gui, text=value, bg='white', fg='black', font=font2, height=1, width=10, command = lambda: clickButton(entrybox, value))
    return Button(gui, text=value, bg='coral', fg='black', font=font2, height=2, width=5, command = lambda: clickButton(entrybox, value))

# draws the ui
def drawButtons():
    buttons = getButtons()
    k = 4           
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)
    buttons[len(buttons)-1].grid(row=5, column=1, columnspan=2)

# when each button is clicked
def clickButton(entrybox, value):
    if value == 'shuffle':
        shuffleButtons()
    else:
        game.update(int(value))
        if game.is_valid_move(int(value)):
            drawButtons()
            if game.is_solved():
                print('Congratulations!!')

#shuffle the boards
def shuffleButtons():
    game.shuffle()
    drawButtons()

def fifteen(gui):   
    # name the gui window
    gui.title("Fifteen")

    drawButtons()

# main program
# create the main window
if __name__ == '__main__':
    game = Fifteen()
    game.shuffle()

    gui = Tk()
    fifteen(gui)

    # update the window
    gui.mainloop()