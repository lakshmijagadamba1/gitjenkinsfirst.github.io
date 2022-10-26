# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:52:54 2019

@author: Dr P.V.S.L Jagadamba
"""

from tkinter import *
 
root = Tk()
root.title("Calculator")
# So that it becomes of fixed size
root.config(bg="grey")
root.resizable(0, 0)
# So that it remains on top of the screen
root.wm_attributes("-topmost", 1)
 
# Label
Label1 = Label(root, text = "CALCULATOR",fg="yellow",bg="grey", font=14)
Label1.grid(row=0, column=0, columnspan=8)

 
# Variables
equa = ""
equation = StringVar()
 
calculation = Label(root, textvariable = equation, borderwidth=2, relief=SOLID, width=20,bg='powder blue', font=20 )
 
calculation.grid(row=2, column=0, columnspan=6) 
def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
 
def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""
 
def ClearPress():
    global equa
    equa = ""
    equation.set("")
#Button_effects={ fg="yellow",font=14} 
Button0 = Button(root, text="0", command = lambda:btnPress(0))
Button0.config(fg="White",font=("Bold", 14), bg="orange", borderwidth=5, relief=RIDGE)
Button0.grid(row = 6, column = 2, padx=10, pady=10)

Button1 = Button(root, text="1", command = lambda:btnPress(1), bg="orange", borderwidth=5, font=18, relief=SUNKEN)
Button1.grid(row = 3, column = 1, padx=10, pady=10)

Button2 = Button(root, text="2", command = lambda:btnPress(2), bg="orange", borderwidth=5, font=18, relief=RAISED)
Button2.grid(row = 3, column = 2, padx=10, pady=10)

Button3 = Button(root, text="3", command = lambda:btnPress(3), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button3.grid(row = 3, column = 3, padx=10, pady=10)

Button4 = Button(root, text="4", command = lambda:btnPress(4), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button4.grid(row = 4, column = 1, padx=10, pady=10)

Button5 = Button(root, text="5", command = lambda:btnPress(5), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button5.grid(row = 4, column = 2, padx=10, pady=10)

Button6 = Button(root, text="6", command = lambda:btnPress(6), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button6.grid(row = 4, column = 3, padx=10, pady=10)

Button7 = Button(root, text="7", command = lambda:btnPress(7), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button7.grid(row = 5, column = 1, padx=10, pady=10)

Button8 = Button(root, text="8", command = lambda:btnPress(8), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button8.grid(row = 5, column = 2, padx=10, pady=10)

Button9 = Button(root, text="9", command = lambda:btnPress(9), bg="orange", borderwidth=1, font=18, relief=SOLID)
Button9.grid(row = 5, column = 3, padx=10, pady=10)

Plus = Button(root, text="+", command = lambda:btnPress("+"), bg="orange", borderwidth=1, font=20, relief=SOLID)
Plus.grid(row = 3, column = 4, padx=10, pady=10)

Minus = Button(root, text="-", command = lambda:btnPress("-"), bg="orange", borderwidth=1, font=20, relief=SOLID)
Minus.grid(row = 4, column = 4, padx=10, pady=10)

Multiply = Button(root, text="*", command = lambda:btnPress("*"), bg="orange", borderwidth=1, font=20, relief=SOLID)
Multiply.grid(row = 5, column = 4, padx=10, pady=10)

Divide = Button(root, text="/", command = lambda:btnPress("/"), bg="orange", borderwidth=1, font=20, relief=SOLID)
Divide.grid(row = 6, column = 4, padx=10, pady=10)

Equal = Button(root, text="=", command = EqualPress, bg="orange", borderwidth=1, font=20, relief=SOLID)
Equal.grid(row=6, column=3, padx=10, pady=10)

Clear = Button(root, text="C", command = ClearPress, bg="orange", borderwidth=1, font=20, relief=SOLID)
Clear.grid(row = 6, column = 1, padx=10, pady=10)
 
root.mainloop()