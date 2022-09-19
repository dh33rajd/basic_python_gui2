from tkinter import*

root=Tk()
root.geometry("500x200")
root.title("AIIMS Bhopal")
heading=Label(root,text="AIIMS Bhopal").grid(row=1,column=1,columnspan=3)

r=IntVar()
r1=IntVar()

def proceed():
    if r.get()==1:
        admi=Toplevel()
        admi.geometry("500x500")
        admi.title("Admin Login")
        pw=Label(admi,text="Enter the password : ").grid(row=1,column=1)
        enter=Entry(admi)
        enter.grid(row=2,column=1,columnspan=3)
        def admi_proceed(value):
            if int(value)==1234:
                welcome=Label(admi,text="welcome : ").grid(row=4,column=1,columnspan=3)
                opt1=Radiobutton(admi,text="add a doctor",variable=r1,value=1).grid(row=5,column=1,sticky=W)
                opt2=Radiobutton(admi,text="list doctors",variable=r1,value=2).grid(row=6,column=1,sticky=W)
                opt3=Radiobutton(admi,text="modify a doctor",variable=r1,value=3).grid(row=7,column=1,sticky=W)
                opt4=Radiobutton(admi,text="delete a doctor",variable=r1,value=4).grid(row=8,column=1,sticky=W)
                choose=Button(admi,text="proceed").grid(row=9,column=1,sticky=W)
                exi=Button(admi,text="exit",command=admi.destroy).grid(row=9,column=3)
            else:
                messagebox.showerror("Error","Incorrect Password")
        choose=Button(admi,text="proceed",command=lambda: admi_proceed(enter.get())).grid(row=3,column=1,sticky=W)
        exi=Button(admi,text="exit",command=admi.destroy).grid(row=3,column=3)
        
    if r.get()==2:
        use=Toplevel()
        use.geometry("500x500")
        use.title("User Login")
        pw=Label(use,text="Enter the password : ").grid(row=1,column=1)
        enter=Entry(use)
        enter.grid(row=2,column=1,columnspan=3)
        def use_proceed(value):
            if int(value)==1234:
                welcome=Label(use,text="welcome : ").grid(row=4,column=1,columnspan=3)
                opt1=Radiobutton(use,text="add a patient",variable=r1,value=1).grid(row=5,column=1,sticky=W)
                opt2=Radiobutton(use,text="find a patient",variable=r1,value=2).grid(row=6,column=1,sticky=W)
                opt3=Radiobutton(use,text="modify a patient",variable=r1,value=3).grid(row=7,column=1,sticky=W)
                opt4=Radiobutton(use,text="discharge a patient",variable=r1,value=4).grid(row=8,column=1,sticky=W)
                choose=Button(use,text="proceed").grid(row=9,column=1,sticky=W)
                exi=Button(use,text="exit",command=use.destroy).grid(row=9,column=3)
            else:
                messagebox.showerror("Error","Incorrect Password")
        choose=Button(use,text="proceed",command=lambda: use_proceed(enter.get())).grid(row=3,column=1,sticky=W)
        exi=Button(use,text="exit",command=use.destroy).grid(row=3,column=3)
        
login=Label(root,text="account login : ").grid(row=2,column=1)
opt1=Radiobutton(root,text="Admin",variable=r,value=1).grid(row=3,column=1,sticky=W)
opt2=Radiobutton(root,text="User",variable=r,value=2).grid(row=4,column=1,sticky=W)
choose=Button(root,text="proceed",command=proceed).grid(row=5,column=1)
exi=Button(root,text="exit",command=root.destroy).grid(row=5,column=3)

root.mainloop()