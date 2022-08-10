from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root=Tk()
root.title('Codemy.com-Learn To Code!')
root.geometry("400x200")



f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)


f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

submit_btn = Button(root,text="Add Record To Database")
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


root.mainloop()