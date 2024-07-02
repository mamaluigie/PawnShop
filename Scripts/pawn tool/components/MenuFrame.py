from tkinter import *

def testButtonClick():
    print("button was clicked")

def MenuFrame(frame, height, width):

    menu_box = Frame(frame, height=height, width=width, bg="white")
    menu_box.grid(row=1,padx=10, pady=10)
    menu_box.grid_propagate(False)

    button = Button(menu_box, text="Calculations", command=testButtonClick, bg="white")
    button.grid()

    return menu_box
