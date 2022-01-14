from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

class registerwindow:
    def __init__(self):
        x=0
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
    
    def formreg(self):
        self.window = Tk()
        self.window.title("Inventory Management System | Customer Registration")
        self.window.geometry('1080x1080')
        self.window.configure(background = "white")
        a = Label(self.window,text = "First Name").grid(row = 0,column = 1)
        b = Label(self.window,text = "Address").grid(row = 1,column = 1)
        c = Label(self.window,text = "Customer Id").grid(row = 2,column = 1)
        d = Label(self.window,text = "Contact Number").grid(row = 3,column = 1)
        f = Label(self.window,text = "Customer_password").grid(row=4,column=1)
        g = Label(self.window,text = "Pincode").grid(row=5,column=1)
        h = Label(self.window,text = "Gender").grid(row=6,column=1)
        i = Label(self.window,text = "DOB (yyyy-mm-dd)").grid(row=7,column=1)
        a1 = Entry(self.window).grid(row = 0,column = 2)
        b1 = Entry(self.window).grid(row = 1,column = 2)
        c1 = Entry(self.window).grid(row = 2,column = 2)
        d1 = Entry(self.window).grid(row = 3,column = 2)
        f1 = Entry(self.window).grid(row = 4,column = 2)
        g1 = Entry(self.window).grid(row = 5,column = 2)
        h1 = Entry(self.window).grid(row = 6,column = 2)
        i1 = Entry(self.window).grid(row = 7,column = 2)
        
        def clicked():
            mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="project")
            mycur = mydb.cursor()
            # mycur.execute('INSERT INTO CUSTOMER VALUES("'+
            # str(c1)+'" ,"'+ str(a1) + '" ,' + d1 + ' ,"' + str(b1) + '" ,' + 
            # g1 + '" ,"' + str(f1) + '" ,"' + str(h1) + '" ,' + """'%s'""",i1)
            mycur.execute("SHOW TABLES")
            result = mycur.fetchall()
            print(result)
            mycur.execute("Select * from CUSTOMER")
            result1 = mycur.fetchall()
            print(result1)
                
                
        btn = ttk.Button(clicked() ,text="Submit").grid(row=9,column=2)
        self.window.mainloop()

if __name__ == "__main__":
    x = registerwindow()
    x.formreg()


