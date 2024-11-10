from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130") 
        self.root.title("Inventory Management System |  Developed by BYTE ME")
        self.root.config(bg="white")
        self.root.focus_force()
        #=========================
        #===Variables===
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()


        #===Frames===
        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)

        #===title===
        title=Label(product_Frame,text=" ManageProduct Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        #===column1===
        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",15),bg="white").place(x=30,y=110)
        lbl_name=Label(product_Frame,text="Name",font=("goudy old style",15),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",15),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",15),bg="white").place(x=30,y=310)

        #===column2===
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)


        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=150,y=11100,width=200)
        cmb_cat.current(0)

        txt_cat=Entry(product_Frame,textvariable=self.var_cat,font=("goudy old style",15),bg='light yellow').place(x=150,y=110,width=200)



if __name__=="__main__":
    root=Tk() 
    obj=productClass(root)
    root.mainloop()  