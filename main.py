from tkinter import *
import sqlite3
from tkinter import messagebox
import pandas as pd

def mainWindow():
    root=Tk()
    root.title('Data Extraction Tool')
    root.eval('tk::PlaceWindow . center')  
    root.geometry("400x250")
    

    def addData(Id, BilledUnit, Name, Rate, NetAmount, place, port):
        
        if Id == "" or Billed_Unit == "" or Name == "" or Rate == "" or Net_Amount == "" or place == "" or port == "":
            messagebox.showinfo("Error","Please fill all the values")
            return

        # Joining white spaces due to declaration of table names as such (Paltan Bazar - PaltanBazar(table name))
        place = "".join(place.split())

        # places for port1
        if port == '1':
            if place in ["PaltanBazar", "Panbazar"]:
                pass
            else:     
                messagebox.showinfo("Error","No table named {0} in Port {1}".format(place, port))
                return
        elif port == '2':
             if place in ["Jalukbari", "Adabari"]:
                pass
             else:     
                messagebox.showinfo("Error","No table named {0} in Port {1}".format(place, port))
                return
    
        # Last character of port variable specifies the port number (Port1, Port2 etc.)
        conn = sqlite3.connect('Port' + port + '.db')

        # First character of table name should be uppercase
        sql = "INSERT INTO " + place + " (Id, Billed_Unit, Name, Rate, Net_Amount) VALUES (?, ?, ?, ?, ?)"
            
        conn.execute(sql, (Id, BilledUnit, Name, Rate, NetAmount ))

        # Commit the changes to the database
        conn.commit()

        pd.read_sql('select * from ' + place, conn).to_csv('apdcl.csv', mode='a', index=False, header=False)

        conn.close()


    IdEnt=Entry(root,width=30)
    IdEnt.grid(row=0,column=1,padx=20)
    Billed_UnitEnt=Entry(root,width=30)
    Billed_UnitEnt.grid(row=1,column=1)
    NameEnt=Entry(root,width=30)
    NameEnt.grid(row=2,column=1)
    RateEnt=Entry(root,width=30)
    RateEnt.grid(row=3,column=1)
    Net_AmountEnt=Entry(root,width=30)
    Net_AmountEnt.grid(row=4,column=1)
    placeEnt=Entry(root,width=30)
    placeEnt.grid(row=5,column=1)
    PortEnt=Entry(root,width=30)
    PortEnt.grid(row=6,column=1)


    Id = Label(root,text="Id")
    Id.grid(row=0,column=0)
    Billed_Unit = Label(root,text="Billed Unit")
    Billed_Unit.grid(row=1,column=0)
    Name = Label(root,text="Name")
    Name.grid(row=2,column=0)
    Rate = Label(root,text="Rate")
    Rate.grid(row=3,column=0)
    Net_Amount = Label(root,text="Net_Amount")
    Net_Amount.grid(row=4,column=0)
    place = Label(root,text="Place")
    place.grid(row=5,column=0)
    Port = Label(root,text="Port")
    Port.grid(row=6,column=0)

    def getData():

        IdVal = IdEnt.get()
        BilledUnitVal = Billed_UnitEnt.get()
        NameVal = NameEnt.get()
        RateVal = RateEnt.get()
        NetAmountVal = Net_AmountEnt.get()
        PlaceVal = placeEnt.get()
        PortVal = PortEnt.get()

        addData(IdVal, BilledUnitVal, NameVal, RateVal, NetAmountVal, PlaceVal, PortVal)

        # Deleting entries after addData
        IdEnt.delete(0, END)
        Billed_UnitEnt.delete(0, END)
        NameEnt.delete(0, END)
        RateEnt.delete(0, END)
        Net_AmountEnt.delete(0, END)
        placeEnt.delete(0, END)
        PortEnt.delete(0, END)

    submit_btn = Button(root,text="Add Record To Database", command=getData)
    submit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


    root.mainloop()

if __name__ == "__main__":

    mainWindow()