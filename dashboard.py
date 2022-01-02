from tkinter import *

class DashboardWindow:
    def __init__(self):
        self.win = Tk()
        
        #giving title to the window
        self.win.title("Inventory Management System")

        #for size and color of main window
        self.canvas = Canvas(self.win, width=1000, height=600, bg='white')
        self.canvas.pack(expand=YES,fill=BOTH)

        #positioning of the window when program runs
        width = self.win.winfo_screenmmwidth()
        height = self.win.winfo_height()

        x= int(width / 2 - 100 / 2)
        y= int(height/ 6 - 0)

        self.win.geometry("1000x500+"+str(x)+"+"+str(y))



if __name__ == "__main__":
    x = DashboardWindow()
    


