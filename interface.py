#!/usr/bin/python
from tkinter import *
top = Tk()

frame = Frame(top)
frame.pack()

CardNumberLabel = Label(frame, text="Card Number").grid(row=1, column=1)
CardNumberEntry = Entry(frame, bd=30).grid(row=1, column=2)

CVVLabel = Label(frame, text="CVV").grid(row=2, column=1)
CVVEntry = Entry(frame, bd=30).grid(row=2, column=2)

CardDateLabel = Label(frame, text="Card Date").grid(row=3, column=1)
CardDateEntry = Entry(frame, bd=30).grid(row=3, column=2)

Button = Button(frame, text = "send", bd=15).grid(row=4, column=2)

top.mainloop()









print ("HELLO!! OMG it's working!!!""")
