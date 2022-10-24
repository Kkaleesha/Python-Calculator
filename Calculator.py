from tkinter import*

#Functions
def add():
    a = E1.get()
    b = E2.get()
    z = float(a)+float(b)
    L1.config(text=z)

def sub():
    a = E1.get()
    b = E2.get()
    c = float(a)-float(b)
    L1.config(text=c)

def mul():
    a = E1.get()
    b = E2.get()
    c = float(a)*float(b)
    L1.config(text=c)

def div():
    a = E1.get()
    b = E2.get()
    c = float(a)/float(b)
    L1.config(text=c)

def c():
    E1.delete(0,END)
    E2.delete(0,END)

#window
window = Tk()
window.title("Calculator")
window.config(background="#282A35")
window.iconbitmap(r"C:\Users\SAMSUNG\Desktop\Python Projects\Python Calculator\calculator.ico")

#frame 1
F1 = Frame(window)
F1.pack(fill=X)
F1.config(background="#e38056")
E1 = Entry(F1)
E1.pack(side=LEFT,padx=5,pady=5)
E1.config(background="#f0ba4f")
E2 = Entry(F1)
E2.pack(side=RIGHT)
E2.config(background="#f0ba4f")

#Output Field
L1 = Label(window,text=0)
L1.pack(fill=X,padx=0,pady=0)
L1.config(background="#b2d156")

#Add Buttons
B1 = Button(window,text=" + ",command=add)
B1.pack(side=LEFT,pady=5)
B1.config(width=5,background="#215eb5")

#sub button
B2 = Button(window,text=" - ",command=sub)
B2.pack(side=LEFT,pady=5,padx=5)
B2.config(width=5,background="#215eb5")

#mul button
B3 = Button(window,text=" * ",command=mul)
B3.pack(side= LEFT,pady=5,padx=5)
B3.config(width=5,background="#215eb5")

#division
B4 = Button(window,text=" / ",command=div)
B4.pack(side=LEFT,padx=5,pady=5)
B4.config(width=5,background="#215eb5")

#c button
B5 = Button(window,text=" C ",command=c)
B5.pack(side=LEFT,padx=5,pady=5)
B5.config(width=5,background="#215eb5")

window.mainloop()