from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
import mysql.connector as db

con = db.connect(host="localhost",
                 user="root",
                 password="",
                 port=3306,
                 database="tourist")

cursor = con.cursor()
cursor.execute("""create table if not exists students(Name varchar(50) not null,
            Class varchar(50) not null,
            Division varchar(50) not null,
            Roll_Number varchar(50) not null,
            Parent_Name varchar(50) not null,
            Contact varchar(50) not null,
            Gender varchar(50) not null,
            Email varchar(50) not null,
            Password varchar(50) not null,
            Date_of_Birth varchar(50) not null)""")
con.commit()


window = Tk()
photo = PhotoImage(file="homeimage.png")
controller=BooleanVar()
window.title("Student Management System")
window.iconbitmap("icon.ico")
window.geometry("1000x650+300+20")

home=Frame(window,width=1000,height=650,).place(x=0,y=0)

    
title = Label(home,text="KELTRON KNOWLEDGE CENTRE - KUTTIPPURAM",font="Times 18 bold",bg="pink").pack(side=TOP,fill=X)
    
homepic = Label(home,image=photo).pack(side=LEFT,fill = Y)

contact=Label(home,text="Copyright @ 2023-24 Keltron Knowledge Centre Tkinter Training Program",font='times 12 bold',bg='yellow').place(x=270,y=620)

en1=StringVar()
en2=StringVar()

t1=StringVar()
t2=StringVar()
tr=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()
t8=StringVar()
t9=StringVar()
t10=StringVar()

se=StringVar()
############################### Login Here ##################################################################


loginform = Frame(home,bg="cadetblue1",width=500,height=500).pack(side=RIGHT)

frametitle = Label(loginform,text="Login Here",relief=GROOVE,bd=10,font="Times 20 bold",bg="burlywood").place(x=680,y=160)
loginid = Label(loginform,text="Enter Email Id : ",font="times 14 bold",bg="cadetblue1").place(x=580,y=300)
entry1 = Entry(loginform,font="times 16 ",textvariable=en1).place(x=750,y=300)

code = Label(loginform,text="Enter Password : ",font="times 14 bold",bg="cadetblue1").place(x=580,y=350)
entry2 = Entry(loginform,font="times 16 ",textvariable=en2).place(x=750,y=350)

def Go():
    if((en1.get()=="keltron@tkinter") and (en2.get()=="keltron") ):
        
        registerframe= Frame(home,bg="violetred2",width=1000,height=750).place(x=0,y=0)
        registerimage= Label(registerframe,image=photo,width=1000).place(x=0,y=380)
    
        name = Label(registerframe,text="Name : ",font="times 18 bold",bg="violetred2").place(x=20,y=20)
        gender = Label(registerframe,text="Gender : ",font="times 18 bold",bg="violetred2").place(x=480,y=20)
        cls = Label(registerframe,text="Class : ",font="times 18 bold",bg="violetred2").place(x=20,y=80)
        division = Label(registerframe,text="Division : ",font="times 18 bold",bg="violetred2").place(x=480,y=80)
        rollnumber = Label(registerframe,text="Roll Number : ",font="times 18 bold",bg="violetred2").place(x=20,y=140)
        birthdate = Label(registerframe,text="Date of Birth : ",font="times 18 bold",bg="violetred2").place(x=480,y=140)
        guardian = Label(registerframe,text="Guardian : ",font="times 18 bold",bg="violetred2").place(x=20,y=200)
        contact = Label(registerframe,text="Phone Number : ",font="times 18 bold",bg="violetred2").place(x=480,y=200)
        email = Label(registerframe,text="Email : ",font="times 18 bold",bg="violetred2").place(x=20,y=260)
        password = Label(registerframe,text="Password : ",font="times 18 bold",bg="violetred2").place(x=480,y=260)
    

    
            
        e1 = Entry(registerframe,font="times 18 ",textvariable=t1).place(x=180,y=20)
        e2 = Entry(registerframe,font="times 18 ",textvariable=t2,width=10).place(x=640,y=20)
    
        def sel():
            t2.set(tr.get())
        
    
        r1 = Radiobutton(registerframe,text="Male",font="times 18 bold",value="Male",bg="violetred2",variable=tr,command=sel).place(x=760,y=20)
        r2 = Radiobutton(registerframe,text="Female",font="times 18 bold",value="Female",bg="violetred2",variable=tr,command=sel).place(x=850,y=20)
        e3 = Entry(registerframe,font="times 18 ",textvariable=t3).place(x=180,y=80)
        e4 = Entry(registerframe,font="times 18 ",textvariable=t4).place(x=680,y=80)
        e5 = Entry(registerframe,font="times 18 ",textvariable=t5).place(x=180,y=140)
        e6 = Entry(registerframe,font="times 18 ",textvariable=t6).place(x=680,y=140)
        e7 = Entry(registerframe,font="times 18 ",textvariable=t7).place(x=180,y=200)
        e8 = Entry(registerframe,font="times 18 ",textvariable=t8).place(x=680,y=200)
        e9 = Entry(registerframe,font="times 18 ",textvariable=t9).place(x=180,y=260)
        e10 = Entry(registerframe,font="times 18 ",textvariable=t10).place(x=680,y=260)

