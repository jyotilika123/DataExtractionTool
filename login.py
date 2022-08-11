from tkinter import *
import main
import pandas as pd

users = {
	"Jyoti": "Dimpi"
}

def validateLogin(username, password):
	if users[username] == password:
		# from main.py file
		tkWindow.destroy()
		main.mainWindow()
	else:
		messagebox("Error", "Authentication failed! Please fill the correct Username/Password")
		
#window
tkWindow = Tk()  
tkWindow.geometry('200x100')
tkWindow.eval('tk::PlaceWindow . center')  
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
usernameEntry = Entry(tkWindow)
usernameEntry.grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
passwordEntry = Entry(tkWindow, show='*')
passwordEntry.grid(row=1, column=1)  

def login():
	u = usernameEntry.get()
	p = passwordEntry.get()
	validateLogin(u, p)

#login button
loginButton = Button(tkWindow, text="Login", command=login).grid(row=4, column=0)  

tkWindow.mainloop()