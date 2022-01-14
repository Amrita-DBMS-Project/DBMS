from sqlite3 import connect
from tkinter import *
from tkinter import messagebox
import mysql.connector

class LoginWindow:
    def __init__(self):
        self.win = Tk()
        
        #giving title to the window
        self.win.title("Inventory Management System | Login Page")

        #for size and color of main window
        self.canvas = Canvas(self.win, width=1000, height=600, bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)

        #positioning of the window when program runs
        width = self.win.winfo_screenmmwidth()
        height = self.win.winfo_height()

        x= int(width / 2 - 100 / 2)
        y= int(height/ 6 + 40)

        self.win.geometry("1000x550+"+str(x)+"+"+str(y))

        
    def form(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=290, y=72)


        x,y= 280,65

 
    #now create a login form
        self.label = Label(self.frame, text="User Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y = y + 150)

        self.emlabel = Label(self.frame, text="Enter Email")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y= y + 230)

        self.email = Entry(self.frame, font='Courier 12')
        self.email.place(x=200, y= y + 230)

        self.pslabel = Label(self.frame, text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y+260)

        self.password = Entry(self.frame,show='*', font='Courier 12')
        self.password.place(x=200, y=y+260)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold',
                             command=self.login)
        self.button.place(x=170, y=y+290)

        self.win.mainloop()
    
    def login(self):
        self.un=self.email.get()
        self.pw=self.password.get()
    
        if self.email.get() == "":
            messagebox.showerror("Alert!","Enter Email First")
        elif self.password.get() == "":
            messagebox.showerror("Alert!", "Enter Password first")

        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="pass",database="project")
            mycur = mydb.cursor()
            mycur.execute("select cust_id,cust_password from customer")
            
            result = mycur.fetchall()
            
            flag=0
            for i in result:
                if(i[0]==self.un and i[1]==self.pw):
                    flag=1
                    break
            if(flag==1):
                self.win.destroy()
            else:
                messagebox.showerror("Alert!","Invalid credentials")

    


if __name__ == "__main__":
    x = LoginWindow()
    x.form()
    