#### Submit Button ###########################
    
        def sub():
            if(t1.get()!="" and t5.get()!="" and t7.get()!="" and t8.get()!="" and t9.get()!="" and t10!=""):
                data={}
                data["Name"]=t1.get()
                data["Class"]=t3.get()
                data["Division"]=t4.get()
                data["Roll_Number"]=t5.get()
                data["Parent_Name"] =t7.get()
                data["Contact"] =t8.get()
                data["Gender"] =t2.get()
                data["Email"] =t9.get()
                data["Password"] =t10.get()
                data["Date_of_Birth"] =t6.get()
                cursor.execute(f"""INSERT INTO students values(
                '{data["Name"]}',
                '{data["Class"]}',
                '{data["Division"]}',
                '{data["Roll_Number"]}',
                '{data["Parent_Name"]}',
                '{data["Contact"]}',
                '{data["Gender"]}',
                '{data["Email"]}',
                '{data["Password"]}',
                '{data["Date_of_Birth"]}')""")
                con.commit()
                showinfo(title="Done",message="Successfully Submited")
            else:
                showerror(title="Error",message="Empty Field Exist")

        save = Button(registerframe,text="Submit",font="times 18 bold",bg="springgreen1",command=sub).place(x=360,y=320)


####### Search Bar ###########################

        search = Entry(registerframe,textvariable=se,font="times 14 bold").place(x=20,y=330)
        se.set("Search Roll Number")
        def ser():
            pass
        se_button = Button(registerframe,text="Search",font="times 14 bold",bg="gray",command=ser).place(x=235,y=325)



#### Update Button ########################### 
   
        def up():
            pass
        update = Button(registerframe,text="Update",font="times 18 bold",bg="purple",command=up).place(x=490,y=320)


#### Delete Button ########################### 
   
        def dele():
            pass
        delete = Button(registerframe,text="Delete",font="times 18 bold",bg="red",command=dele).place(x=620,y=320)

### Clear Button#############################
        def clr():
            t1.set("")
            t2.set("")
            t3.set("")
            t4.set("")
            t5.set("")
            t6.set("")
            t7.set("")
            t8.set("")
            t9.set("")
            t10.set("")
        clear = Button(registerframe,text=" clear ",font="times 18 bold",bg="white",command=clr).place(x=740,y=320)
   
### Back Button#############################
        def bk():
            window.destroy()

        quit = Button(registerframe,text="Close",font="times 18 bold",bg="snow4",command=bk).place(x=850,y=320)

    elif(en1.get()=="" and en2.get()==""):
        showerror(title="Error",message="Empty Field Exist")
    else:
        showerror(title="Error",message="Wrong Entry")




## Register Button

login = Button(loginform,text="LOGIN",font="times 20 bold",bg="green1",relief=SUNKEN,width=10,command=Go).place(x=650,y=420)
#register = Button(loginform,text="REGISTER",font="times 24 bold",relief=SUNKEN,bg="lavender",width=20,command=submit).place(x=580,y=420)


window.mainloop()
	





