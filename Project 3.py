from tkinter import *

def submit():
    username = entry.get() #gets entry text
    print("Hello "+username)

def delete():
    entry.delete(0,END) #deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) #delete last character

window = Tk()
window.title("user input")
label = Label(window,text="username: ")
label.config(font=("Consolas",30))
label.pack(side=LEFT)

submit = Button(window,text="submit",command=submit)
submit.pack(side = RIGHT)

delete = Button(window,text="delete",command=delete)
delete.pack(side = RIGHT)

backspace = Button(window,text="backspace",command=backspace)
backspace.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Ink Free',50)) #change font
entry.config(bg='#111111') #background
entry.config(fg='#00FF00') #foreground
entry.config(width=10) #width displayed in characters
#entry.insert(0,'Spongebob') #set default text
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(show='*') #replace characters shown with x character
entry.pack()
window.mainloop()
