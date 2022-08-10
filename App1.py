from cProfile import label
from tkinter import*
root=Tk()
root.minsize(height=500,width=900)
def tab2():
                                                    
    Label1.destroy()
    button1.destroy()
    Label2=label(root,text='THIS IS SECOND TAB',font=('Times_New_roman',25))
    Label2.pack()
def back():
    Label2=label(root,text='THIS IS SECOND TAB',font=('Times_New_roman',25))
    Label2.pack()
    Label2.destroy()
    button2.destroy()

button2=Button(root,text='BACK',font=('Times New Roman',25),command='back',activebackground='blue')
button2. pack(side=BOTTOM)
Label1=Label(root,text='THIS IS FIRST TAB',font=('Times_New_Roman',25))
Label1.pack()
button1=Button(root,text='NEXT',font=('Times New Roman',25),command=tab2,activebackground='blue')
button1.pack(side=BOTTOM)
                                                
root.mainloop()

