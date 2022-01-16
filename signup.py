from tkinter import *
from tkinter import messagebox
import mysql.connector
import login

class SignupWindow:
    def __init__(self):
        self.win = Tk()
        
        #giving title to the window
        self.win.title("Inventory Management System | Signup Page")

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
        self.frame = Frame(self.win, height=410, width=500)
        self.frame.place(x=250, y=65)


        x,y= 100,-140

 
    #now create a login form
        self.label = Label(self.frame, text="User Sign-Up")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=160, y = y + 150)

        self.nlabel = Label(self.frame, text="Enter Name")
        self.nlabel.config(font=("Courier", 12, 'bold'))
        self.nlabel.place(x=50, y= y + 230)

        self.name = Entry(self.frame, font='Courier 12')
        self.name.place(x=250, y= y + 230)

        self.emlabel = Label(self.frame, text="Enter Email Address")
        self.emlabel.config(font=("Courier", 12, 'bold'))
        self.emlabel.place(x=50, y=y+260)

        self.email = Entry(self.frame,font='Courier 12')
        self.email.place(x=250, y=y+260)

        self.pwlabel = Label(self.frame, text="Enter Password")
        self.pwlabel.config(font=("Courier", 12, 'bold'))
        self.pwlabel.place(x=50, y=y+290)

        self.password = Entry(self.frame,show='*', font='Courier 12')
        self.password.place(x=250, y=y+290)

        self.pnlabel = Label(self.frame, text="Enter Phone number")
        self.pnlabel.config(font=("Courier", 12, 'bold'))
        self.pnlabel.place(x=50, y=y+320)

        self.phone = Entry(self.frame,font='Courier 12')
        self.phone.place(x=250, y=y+320)

        self.glabel = Label(self.frame, text="Select Gender")
        self.glabel.config(font=("Courier", 12, 'bold'))
        self.glabel.place(x=50, y=y+350)

        self.gender = IntVar()

        Radiobutton(self.frame, text="Male",font=("Courier", 12, 'bold'), variable = self.gender,value=1).place(x=200, y=y+350)

        Radiobutton(self.frame, text="Female",font=("Courier", 12, 'bold'), variable = self.gender,value=2).place(x=280, y=y+350)

        Radiobutton(self.frame, text="Other",font=("Courier", 12, 'bold'), variable = self.gender,value=3).place(x=380, y=y+350)  

        self.addlabel = Label(self.frame, text="Enter Address")
        self.addlabel.config(font=("Courier", 12, 'bold'))
        self.addlabel.place(x=50, y=y+380)
        
        self.address = Entry(self.frame,font='Courier 12',justify="left")
        self.address.place(x=250, y=y+380,height=40)

        self.pclabel = Label(self.frame, text="Enter Pincode")
        self.pclabel.config(font=("Courier", 12, 'bold'))
        self.pclabel.place(x=50, y=y+430)
        
        self.pincode = Entry(self.frame,font='Courier 12',justify="left")
        self.pincode.place(x=250, y=y+430)

        self.doblabel = Label(self.frame, text="Enter DOB")
        self.doblabel.config(font=("Courier", 12, 'bold'))
        self.doblabel.place(x=50, y=y+460)
        
        self.date = Entry(self.frame,font='Courier 12',justify="left")
        self.date.place(x=280, y=y+460,width=35)
        self.month = Entry(self.frame,font='Courier 12',justify="left")
        self.month.place(x=330, y=y+460,width=35)
        self.year = Entry(self.frame,font='Courier 12',justify="left")
        self.year.place(x=380, y=y+460,width=45)


        self.button = Button(self.frame, text="Signup", font='Courier 15 bold',
                             command=self.signup)
        self.button.place(x=215, y=y+500)


        self.win.mainloop()
    
    def signup(self):
        self.un=str(self.email.get())
        print(self.un)
        self.pw=str(self.password.get())
        self.nm=str(self.name.get())
        self.gn=str(self.gender.get())
        self.ph=str(self.phone.get())
        self.pc=str(self.pincode.get())
        self.adr=str(self.address.get())
        self.dob=str(self.year.get())+"-"+str(self.month.get())+"-"+str(self.date.get())
        
        
        if self.name.get() == "" :
            messagebox.showerror("Alert!", "Enter Your Name First")    

        elif (("@" not in self.email.get()) or (".com" not in self.email.get()) or (self.email.get() == "")):
            messagebox.showerror("Alert!", "Enter Valid Email")

        elif self.password.get() == "":
            messagebox.showerror("Alert!", "Enter Password first")

        elif ((self.phone.get()).isalpha() or (len(self.phone.get())!=10)) :
            messagebox.showerror("Alert!", "Enter Valid Phone Number")

        elif (self.gn=="0") :
            messagebox.showerror("Alert!", "Please select a gender")
                    
        elif self.address.get() == "" :
            messagebox.showerror("Alert!", "Enter Your Address")
        
        elif ((self.pincode.get()).isalpha() or (len(self.pincode.get())!=6)):
            messagebox.showerror("Alert!", "Enter a Valid Pincode")
        
        elif((int(self.date.get())>31) or (len(self.date.get())!=2)):
            messagebox.showerror("Alert","Please give a valid date")
        elif((int(self.month.get())>12) or (len(self.month.get())!=2)):
            messagebox.showerror("Alert","Please give a valid month")
        elif((len(self.year.get())!=4)):
            messagebox.showerror("Alert","Please give a valid year")
        
        else:
            if(self.gn=="1"):
                self.gn="M"
            if(self.gn=="2"):
                self.gn="F"
            if(self.gn=="3"):
                self.gn="O"
            print("before connector")
            self.mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="project")
            print("after connector")
            self.mycursor = self.mydb.cursor()
            print("after cursor")

            tab="INSERT INTO CUSTOMER(CUST_ID,CUST_NAME,CUST_PHONE,CUST_ADDRESS,CUST_PINCODE,CUST_PASSWORD,CUST_GENDER,CUST_DOB) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(self.email.get(),self.name.get(),self.phone.get(),self.address.get(),self.pincode.get(),self.password.get(),self.gn,self.dob)
            self.mycursor.execute(tab,val)
    
            self.mydb.commit()

            x= login.LoginWindow()
            x.form()
    


if __name__ == "__main__":
    x = SignupWindow()
    x.form()