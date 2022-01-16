from datetime import date
from tkinter.tix import COLUMN
import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="project"
)

mycursor = mydb.cursor(buffered=True)


def login_user():

    if 1 == 1:
        def items():
            inventory_window = Toplevel(newWindow)
            item_id = Label(inventory_window, text='ITEM ID')
            item_id.grid(row=0, column=0)

            iname = Label(inventory_window, text='ITEM NAME')
            iname.grid(row=0, column=1)

            idec = Label(inventory_window, text='ITEM CATEGORY')
            idec.grid(row=0, column=2)

            ip = Label(inventory_window, text='ITEM PRICE')
            ip.grid(row=0, column=3)

            mycursor.execute("select * from ITEMS")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(inventory_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            btn = Button(inventory_window, text="Add items", command=lambda: add_product())
            btn.grid(row=i + 2, column=1)

            btn = Button(inventory_window, text="Delete items", command=lambda: remove_product())
            btn.grid(row=i + 2, column=2)

            btn = Button(inventory_window, text="Update items", command=lambda: update_product())
            btn.grid(row=i + 2, column=3)
        
        def update_product():
            userWindow = Toplevel(newWindow)

            iid = Label(userWindow, text='ITEM ID')
            iid.grid(row=0, column=0)

            what = Label(userWindow, text="WHAT TO UPDATE")
            what.grid(row=0,column=1)

            value1 = what = Label(userWindow, text="UPDATE VALUE")
            value1.grid(row=0,column=2)

            iid1 = Entry(userWindow)
            iid1.grid(row=1,column=0)

            update_what = Entry(userWindow)
            update_what.grid(row=1,column=1)

            value = Entry(userWindow)
            value.grid(row=1,column=2)

            update_into = Button(userWindow, text='UPDATE',
                                 command=lambda: update_values_product(update_what.get(),value.get(),iid1.get()))
            update_into.grid(row=2,column=9)
        
        def update_values_product(update_what,value,uid):
            # val = (update_what,value,uid)
            # query = 'UPDATE CUSTOMER SET %s = %s WHERE CUST_ID = %s'
            mycursor.execute("UPDATE ITEMS SET %s='%s' WHERE ITEM_ID='%s'" % (update_what,value,uid))
            mydb.commit() 

        def add_product():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("500x300")
            l1 = Label(insertWindow, text="Enter Item Name")
            l1.place(x=20, y=20)

            l1 = Label(insertWindow, text="Enter Item category")
            l1.place(x=20, y=80)

            l1 = Label(insertWindow, text="Enter Item Price")
            l1.place(x=20, y=140)

            l1 = Label(insertWindow, text="Enter ID")
            l1.place(x=20, y=200)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            e2 = Entry(insertWindow)
            e2.place(x=200, y=80)

            e3 = Entry(insertWindow)
            e3.place(x=200, y=140)

            e4 = Entry(insertWindow)
            e4.place(x=200, y=200)

            insert_into = Button(insertWindow, text='INSERT INTO ITEMS',
                                 command=lambda: insert_values_inventory(e4.get(), e1.get(), e2.get(), e3.get()))
            insert_into.place(x=300, y=270)

        def insert_values_inventory(iname, idesc, iprice, iqu):
            mycursor.execute('insert into items(item_id, item_name, item_category, item_price)'
                             ' values(%s, %s, %s, %s)', (iname, idesc, iprice, iqu))
            mydb.commit()

        def remove_product():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("300x300")
            l1 = Label(insertWindow, text="Enter Item ID to be deleted")
            l1.place(x=20, y=20)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            insert_into = Button(insertWindow, text='DELETE',
                                 command=lambda: delete_product(e1.get()))
            insert_into.place(x=60, y=80)

        def delete_product(item_id):
            mycursor.execute("DELETE FROM ITEMS WHERE ITEM_ID='%s'" % (item_id))
            mydb.commit()

        def order_lists():
            order_window = Toplevel(newWindow)

            order_id = Label(order_window, text='ORDER ID')
            order_id.grid(row=0, column=0)

            od = Label(order_window, text='ORDER STATUS')
            od.grid(row=0, column=1)

            tp = Label(order_window, text='ITEM ID')
            tp.grid(row=0, column=2)

            ui = Label(order_window, text='CUSTOMER ID')
            ui.grid(row=0, column=3)

            cp = Label(order_window, text='CUSTOMER PHONE')
            cp.grid(row=0, column=4)

            c_add = Label(order_window, text='CUSTOMER ADDRESS')
            c_add.grid(row=0, column=5)

            s_id = Label(order_window, text='SELLER ID')
            s_id.grid(row=0, column=6)

            mycursor.execute("SELECT * FROM ORDERS")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(order_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            lbl = Label(order_window, text="Enter Order ID to view")
            lbl.grid(row=i + 3, column=1)
            order_entry = Entry(order_window, width=15)
            order_entry.grid(row=i + 3, column=2)
            btn = Button(order_window, text="submit", command=lambda: show_order(order_entry.get()))
            btn.grid(row=i + 3, column=3)

            create_user = Button(order_window, text='ADD ORDER', command=lambda: insert_order())
            create_user.grid(row=i + 3, column=0)

        def show_order(oid):
            so_window = Toplevel(newWindow)
            oi = Label(so_window, text='ORDER ID')
            oi.grid(row=0, column=0)

            ii = Label(so_window, text='ORDER STATUS')
            ii.grid(row=0, column=1)

            qo = Label(so_window, text='ITEM ID')
            qo.grid(row=0, column=2)

            it_nm = Label(so_window, text='CUST ID')
            it_nm.grid(row=0, column=3)

            it_ds = Label(so_window, text='CUST PHONE')
            it_ds.grid(row=0, column=4)

            ip = Label(so_window, text='CUST ADDRESS')
            ip.grid(row=0, column=5)

            s_id = Label(so_window, text='SELLER ID')
            s_id.grid(row=0, column=6)

            # mycursor.execute("SELECT * FROM ORDERS")
            mycursor.execute(
                "select *"
                " from ORDERS"
                " where order_id=%s", (oid,)
            )
            l = 1
            for x in mycursor.fetchall():
                for y in range(len(x)):
                    e = Entry(so_window, width=10, fg='blue')
                    e.grid(row=l, column=y)
                    e.insert(END, x[y])
                l = l + 1

            lbl = Label(so_window, text="Enter Order ITEM ID to be completed")
            lbl.grid(row=l + 1, column=3)
            order_update = Entry(so_window, width=10)
            order_update.grid(row=l + 2, column=3)
            btn = Button(so_window, text="submit", command=lambda: update_inventory(order_update.get()))
            btn.grid(row=l + 3, column=3)

        def insert_order():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("400x300")

            oi = Label(insertWindow, text='ORDER ID')
            oi.grid(row=0, column=0)
            oi1 = Entry(insertWindow)
            oi1.grid(row=1,column=0)

            ii = Label(insertWindow, text='ORDER STATUS')
            ii.grid(row=0, column=1)
            ii1 = Entry(insertWindow)
            ii1.grid(row=1,column=1)

            qo = Label(insertWindow, text='ITEM ID')
            qo.grid(row=0, column=2)
            qo1 = Entry(insertWindow)
            qo1.grid(row=1,column=2)

            it_nm = Label(insertWindow, text='CUST ID')
            it_nm.grid(row=0, column=3)
            it_nm1 = Entry(insertWindow)
            it_nm1.grid(row=1,column=3)

            it_ds = Label(insertWindow, text='CUST PHONE')
            it_ds.grid(row=0, column=4)
            it_ds1 = Entry(insertWindow)
            it_ds1.grid(row=1,column=4)

            ip = Label(insertWindow, text='CUST ADDRESS')
            ip.grid(row=0, column=5)
            ip1 = Entry(insertWindow)
            ip1.grid(row=1,column=5)

            s_id = Label(insertWindow, text='SELLER ID')
            s_id.grid(row=0, column=6)
            s_id1 = Entry(insertWindow)
            s_id1.grid(row=1,column=6)

            mycursor.execute("SELECT * FROM ORDERS")

            insert_into = Button(insertWindow, text='ADD',
                                 command=lambda: insert_values_orders(oi1.get(), ii1.get(), qo1.get(),it_nm1.get(),it_ds1.get(),ip1.get(),s_id1.get() ))
            insert_into.grid(row=2,column=5)
            

        def insert_values_orders(oi,ii,qo,it,it_ds,ip,s_id):
            odate = date.today()
            print(odate)
            mycursor.execute('INSERT INTO orders(order_id, order_status, item_id, cust_id, cust_phone, cust_address, seller_id) VALUES(%s,%s,%s,%s,%s,%s,%s)',
                             (oi,ii,qo,it,it_ds,ip,s_id))
            mydb.commit()

        item_id_list = []
        quantity_ordered_list = []

        def items_insert():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("600x300")
            l1 = Label(insertWindow, text="Enter ITEM ID")
            l1.place(x=20, y=20)

            a = Entry(insertWindow)
            a.place(x=150, y=20)

            l2 = Label(insertWindow, text="Enter QUANTITY ORDERED")
            l2.place(x=20, y=60)

            b = Entry(insertWindow)
            b.place(x=200, y=60)

            items = Button(insertWindow, text="Submit", command=lambda: fetch_item_id(a.get(), b.get()))
            items.place(x=20, y=150)

        def fetch_item_id(item_id, quantity_ordered):
            item_id_list.append(item_id)
            quantity_ordered_list.append(quantity_ordered)

        def update_inventory(order_item_id):
            mycursor.execute('select item_id, order_id, order_status from orders where order_item_id=%s',
                             (order_item_id,))
            item_id, order_id, quantity_ordered = mycursor.fetchall()[0]

            # mycursor.execute('select quantity_in_stock from product_inventory where item_id = %s', (item_id,))
            # quantity_in_stock = mycursor.fetchall()[0][0]

            # if quantity_in_stock >= quantity_ordered:
            #     mycursor.execute(
            #         'update product_inventory set quantity_in_stock = quantity_in_stock - %s where item_id = %s',
            #         (quantity_ordered, item_id,))
            #     mydb.commit()

            #     mycursor.execute('select count(*) from contain where order_id=%s', (str(order_id),))
            #     rows = mycursor.fetchall()[0][0]
            #     if rows == 1:
            #         mycursor.execute('delete from orders where order_id=%s', (order_id,))
            #         mydb.commit()
            #     mycursor.execute('delete from contain where order_item_id=%s', (order_item_id,))
            #     mydb.commit()

            # else:
            #     MessageBox.showwarning('Error', 'Required quantity not available')

            # mycursor.execute('select * from product_inventory')
            # for x in mycursor.fetchall():
            # print(x)

        def users():
            userWindow = Toplevel(newWindow)

            uid = Label(userWindow, text='SELLER ID')
            uid.grid(row=0, column=0)

            fname = Label(userWindow, text='CUST NAME')
            fname.grid(row=0, column=1)

            lname = Label(userWindow, text='CUST PHONE')
            lname.grid(row=0, column=2)

            uadd = Label(userWindow, text='CUST ADDRESS')
            uadd.grid(row=0, column=3)

            upin = Label(userWindow, text="CUST PINCODE")
            upin.grid(row=0,column=4)

            upass = Label(userWindow, text="CUST PASSWORD")
            upass.grid(row=0,column=5)

            ugend = Label(userWindow, text="CUST GENDER")
            ugend.grid(row=0,column=6)

            udob = Label(userWindow, text="CUST DOB")
            udob.grid(row=0,column=7)

            mycursor.execute("select * from CUSTOMER")
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(userWindow, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            create_user = Button(userWindow, text='ADD USER', command=lambda: insert_user())
            create_user.grid(row=1, column=9)

            del_user = Button(userWindow, text='DELETE USER', command=lambda: delete_user())
            del_user.grid(row=2, column=9)

            update_user1 = Button(userWindow, text='UPDATE USER', command=lambda: update_user())
            update_user1.grid(row=3,column=9)

        def insert_user():
            userWindow = Toplevel(newWindow)

            uid = Label(userWindow, text='SELLER ID')
            uid.grid(row=0, column=0)

            fname = Label(userWindow, text='CUST NAME')
            fname.grid(row=0, column=1)

            lname = Label(userWindow, text='CUST PHONE')
            lname.grid(row=0, column=2)

            uadd = Label(userWindow, text='CUST ADDRESS')
            uadd.grid(row=0, column=3)

            upin = Label(userWindow, text="CUST PINCODE")
            upin.grid(row=0,column=4)

            upass = Label(userWindow, text="CUST PASSWORD")
            upass.grid(row=0,column=5)

            ugend = Label(userWindow, text="CUST GENDER")
            ugend.grid(row=0,column=6)

            udob = Label(userWindow, text="CUST DOB")
            udob.grid(row=0,column=7)

            uid1 = Entry(userWindow)
            uid1.grid(row=1,column=0)

            fname1 = Entry(userWindow)
            fname1.grid(row=1,column=1)

            lname1 = Entry(userWindow)
            lname1.grid(row=1,column=2)
        
            uadd1 = Entry(userWindow)
            uadd1.grid(row=1,column=3)

            upin1 = Entry(userWindow)
            upin1.grid(row=1,column=4)

            upass1 = Entry(userWindow)
            upass1.grid(row=1,column=5)

            ugend1 = Entry(userWindow)
            ugend1.grid(row=1,column=6)

            udob1 = Entry(userWindow)
            udob1.grid(row=1,column=7)


            insert_into = Button(userWindow, text='INSERT',
                                 command=lambda: insert_values_users(uid1.get(),fname1.get(),lname1.get(),uadd1.get(),upin1.get(),upass1.get(),ugend1.get(),udob1.get()))
            insert_into.grid(row=2,column=9)

        def insert_values_users(uid, ufname, ulname, uadd, upin, upass, ugend, udob):
            mycursor.execute('INSERT INTO customer(cust_id, cust_name, cust_phone, cust_address, cust_pincode, cust_password, cust_gender, cust_dob) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
                             (uid, ufname, ulname, uadd, upin, upass, ugend, udob))
            mydb.commit()

        def delete_user():
            insertWindow = Toplevel(newWindow)
            insertWindow.geometry("500x300")
            l1 = Label(insertWindow, text="Enter SELLER ID to be deleted")
            l1.place(x=20, y=20)

            e1 = Entry(insertWindow)
            e1.place(x=200, y=20)

            insert_into = Button(insertWindow, text='DELETE',
                                 command=lambda: remove_user(e1.get()))
            insert_into.place(x=60, y=80)

        def remove_user(user_id):
            mycursor.execute('delete from customer where cust_id=%s', (user_id,))
            mydb.commit()
        
        def update_user():
            userWindow = Toplevel(newWindow)

            uid = Label(userWindow, text='SELLER ID')
            uid.grid(row=0, column=0)

            what = Label(userWindow, text="WHAT TO UPDATE")
            what.grid(row=0,column=1)

            value1 = what = Label(userWindow, text="UPDATE VALUE")
            value1.grid(row=0,column=2)

            uid1 = Entry(userWindow)
            uid1.grid(row=1,column=0)

            update_what = Entry(userWindow)
            update_what.grid(row=1,column=1)

            value = Entry(userWindow)
            value.grid(row=1,column=2)

            update_into = Button(userWindow, text='UPDATE',
                                 command=lambda: update_values_user(update_what.get(),value.get(),uid1.get()))
            update_into.grid(row=2,column=9)

        def update_values_user(update_what,value,uid):
            # val = (update_what,value,uid)
            # query = 'UPDATE CUSTOMER SET %s = %s WHERE CUST_ID = %s'
            mycursor.execute("UPDATE CUSTOMER SET %s='%s' WHERE CUST_ID='%s'" % (update_what,value,uid))
            mydb.commit()            

        newWindow = Tk()
        newWindow.geometry("800x300")

        show_inventory = Button(newWindow, text="Show Items", command=items)
        show_inventory.place(x=20, y=20)

        show_order_lists = Button(newWindow, text='Show orders', command=order_lists)
        show_order_lists.place(x=150, y=20)

        show_users = Button(newWindow, text='Show users', command=users)
        show_users.place(x=300, y=20)

    else:
        print(mycursor.rowcount)
        MessageBox.showwarning('Error', 'Invalid login credentials')


root = Tk()
root.geometry("600x300")
root.title('Inventory Management')

empid = Label(root, text="Enter SELLER ID: ")
empid.place(x=20, y=20)

password = Label(root, text="Enter password: ")
password.place(x=20, y=50)

empid_entry = Entry(root)
empid_entry.place(x=150, y=20)

password_entry = Entry(root, show='*')
password_entry.place(x=150, y=50)

login_button = Button(root, text="Login", command=login_user, height=2, width=7)
login_button.place(x=170, y=130)

root.mainloop()