from cProfile import label
from tkinter import *
from tkinter import messagebox
import mysql.connector
import signup
import cust_dash
class LoginWindow:
    def __init__(self):
        self.win = Tk()
        
        #giving title to the window
        self.win.title("Inventory Management System | Login Page")

        #for size and color of main window
        self.canvas = Canvas(self.win, width=1000, height=600, bg='black')
        self.canvas.pack(expand=YES,fill=BOTH)

        #positioning of the window when program runs
        width = self.win.winfo_screenmmwidth()
        height = self.win.winfo_height()

        x= int(width / 2 - 100 / 2)
        y= int(height/ 6 + 40)

        self.win.geometry("1000x550+"+str(x)+"+"+str(y))
        self.win.resizable(width=False,height=False)

        
    def form(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=290, y=72)


        x,y= 280,65
    #now create a login form

        self.label = Label(self.frame, text="User Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y = y + 10)

        self.emlabel = Label(self.frame, text="Enter Email")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y= y + 80)

        self.email = Entry(self.frame, font='Courier 12')
        self.email.place(x=200, y= y + 80)

        self.pslabel = Label(self.frame, text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y+110)

        self.password = Entry(self.frame,show='*', font='Courier 12')
        self.password.place(x=200, y=y+110)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold',
                             command=self.login)
        self.button.place(x=190, y=y+150)

        self.label = Label(self.frame,text="New user?")
        self.label.config(font=("Courier", 10, 'bold'))
        self.label.place(x=150, y = y + 215)

        self.button = Button(self.frame, text="Signup", font='Courier 10 bold',
                             command=self.sign)
        self.button.place(x=230, y=y+210,width=55)

        self.win.mainloop()
    def sign(self):
        x= signup.SignupWindow()
        x.form()
    
    def login(self):
        self.un=self.email.get()
        self.pw=self.password.get()
    
        if self.email.get() == "":
            messagebox.showerror("Alert!","Enter Email First")
        elif self.password.get() == "":
            messagebox.showerror("Alert!", "Enter Password first")

        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="project")
            mycur = mydb.cursor()
            mycur.execute("select cust_id,cust_password from customer")
            
            result = mycur.fetchall()
            
            flag=0
            for i in result:
                if(i[0]==self.un and i[1]==self.pw):
                    flag=1
                    break
            if(flag==1):
                # self.win.destroy()
                cust_dash.login_user()
            else:
                messagebox.showerror("Alert!","Invalid credentials")

    


if __name__ == "__main__":
    x = LoginWindow()
    x.form()
    


