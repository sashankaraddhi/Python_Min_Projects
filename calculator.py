from tkinter import *
import operator

root = Tk()
root.title("calculator")
root.geometry("400x400")
root.configure(bg="black")
# entry box 

entry=Entry(root, width=30, borderwidth=5)
entry.place(x=10, y=10)

#function

def click(a):
    return entry.insert(END,a)
    
#button

button=Button(root,text ="1",width=5,command=lambda:click(1),bg="WHITE",fg="black"  )
button.place(x=10 , y=60)

button2=Button(root,text ="2",width=5,command=lambda:click(2),bg="WHITE",fg="black")
button2.place(x=90, y=60)       

button3=Button(root,text ="3",width=5 ,command =lambda:click(3),bg="WHITE",fg="black")
button3.place(x=170 , y=60)       

button4=Button(root,text ="4",width=5 ,command =lambda:click(4),bg="WHITE",fg="black")
button4.place(x= 10 , y= 120)

button5=Button(root,text ="5",width=5 ,command =lambda:click(5),bg="WHITE",fg="black")
button5.place(x=90 , y=120)

button6=Button(root,text ="6",width=5 ,command =lambda:click(6),bg="WHITE",fg="black") 
button6.place(x = 170 ,y = 120)

button7=Button(root,text ="7",width=5 ,command =lambda:click(7),bg="WHITE",fg="black")
button7.place(x= 10, y=180)

button8=Button(root,text ="8",width=5 ,command =lambda:click(8),bg="WHITE",fg="black")
button8.place(x=90 , y=180)

button9=Button(root,text ="9",width=5,command =lambda:click(9),bg="WHITE",fg="black")
button9.place(x=170 , y=180)

button10=Button(root,text ="0",width=5,command =lambda:click(0),bg="WHITE",fg="black")
button10.place(x=10 , y=240)

# operator 

def add():  
   global i, operator
   i = int(entry.get())
   operator = "addition"
   entry.delete(0, END)

button11=Button(root,text ="+",width=5,command=add )
button11.place(x=170 , y=240)

def sub():
    global i, operator
    i = int (entry.get())
    operator = "subtraction"
    entry.delete(0, END)

button12=Button(root,text ="-",width=5,command=sub )
button12.place(x=90 , y=240)

def mul():
   global i, operator
   i = int(entry.get())
   operator = "multiplication"
   entry.delete(0, END)

button13=Button(root,text ="*",width=5,command=mul )
button13.place(x=170 , y=300)

def div():
    global i, operator
    i = int(entry.get())
    operator = "division"
    entry.delete(0, END)

button14=Button(root,text ="/",width=5,command=div )
button14.place(x=10 , y=300)

def equal():
    global i, operator
    second = int(entry.get())
    entry.delete(0, END)
    if operator == "addition":
        entry.insert(0, i + second)
    elif operator == "subtraction":
        entry.insert(0, i - second)
    elif operator == "multiplication":
        entry.insert(0, i * second)
    elif operator == "division":
        if second != 0:
            entry.insert(0, i / second)
        else:
            entry.insert(0, "Error")


button16=Button(root,text ="=",width=5,command=equal,bg="WHITE",fg="black" )
button16.place(x=90 , y=300)

def clear():
    entry.delete(0,END)

button15=Button(root,text ="Clear",width=5,command=clear,bg="red",fg="white" )
button15.place(x=10 , y=360)


root.mainloop()