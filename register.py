from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class registerwindow:
    global mydb,mycur
    
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="project")
    mycur = mydb.cursor()
    def __init__(self):
        self.window = Tk()
        self.window.title("Inventory Management System | Customer Registration")
        self.canvas = Canvas(self.window, width=1000, height=600, bg='white')
        # self.canvas.pack(expand=YES,fill=BOTH)

        #positioning of the window when program runs
        width = self.window.winfo_screenmmwidth()
        height = self.window.winfo_height()

        x= int(width / 2 - 100 / 2)
        y= int(height/ 6 + 40)

        self.window.geometry("1000x550+"+str(x)+"+"+str(y))
        self.window.resizable(width=False,height=False)
        self.flag = 0
        # self.window = Tk()
        # self.window.title("Inventory Management System | Customer Registration")
        # self.canvas = Canvas(self.window, width=1080, height=1080, bg='white')
        # self.canvas.pack(expand=YES,fill=BOTH)
        # width = self.window.winfo_screenmmwidth()
        # height = self.window.winfo_height()
        # x= int(width / 2 - 100 / 2)
        # y= int(height/ 6 + 40)
        # self.window.geometry("1000x550+"+str(x)+"+"+str(y))
        # self.window.resizable(True,True)
    def clicked(self):
        # mycur.execute('INSERT INTO CUSTOMER VALUES("'+
        # str(c1)+'" ,"'+ str(a1) + '" ,' + str(d1) + ' ,"' + str(b1) + '" ,' + 
        # str(g1) + '" ,"' + str(f1) + '" ,"' + str(h1) + '" ,' + "'2002-10-10'")
        if self.flag==0:
            self.flag = 1
            print("Seda")
        else:
            mycur.execute(f'INSERT INTO CUSTOMER VALUES("{self.c1.get()}","{self.a1.get()}",{self.d1.get()},"{self.b1.get()}",{self.g1.get()},"{self.f1.get()}","{self.h1.get()}","{self.i1.get()}")')
            mydb.commit()
            print("asdasdasdasda")
            result = mycur.fetchall()
            print(result)
            self.flag += 1
        # print(f'INSERT INTO CUSTOMER VALUES("{c1}","{a1}",{d1},"{b1}",{g1},"{f1}","{h1}","{i1}")')
        #mycur.execute("SHOW TABLES")
        # result = mycur.fetchall()
        # print(result)

        mycur.execute("Select * from CUSTOMER")
        result1 = mycur.fetchall()
        print(result1)

    def formreg(self):
        
        self.a = Label(self.window,text = "First Name").grid(row = 0,column = 3)
        self.b = Label(self.window,text = "Address").grid(row = 1,column = 3)
        self.c = Label(self.window,text = "Customer Id").grid(row = 2,column = 3)
        self.d = Label(self.window,text = "Contact Number").grid(row = 3,column = 3)
        self.f = Label(self.window,text = "Customer_password").grid(row=4,column=3)
        self.g = Label(self.window,text = "Pincode").grid(row=5,column=3)
        self.h = Label(self.window,text = "Gender").grid(row=6,column=3)
        self.i = Label(self.window,text = "DOB (yyyy-mm-dd)").grid(row=7,column=3)
        self.a1 = Entry(self.window).grid(row = 0,column = 8)
        self.b1 = Entry(self.window).grid(row = 1,column = 8)
        self.c1 = Entry(self.window).grid(row = 2,column = 8)
        self.d1 = Entry(self.window).grid(row = 3,column = 8)
        self.f1 = Entry(self.window).grid(row = 4,column = 8)
        self.g1 = Entry(self.window).grid(row = 5,column = 8)
        self.h1 = Entry(self.window).grid(row = 6,column = 8)
        self.i1 = Entry(self.window).grid(row = 7,column = 8)
        
        self.btn = ttk.Button(command=self.clicked ,text="Submit").grid(row=8,column=4)
        self.window.mainloop()

    
if __name__ == "__main__":
    x = registerwindow()
    x.formreg()


