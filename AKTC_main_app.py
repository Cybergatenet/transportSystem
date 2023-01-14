from tkinter import *
from tkinter.font import Font
# from tkhtmlview import HTMLLabel
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime
import time
from tkinter.messagebox import showinfo

wind = Tk()
wind.title("-- AKTC Automated Information System -- ")
winhet = wind.winfo_screenheight()
winwidt = wind.winfo_screenwidth()
mainwinh = winhet - 200
mainwidt = winwidt - 200

wind.geometry("%dx%d" % (mainwidt, mainwinh))
icon = PhotoImage(file='img/mainjpg.png')
wind.iconphoto(False, icon)

# the fonts
font1 = Font(family='Times New Roman', size=12, weight='bold', slant='roman', underline=True, overstrike=False)
font1b = Font(family='Times New Roman', size=12, slant='roman', overstrike=False)
font2 = Font(family='comic', size=10, weight='bold', slant='roman', )
font3 = Font(family='comic', size=15, weight='bold', slant='roman', )
f4 = Font(family='comic', size=12, weight='bold', slant='roman', )
f5 = Font(family='Lucida Sans', size=9, weight='bold', slant='roman', )

t = time.localtime()
dt = time.asctime(t)
x = datetime.datetime.now()
months = x.strftime('%B')

# THE CONNECTIONS AND DATABASE ARRANGEMNET
inconnection = sqlite3.connect("aktc_main.db")
icursor = inconnection.cursor()
dconnection = sqlite3.connect("aktc_main.db")
dcursor = dconnection.cursor()


# THE WINDOWS AND THE DESKTOP APPS
Frstframe = Frame(wind, bg='black')
sub_frm = Frame(Frstframe, relief=SUNKEN, )

dexk = PhotoImage(file= 'img/bg9.png')
dexkv = dexk.subsample(7, 5)

ldesk = Label(sub_frm, image=dexkv,justify=LEFT, bd=0)
ldesk.grid(row=0,column=2)

sub_frm.pack(fill=BOTH, pady=10, padx=10)

genderdb = StringVar()
genderdb1 = StringVar()

# THIS TIS THE SECOND SCCREE AND SISINES ME
Secondwind = PanedWindow(wind, orient=HORIZONTAL, bg='#090315')
sectframe = Frame(Secondwind, relief=SUNKEN, bd=5, padx=10, pady=10, bg='#341ff5')
workframe = Frame(Secondwind, relief=SUNKEN, bd=5, bg='#eee', width=800)
Secondwind.add(sectframe)
Secondwind.add(workframe)

# OVER HERE WE GET OUR FUNCTIONS FOR SECOND WINDOW;
# FUNCTTIONS AND FUNCTIIONSS AND FUNCTIONS AND FUNCTIONS

# BUTTON TO HIDE
def staffschframedes():
    # searchfram5.destroy()
    deletebu5.destroy()
    AddStaff.destroy()
    searchfram6.destroy()

def lognin():
    if userver.get() == '' or identver.get() == '':
        messagebox.showerror('Input Error', 'All fields are required',parent=loginFr)
    elif userver.get()=='Admin':
        try:
            connection1 = sqlite3.connect("aktc_main.db")
            cursor1 = connection1.cursor()
            yes = connection1.execute('SELECT * FROM stafflist WHERE Email= ? OR Office=? AND Password=?',
                                      ('Admin', 'Admin', identver.get(),))
            row = yes.fetchone()
            if row == None:
                messagebox.showerror('Wrong input', 'Not registerd in our system')
            else:
                password_reset.destroy()
                Frstframe.pack_forget()
                Secondwind.pack(fill=BOTH, expand=True)
                theuser = Label(taskbar, text=row[7], font=font1)
                theuser.place(rely=0, relx=0.4)
                h3.configure(text=f'{row[1]} {row[2]}')
                h4.configure(text=f'I am {row[7]}')

            connection1.commit()
            connection1.close()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=Secondwind)
    elif userver.get()=='Superadmin':
        connection1 = sqlite3.connect("aktc_main.db")
        cursor1 = connection1.cursor()
        yes = connection1.execute('SELECT * FROM stafflist WHERE Email= ? OR Office=? AND Password=?',
                                  ('Superadmin', 'Superadmin', identver.get(),))
        row = yes.fetchone()
        if row == None:
            messagebox.showerror('Wrong input', 'Not registerd in our system')
        else:
            Frstframe.pack_forget()
            Secondwind.pack(fill=BOTH, expand=True)
            theuser = Label(taskbar, text=row[7], font=font1)
            theuser.place(rely=0, relx=0.4)
            h3.configure(text=f'{row[1]} {row[2]}')
            h4.configure(text=f'I am {row[7]}')

        connection1.commit()
        connection1.close()
    elif userver.get() != 'Admin' and userver.get() != 'Superadmin':
        try:

            connection1 = sqlite3.connect("aktc_main.db")
            cursor1 = connection1.cursor()
            yes = connection1.execute('SELECT * FROM stafflist WHERE Email= ? OR Office=? AND Password=?',(userver.get(),userver.get(),identver.get(),))
            row = yes.fetchone()
            if row == None:
                messagebox.showerror('Wrong input','Not registerd in our system')
            else:
                password_reset.destroy()
                staffschframedes()
                Frstframe.pack_forget()
                Secondwind.pack( fill= BOTH, expand = True)
                theuser= Label(taskbar,text=row[7],font=font1)
                theuser.place(rely=0,relx=0.4)
                h3.configure(text=f'{row[1]} {row[2]}')
                h4.configure(text=f'I am {row[7]}')


            connection1.commit()
            connection1.close()
        except Exception as es:
            messagebox.showerror('Error',f"Error due to :{str(es)}",parent=loginFr)

def logout():
    lm= messagebox.askyesno(title='Logout',message='Do you want to LOG out ?',)
    if lm:
        Frstframe.pack(fill=BOTH)
        Secondwind.pack_forget()
    else:
        messagebox.showinfo('Return','Returning to my Dashboard')

def dasboardmange():
    try:
        for item in tree.get_children():
            tree.delete(item)
        sl= sqlite3.connect("aktc_main.db")
        slcursor = sl.cursor()
        slcursor.execute("SELECT seq FROM sqlite_sequence")
        tsl= slcursor.fetchall()
        # for i in tsl:
        activeld_no.configure(text=tsl[2])
        activeld_no4.configure(text=tsl[0])
        activeld_no5.configure(text=tsl[3])
        activeld_no3.configure(text=tsl[1])
        sl.commit()
        sl.close()

        lconnection = sqlite3.connect("aktc_main.db")
        lcursor = lconnection.cursor()
        # Driverid,No_of_passengers, Tripnumber,Busnumber, Cashdeposite, Driversdept,Loaddate,Loadfrom,Loadto,Consigner,Tripstate,Date
        lcursor.execute(
            "SELECT loadid,Busnumber,Driverid,Phoneno,Consigner,Loaddate,Loadfrom,Loadto,Date FROM Loadlist")
        tt = lcursor.fetchall()
        for contact in tt:
            tree.insert('', END, values=contact)

        lcursor.execute(
            "SELECT Cashdeposite FROM Loadlist")
        tc = lcursor.fetchall()
        myresult1 = sum(map(sum, tc))
        activeld_no2.configure(text=myresult1)
        lcursor.execute(
            "SELECT Driversdept FROM Loadlist")
        tm = lcursor.fetchall()
        myresult2 = sum(map(sum, tm))
        activeld_no1.configure(text=myresult2)
        lcursor.execute(
            "SELECT No_of_passengers FROM Loadlist")
        tmk = lcursor.fetchall()
        myresult3 = sum(map(sum, tmk))
        activeld_no6.configure(text=myresult3)
        lconnection.commit()
        lconnection.close()
    except Exception as ex:
        messagebox.showerror('Error', f'Error due to {str(ex)}', parent=thecontentd1)

    Loading_details.pack_forget()
    Consinger_addstaff.pack_forget()
    DriverManagement.pack_forget()
    ProfileManger.pack_forget()
    Report.pack_forget()
    ImagSection.pack_forget()
    Dashboard.pack(fill= BOTH, expand = True)

def displaydivs():
    pass

# --------------------THIS MANAGES FOR THE LOADS AND EVERY BUTTON ON THE LOAD PAGE --------------
def loadmange():
    try:
        lconnection = sqlite3.connect("aktc_main.db")
        lcursor = lconnection.cursor()
        lcursor.execute(
            "SELECT loadid,Driverid,Loaddate,Loadfrom FROM Loadlist")
        t3 = lcursor.fetchall()
        for item in tree3.get_children():
            tree3.delete(item)
        for contact in t3:
            tree3.insert('', END, values=contact)
    except Exception as ex:
        messagebox.showerror('Record not found', parent=Loading_details)
    lconnection.commit()
    lconnection.close()
    Dashboard.pack_forget()
    ImagSection.pack_forget()
    Report.pack_forget()
    DriverManagement.pack_forget()
    Consinger_addstaff.pack_forget()
    Loading_details.pack(fill= BOTH, expand = True)
    ProfileManger.pack_forget()

def updatetheload():
    lconnection = sqlite3.connect("aktc_main.db")
    lcursor = lconnection.cursor()
    lcursor.execute(
        'CREATE TABLE IF NOT EXISTS Loadlist(loadid INTEGER PRIMARY KEY AUTOINCREMENT,Driverid TEXT,No_of_passengers INTEGER,Tripnumber INTEGER,Busnumber TEXT,Cashdeposite INTEGER,Driversdept INTEGER,Loaddate TEXT,Loadfrom TEXT,Loadto TEXT,Consigner TEXT,Phoneno TEST,Tripstate TEXT,Date TEXT)')
    if loadin1.get() == '' or loadin2.get() == '' or loadin3.get() == '' or loadin4.get() == '' or loadin5.get() == '' or loadin6.get() == '' or loadin7.get() == '' or loadin8.get() == '' or loadin9.get() == '' or loadin10.get() == ''or loadin11.get()=='' or loadin12.get() == '':
        messagebox.showerror('Error', 'All fields are required', parent=Loading_details)
    else:
        try:
            lcursor.execute(
                "INSERT INTO Loadlist(Driverid,No_of_passengers, Tripnumber,Busnumber, Cashdeposite, Driversdept,Loaddate,Loadfrom,Loadto,Consigner,Phoneno,Tripstate,Date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (loadin1.get().title(), loadin2.get(), loadin3.get(), loadin4.get(), loadin5.get(),
                 loadin6.get(), loadin7.get(), loadin8.get(), loadin9.get(), loadin10.get(),loadin11.get(),
                 loadin12.get(), dt,))
            messagebox.showinfo('Success', 'Registerd sucessfully', parent=Loading_details)
            lcursor.execute(
                "SELECT loadid,Driverid,Loaddate,Loadfrom FROM Loadlist")
            t3 = lcursor.fetchall()
            for item in tree3.get_children():
                tree3.delete(item)
            for contact in t3:
                tree3.insert('', END, values=contact)

            lconnection.commit()
            lconnection.close()
            loadin1.delete(0, END)
            loadin2.delete(0, END)
            loadin3.delete(0, END)
            loadin4.delete(0, END)
            loadin5.delete(0, END)
            loadin6.delete(0, END)
            loadin7.delete(0, END)
            loadin8.delete(0, END)
            loadin9.delete(0, END)
            loadin10.delete(0, END)
            loadin11.delete(0, END)
            loadin12.delete(0, END)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=Loading_details)

def selectitem():
    tree3.selection()
    curItem = tree3.focus()
    tt4 = [tuple(tree3.item(curItem)['values'])]
    for contact4 in tt4:
        tree4.insert('', END, values=contact4)

def delactivate():
    try:
        selectedstaff= tree4.selection()[0]
        tree4.delete(selectedstaff)
    except Exception as es:
        messagebox.showerror('Error', f"Error due to :{str(es)}", parent=loginFr)


# ------------------THIS IS FOR THE STAFFS AND ADMIN FUNCTIONS------------------------
def newstaff():
    icursor.execute(
        "CREATE TABLE IF NOT EXISTS stafflist(Staffid INTEGER PRIMARY KEY AUTOINCREMENT,Fname TEXT, Lname TEXT,Email TEXT, Phoneno TEXT, Gender TEXT,Password TEXT,Office TEXT, Salary TEXT, Address TEXT, Date TEXT)")

    if fnam.get()=="" or lastnam.get()=="" or emailin.get()=="" or phonein.get()=="" or genderdb.get()=="" or pass1.get()=="" or pass2.get()=="" or office2.get()=="" or Salary.get()=="" or addressin.get()=="":
        messagebox.showerror('Error', 'All fields are required',parent=adminreg )
    elif pass1.get() != pass2.get() :
        messagebox.showerror('Error', "Your passwords don't macth",parent= adminreg)
    else:
        try:
            icursor.execute('SELECT * FROM stafflist WHERE Email= ?', (userver.get(),))
            row = icursor.fetchone()

            if row != None:
                messagebox.showerror("Error", 'User already exist, pls try again with another email')
            else:
                # Fname TEXT, Lname TEXT,Email TEXT, Phoneno TEXT, Gender TEXT,Password TEXT,Office TEXT, Salary TEXT, Address TEXT, Date TEXT)")
                icursor.execute("INSERT INTO stafflist(Fname,Lname,Email,Phoneno,Gender,Password,Office,Salary,Address,Date) VALUES (?,?,?,?,?,?,?,?,?,?)",
                               (fnam.get().title(), lastnam.get().title(), emailin.get(),phonein.get(),genderdb.get(),pass1.get(),office2.get().title(),Salary.get(),addressin.get(),dt))
                messagebox.showinfo('Success', 'Registerd sucessfully', parent=adminreg)
            inconnection.commit()
            inconnection.close()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}',parent= adminreg)

def consinermange():
    inconnection = sqlite3.connect("aktc_main.db")
    icursor = inconnection.cursor()
    icursor.execute(
        "SELECT Staffid,Fname,Lname,Email,Phoneno,Gender,Password,Office,Salary,Date,Address FROM stafflist")
    tt5 = icursor.fetchall()
    chek5 = len(tt5)
    for item in tree5.get_children():
        tree5.delete(item)
    for contact5 in tt5:
        tree5.insert('', END, values=contact5)
    inconnection.commit()
    inconnection.close()
    ImagSection.pack_forget()
    DriverManagement.pack_forget()
    Loading_details.pack_forget()
    Report.pack_forget()
    Dashboard.pack_forget()
    Consinger_addstaff.pack(fill= BOTH, expand = True)
    displayconsingers.pack(fill=BOTH, expand=True)
    ProfileManger.pack_forget()

def addstaffnav():
    displayDrivers.pack_forget()
    displayconsingers.pack_forget()
    adminreg.pack()

def canclestaffnav():
    adminreg.pack_forget()
    displayconsingers.pack(fill=BOTH, expand=True)

def deletexcessstaff():
    try:
        inconnection = sqlite3.connect("aktc_main.db")
        icursor = inconnection.cursor()
        curItem = tree5.focus()
        tt4 = tuple(tree5.item(curItem)['values'])
        tcheck = tt4[0]

        icursor.execute(
            "DELETE FROM stafflist WHERE Staffid =? ",(tcheck,))

        tree5.delete(curItem)
    except Exception as es:
        messagebox.showerror('info', f'you selected nothing {es}', parent=displayconsingers)
    inconnection.commit()
    inconnection.close()

# ----------------------------DRIVER MANGEMENT AND FUNCTIONS IN THE MANAGER --------------------
# DRIVER MANAGER FUNCTION
def Driverregisterd():
    dcursor.execute('CREATE TABLE IF NOT EXISTS Driverslist(Driverid INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Email TEXT,Gender TEXT,Phoneno TEXT,DrivOfficeid TEXT,State_origin TEXT,Lga_origin TEXT,Salary TEXT,Licenses_no TEXT,Marital_status TEXT,DOB TEXT,YearsEx TEXT,Date TEXT)')
    if loadind1.get() == ''or loadind2.get() == ''or loadind3.get()=='' or loadind4.get()=='' or  loadind5.get()=='' or loadind6.get()==''or loadind7.get()==''or loadind8.get()==''or loadind9.get()==''or loadind10.get()=='' or loadind11.get()=='' or loadind12.get()=='':
        messagebox.showerror('Error', 'All fields are required',parent=thecontentd1 )
    else:
        try:
            dconnection.execute('SELECT * FROM Driverslist WHERE Email = ? AND DrivOfficeid =? ', (loadind2.get(),loadind5.get(),))
            row2 = dcursor.fetchone()
            if row2 != None:
                messagebox.showerror("Error", 'User already exist, pls try again with another email or change the Drivers id')
            else:
                dcursor.execute(
                    # Name TEXT,email TEXT,gender TEXT,phoneno TEXT,driversid TEXT,state_origin TEXT,lga_origin TEXT,salary TEXT,licenses_no TEXT,marital_status TEXT,DOB TEXT,yearsexTEXT
                    "INSERT INTO Driverslist(Name,Email, Gender,Phoneno, DrivOfficeid, State_origin,Lga_origin,Salary,Licenses_no,Marital_status,DOB,YearsEx,Date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (loadind1.get().title(),loadind2.get().title(),loadind3.get(),loadind4.get(),loadind5.get().title(),loadind6.get().title(),loadind7.get().title(),loadind8.get(),loadind9.get(),loadind10.get(),loadind11.get(),loadind12.get(),dt,))
                messagebox.showinfo('Success', 'Registerd sucessfully', parent=thecontentd1)
            dconnection.commit()
            dconnection.close()
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=thecontentd1)

def drivermange():
    ImagSection.pack_forget()
    Report.pack_forget()
    Consinger_addstaff.pack_forget()
    Loading_details.pack_forget()
    Dashboard.pack_forget()
    ProfileManger.pack_forget()
    DriverManagement.pack(fill= BOTH, expand = True)
    # if userver.get() != 'Superadmin' or userver.get() != 'Admin':
    #     driveschframedes()
    #     staffschframedes()
    dcursor.execute(
        "SELECT Driverid,Name,Email,Phoneno,Gender,DrivOfficeid,State_origin,Date,Licenses_no FROM Driverslist")
    tt6 = dcursor.fetchall()
    chek6 = len(tt6)
    for item in tree6.get_children():
        tree6.delete(item)
    for contact6 in tt6:
        tree6.insert('', END, values=contact6)

    displayDrivers.pack(fill= BOTH, expand = True)
    addNdriver.pack_forget()

def adddrive():
    try:
        for item in treed3.get_children():
            treed3.delete(item)
        bl= sqlite3.connect("aktc_main.db")
        blcursor = bl.cursor()
        blcursor.execute(
            "SELECT Vehiclename,Vehicleprice, Platenumber,Condition, Driver FROM Buslist")
        ttd3= blcursor.fetchall()
        for contact in ttd3:
            treed3.insert('', END, values=contact)
        bl.commit()
        bl.close()
    except Exception as ex:
        messagebox.showerror('Error', f'Error due to {str(ex)}', parent=treed4)

    displayDrivers.pack_forget()
    addNdriver.pack(fill=BOTH, expand=True)

def drivenavb():
    displayDrivers.pack(fill=BOTH, expand=True)
    addNdriver.pack_forget()

def driverdel():
    try:
        curItem = tree6.focus()
        tt4 = tuple(tree6.item(curItem)['values'])
        tcheck = tt4[0]

        icursor.execute(
            "DELETE FROM Driverslist WHERE Driverid =? ",(tcheck,))

        tree6.delete(curItem)
    except Exception as es:
        messagebox.showerror('info', f'you selected nothing {es}', parent=displayconsingers)
    inconnection.commit()
    inconnection.close()
# BUSSES FUNCTION
def RegisterBuses():
    bconnection = sqlite3.connect("aktc_main.db")
    bcursor = bconnection.cursor()
    bcursor.execute(
        'CREATE TABLE IF NOT EXISTS Buslist(busid INTEGER PRIMARY KEY AUTOINCREMENT,Vehiclename TEXT,Vehicleprice TEXT,Platenumber TEXT,Condition TEXT,Driver TEXT,Date TEXT)')
    if loadinb1.get() == '' or loadinb2.get() == '' or loadinb3.get() == '' or loadinb4.get() == '' or loadinb5.get() == '' :
        messagebox.showerror('Error', 'All fields are required', parent=treed4)
    else:
        try:
            bcursor.execute(
                "INSERT INTO Buslist(Vehiclename,Vehicleprice, Platenumber,Condition, Driver, Date) VALUES(?,?,?,?,?,?)",
                (loadinb1.get().title(), loadinb2.get(), loadinb3.get(), loadinb4.get(), loadinb5.get(),
              dt,))
            messagebox.showinfo('Success', 'Registerd sucessfully', parent=treed4)
            for item in treed3.get_children():
                treed3.delete(item)
            bcursor.execute(
                "SELECT Vehiclename,Vehicleprice, Platenumber,Condition, Driver FROM Buslist")
            ttd3 = bcursor.fetchall()
            for contact in ttd3:
                treed3.insert('', END, values=contact)
            bconnection.commit()
            bconnection.close()
            loadinb1.delete(0, END)
            loadinb2.delete(0, END)
            loadinb3.delete(0, END)
            loadinb4.delete(0, END)
            loadinb5.delete(0, END)
        except Exception as ex:
            messagebox.showerror('Error', f'Error due to {str(ex)}', parent=treed4)

#THIS DISPLAYS MY FUNCTION

def Profile():
    try:
        connection1 = sqlite3.connect("aktc_main.db")
        cursor1 = connection1.cursor()
        yes = connection1.execute('SELECT * FROM stafflist WHERE Email= ? OR Office=? AND Password=?',
                                  (userver.get(), userver.get(), identver.get(),))
        row = yes.fetchone()
        loadinp1.configure(text=f'{row[1]} {row[2]}')
        loadinp2.configure(text=row[3])
        loadinp3.configure(text=row[4])
        loadinp4.configure(text=row[5])
        loadinp5.configure(text=row[6])
        loadinp6.configure(text=row[7])
        loadinp7.configure(text=row[8])
        loadinp8.configure(text=row[9])
        loadinp9.configure(text=row[10])
        inconnection.commit()
        inconnection.close()
    except Exception as es:
        messagebox.showerror('Error', f"Error due to :{str(es)}", parent=loginFr)
    Consinger_addstaff.pack_forget()
    Loading_details.pack_forget()
    Dashboard.pack_forget()
    Report.pack_forget()
    DriverManagement.pack_forget()
    Profile.pack(fill=BOTH, expand=True)
    ProfileManger.pack(fill= BOTH, expand = True)

def showsetpassword():
    resetArea.grid(row=5, column=2,sticky=W)

def setpassdb():
    if newpassin.get() =="" and confirmpassin.get() =="":
        messagebox.showerror('Error', "Your passwords is empty",parent=resetArea)
    elif newpassin.get() != confirmpassin.get():
        messagebox.showerror('Error', "Your passwords don't macth", parent=resetArea)
    else:
        try:
            connection1 = sqlite3.connect("aktc_main.db")
            cursor1 = connection1.cursor()
            yes = connection1.execute('UPDATE stafflist SET Password=? WHERE Office= ?',
                                      (newpassin.get(), 'Superadmin',))
            connection1.commit()
            connection1.close()
        except Exception as es:
            messagebox.showerror('Error', f"Error due to :{str(es)}", parent=resetArea)

# THIS CHECKS FOR THE REPORTS AND MANAGES THE ITEMS

def viewReport():
    try:
        lconnection = sqlite3.connect("aktc_main.db")
        lcursor = lconnection.cursor()
        # Driverid,No_of_passengers, Tripnumber,Busnumber, Cashdeposite, Driversdept,Loaddate,Loadfrom,Loadto,Consigner,Tripstate,Date
        lcursor.execute(
            "SELECT loadid,Driverid,No_of_passengers,Tripnumber,Busnumber,Loadto,Cashdeposite,Driversdept,Tripstate,Date FROM Loadlist")
        tt = lcursor.fetchall()
        for contact in tt:
            tree10.insert('', END, values=contact)
        lcursor.execute(
            "SELECT Cashdeposite FROM Loadlist")
        tc= lcursor.fetchall()
        myresult1 = sum(map(sum, tc))
        cdepdisp.configure(text=myresult1)
        lcursor.execute(
            "SELECT Driversdept FROM Loadlist")
        tm= lcursor.fetchall()
        myresult2 = sum(map(sum, tm))
        cdepdisp1.configure(text=myresult2)
        lcursor.execute(
            "SELECT No_of_passengers FROM Loadlist")
        tmk = lcursor.fetchall()
        myresult3 = sum(map(sum, tmk))
        cdepdisp2.configure(text=myresult3)
        lconnection.commit()
        lconnection.close()
    except Exception as ex:
        messagebox.showerror('Error', f'Error due to {str(ex)}', parent=thecontentd1)
    Report.pack(fill=BOTH, expand=True)
    Loading_details.pack_forget()
    Consinger_addstaff.pack_forget()
    DriverManagement.pack_forget()
    ProfileManger.pack_forget()
    Dashboard.pack_forget()
    ImagSection.pack_forget()


# THE AREA FOR OUR NAVS AND OUR LINKS
capture = Frame(sectframe, width=300, height=300,bg='#341ff5')
capture.grid(row=1, column=0, padx=10, pady=10)
innerimg = PhotoImage(file='img/avatar6.png')
cim= innerimg.subsample(4, 4)
seeimg = Label(capture, image=cim,justify=LEFT, bd=0,)
seeimg.grid(row=0,column=0,columnspan=2,sticky='w')

h4 = Label(capture, text="Username",font=font3,bg='#341ff5',fg='white')
h4.grid(row=1,column=0, columnspan=2,sticky='w')
h3 = Label(capture, text="Office", font=font2,bg='#341ff5',fg='white')
h3.grid(row=2,column=0, columnspan=2,sticky='w')

bt1 = Button(sectframe, text='Dashboard', width=20, font=font1b, bg='#341ff5', fg='white', bd=0,command=dasboardmange)
bt2 = Button(sectframe, text='Report', width=20, font=font1b, bg='#341ff5', fg='white', bd=0,command=viewReport)
bt3 = Button(sectframe, text='Consingner Management', width=20, font=font1b, bg='#341ff5', fg='white', bd=0,command=consinermange)
bt4 = Button(sectframe, text='Load Management', width=20, font=font1b, bg='#341ff5', fg='white', bd=0,command=loadmange)
bt5 = Button(sectframe, text='Driver Management', width=20, font=font1b, bg='#341ff5', fg='white', bd=0, command=drivermange)
bt6 = Button(sectframe, text='My profile', width=20, font=font1b, bg='#341ff5', fg='white', bd=0,command=Profile)

bt1.grid(row=2, column=0,sticky='w',pady=10)
bt2.grid(row=3, column=0,sticky='w',pady=10)
bt3.grid(row=4, column=0,sticky='w',pady=10)
bt4.grid(row=5, column=0,sticky='w',pady=10)
bt5.grid(row=6, column=0,sticky='w',pady=10)
bt6.grid(row=7, column=0,sticky='w',pady=10)


taskbar = Frame(workframe, width=mainwidt,height=30)
# taskbar.grid(row=0, column=0)
taskbar.pack(fill= BOTH, )

applab = Label(taskbar, text='AKTC_Automation_System', bg='#efefef', fg='black', font=font1)
applab.place(rely=0, relx=0.03)
logout= Button(taskbar, text='Log-out',background='red',fg='white',font=font2,command=logout)
logout.place(rely=0,relx=0.7)

# --------------------------------------------DISLPLAY ALL IMAGE SECTIONS AND WHAT THEY SAY ----------------------
ImagSection = Frame(workframe,bg='#eee',padx=10,pady=20)
ImagSection.pack(fill=BOTH, expand=True)
ImagesShow = Frame(ImagSection,bg='#eee',padx=10,pady=20)
show1 = PhotoImage(file='img/bus.png')
showcim1= show1.subsample(2, 2)
showseeim1 = Label(ImagesShow, image=showcim1,justify=LEFT, bd=5,relief=SUNKEN)
showseeim1.grid(row=0,column=0)

show2 = PhotoImage(file='img/bus.png')
showcim2= show2.subsample(2, 2)
showseeim2 = Label(ImagesShow, image=showcim2,justify=LEFT, bd=5,relief=SUNKEN)
showseeim2.grid(row=0,column=1)

show3 = PhotoImage(file='img/bus1.png')
showcim3= show3.subsample(2, 2)
showseeim3 = Label(ImagesShow, image=showcim3,justify=LEFT, bd=5,relief=SUNKEN)
showseeim3.grid(row=1,column=0)

show4 = PhotoImage(file='img/bus.png')
showcim4= show4.subsample(2, 2)
showseeim4 = Label(ImagesShow, image=showcim4,justify=LEFT, bd=5,relief=SUNKEN)
showseeim4.grid(row=1,column=1)

ImagesShow.pack(fill=BOTH, expand=True)
# DASHHBOARD
Dashboard = Frame(workframe, bg='#eee',padx=10,pady=20)
semidashb = Frame(Dashboard)

fdisp1 = Font(family='comic', size=15, weight='bold', slant='roman', )
fdisp2= Font(family='comic', size=10, weight='bold', slant='roman', )

div1= Frame(semidashb, bg='#696a6b',pady=10,padx=15,relief="raised",width=400)
# div1.place(relheight=100,relwidth=200,rely=0.5,relx=0.5)
activeld_no = Label(div1,bg='#696a6b',fg='white',font=fdisp1, pady=5)
activeld_no.grid(row=0,column=0, sticky='w')
activeld = Label(div1, bg='#696a6b',fg='white', text=' Active Loads ',font=fdisp2)
activeld.grid(row=1,column=0, sticky='w')
minfo = Button(div1,bg='#696a6b',pady=2,relief=FLAT, fg='white',text="More info", command=loadmange)
minfo.grid(row=3,column=0)
div1.grid(row=0, column=0,sticky="w",)
Label(semidashb,text=' ').grid(row=0, column=1,sticky='w')


div2= Frame(semidashb, bg='green',pady=10,padx=10,width=400)
activeld_no1 = Label(div2,bg='green',fg='white',font=fdisp1, pady=5)
activeld_no1.grid(row=0,column=0, sticky='w')
activeld1 = Label(div2, bg='green',fg='white', text='Load Dept',font=fdisp2)
activeld1.grid(row=1,column=0, sticky='w')
minfo1 = Button(div2,bg='green',relief=FLAT, fg='white',pady=2,text="More info",command=viewReport)
minfo1.grid(row=3,column=0)
div2.grid(column=2, row=0)
Label(semidashb,text=' ').grid(row=0, column=3,sticky='w')

div3= Frame(semidashb, bg='#f1a500',pady=10,padx=10,width=400)
activeld_no2 = Label(div3,bg='#f1a500',fg='white',font=fdisp1, pady=5,)
activeld_no2.grid(row=0,column=0, sticky='w')
activeld2 = Label(div3, bg='#f1a500',fg='white', text='Loads Balance',font=fdisp2)
activeld2.grid(row=1,column=0, sticky='w')
minfo2 = Button(div3,bg='#f1a500',relief=FLAT, fg='white',text="More info",pady=2,command=viewReport)
minfo2.grid(row=3,column=0)
div3.grid(column=4, row=0)
Label(semidashb,text=' ').grid(row=0, column=5,sticky='w')

div4= Frame(semidashb, bg='#1982ac',pady=10,padx=10,width=400)
activeld_no3= Label(div4,bg='#1982ac',fg='white',font=fdisp1, pady=5)
activeld_no3.grid(row=0,column=0, sticky='w')
activeld3 = Label(div4, bg='#1982ac',fg='white', text='   Drivers   ',font=fdisp2)
activeld3.grid(row=1,column=0, sticky='w')
minfo3 = Button(div4,bg='#1982ac',relief=FLAT, fg='white',pady=2,text="More info",command=drivermange)
minfo3.grid(row=3,column=0)
div4.grid(column=6, row=0)
Label(semidashb,text=' ').grid(row=0, column=7,sticky='w')

div5= Frame(semidashb, bg='#1d201f',pady=10,padx=10,width=400)
activeld_no4 = Label(div5,bg='#1d201f',fg='white',font=fdisp1, pady=5)
activeld_no4.grid(row=0,column=0, sticky='w')
activeld4 = Label(div5, bg='#1d201f',fg='white', text='   Staffs    ',font=fdisp2)
activeld4.grid(row=1,column=0, sticky='w')
minfo4 = Button(div5,bg='#1d201f',relief=FLAT, fg='white',pady=2,text="More info",command=consinermange)
minfo4.grid(row=3,column=0)
div5.grid(column=8, row=0)
Label(semidashb,text=' ').grid(row=0, column=9,sticky='w')

div6= Frame(semidashb, bg='#51f5b1',pady=10,padx=10,width=400)
activeld_no5 = Label(div6,bg='#51f5b1',fg='white',font=fdisp1, pady=5)
activeld_no5.grid(row=0,column=0, sticky='w')
activeld5 = Label(div6, bg='#51f5b1',fg='white', text='   Viecles   ',font=fdisp2)
activeld5.grid(row=1,column=0, sticky='w')
minfo5 = Button(div6,bg='#51f5b1',relief=FLAT,pady=2, fg='white',text="More info",command=drivermange)
minfo5.grid(row=3,column=0)
div6.grid(column=10, row=0)
Label(semidashb,text=' ').grid(row=0, column=11,sticky='w')

div7= Frame(semidashb, bg='#341ff5',pady=10,padx=10,width=400)
activeld_no6 = Label(div7,background='#341ff5',fg='white',font=fdisp1, pady=5)
activeld_no6.grid(row=0,column=0, sticky='w')
activeld6 = Label(div7, bg='#341ff5',fg='white', text='  Passengers ',font=fdisp2)
activeld6.grid(row=1,column=0, sticky='w')
minfo6 = Button(div7,bg='#341ff5',relief=FLAT,pady=2, fg='white',text="More info",command=viewReport)
minfo6.grid(row=3,column=0)
div7.grid(column=12, row=0)

semidashb.pack(fill= BOTH)

section = Frame(Dashboard, bg='#eee',background='gray')
div8 = Label(section,text="Active Load details",font=fdisp1)
div8.pack()
section.pack()
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading', background='#3b3838', foreground='#eee', font=font1b)
nextsemidb = Frame(Dashboard,pady=10,width=mainwidt)
columns = ('#', 'Viecle No', 'Driver Name', 'Driver Phone', 'Consigner', 'Load Date', 'City From', 'City To', 'Date')

tree = ttk.Treeview(nextsemidb, columns=columns, show='headings', height=25)
tree.grid(row=1, column=0, sticky='nsew')

# define headings

searchfram = Frame(nextsemidb)
searchfram.grid(row=3,column=0,sticky="w")
search = Entry(searchfram, width=50)
search.grid(row=3,column=0,sticky="w")
# deletebu = Button(searchfram,text='Delete',bg='green')
# deletebu.grid(row=3,column=1)

# add a scrollbar
scrollbar = ttk.Scrollbar(nextsemidb, orient=VERTICAL, command=tree.yview,)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=3, sticky='ns')

tree.heading('#', text='Id No')
tree.heading('Viecle No', text='Viecle No')
tree.heading('Driver Name', text='Driver Name')
tree.heading('Consigner', text='Consigner')
tree.heading('Driver Phone', text='Driver Phone')
tree.heading('Load Date', text='Load Date')
tree.heading('City From', text='City From')
tree.heading('City To', text='City To')
tree.heading('Date', text='Date')
tree.heading('Date', text='Date')

tree.column('0', width=100, anchor='c')
tree.column('1', width=100, anchor='c')
tree.column('2', width=100, anchor='c')
tree.column('3', width=100, anchor='c')
tree.column('4', width=100, anchor='c')
tree.column('5', width=100, anchor='c')
tree.column('6', width=100, anchor='c')
tree.column('7', width=100, anchor='c')
tree.column('8', width=150, anchor='c')
nextsemidb.pack(fill= BOTH, expand = True)

# Rpsearchfram = Frame(nextsemidb)
# Rpsearchfram.grid(row=3,column=0,sticky="w")
#
# search = Label(Rpsearchfram, width=50,text='Cash Deposite Total =')
# search.grid(row=3,column=0,sticky="w")
# deletebu = Label(Rpsearchfram,text='Delete',bg='green')
# deletebu.grid(row=3,column=1)
# --------------------------------------------------------------------------------------
# REPORT SECTION WHERE WE GET ALL THE DATA BOTH FINANCIAL AND
Report = Frame(workframe,pady=10)
subreport = Frame(Report)
subreport.pack(fill= BOTH, expand = True)
columnrp = ('#', 'Driverid', 'Passengers num', 'Number of trips', 'Bus number',
           'location/from/to', 'Cash deposit', 'Driver debt', 'Tripstate', 'Date')
tree10 = ttk.Treeview(subreport, columns=columnrp, show='headings', height=15)
tree10.grid(row=1, column=0, sticky='nsew')

scrollbar10 = ttk.Scrollbar(subreport, orient=VERTICAL, command=tree10.yview, )
tree10.configure(yscroll=scrollbar10.set)
scrollbar10.grid(row=1, column=3, sticky='ns')

tree10.heading('#', text='S/N')
tree10.heading('Driverid', text='Driverid')
tree10.heading('Passengers num', text='Passengers num')
tree10.heading('Number of trips', text='Number of trips')
tree10.heading('Bus number', text='Bus number')
tree10.heading('location/from/to', text='location/from/to')
tree10.heading('Cash deposit', text='Cash deposit')
tree10.heading('Driver debt', text='Driver debt')
tree10.heading('Tripstate', text='Tripstate')
tree10.heading('Date', text='Date')

tree10.column('0', width=80, anchor='c')
tree10.column('1', width=100, anchor='c')
tree10.column('2', width=100, anchor='c')
tree10.column('3', width=100, anchor='c')
tree10.column('4', width=100, anchor='c')
tree10.column('5', width=100, anchor='c')
tree10.column('6', width=100, anchor='c')
tree10.column('7', width=100, anchor='c')
tree10.column('8', width=200, anchor='c')

Rpsearchfram = Frame(subreport)
Rpsearchfram.grid(row=3,column=0,sticky="w")

cdep = Label(Rpsearchfram, text='Cash Deposite Total =')
cdep.grid(row=3,column=0,sticky="w")
cdepdisp = Label(Rpsearchfram,text='N')
cdepdisp.grid(row=3,column=1)

cdep1 = Label(Rpsearchfram, text='Drivers Dept Total =')
cdep1.grid(row=3,column=2,sticky="w")
cdepdisp1 = Label(Rpsearchfram,text='N')
cdepdisp1.grid(row=3,column=3)

cdep2 = Label(Rpsearchfram,text='Total passengers  =')
cdep2.grid(row=3,column=4,sticky="w")
cdepdisp2 = Label(Rpsearchfram,text='N')
cdepdisp2.grid(row=3,column=5)

# LOADING DEATILS ARE STATED HERE THIS IS WHERE EACH DRIVERS MOVEMENT IS TRACKED
Loading_details = Frame(workframe, bg='#eee',pady=5,padx=10)
# assign_section = Frame(Loading_details, bg='#eee')
loadReg = Frame(Loading_details, bg='#eee')
loadReg.place(relx=0, rely=0.01)
themaincont = Frame(loadReg)
themaincont.grid(row=1,column=1)

Label(themaincont,text='Loading Trips').grid(row=0,column=1)

thecontent2 = Frame(themaincont,padx=10)
thecontent2.grid(row=1,column=1,sticky='e')

Label(themaincont,text='Active Trips').grid(row=2,column=1)

thecontent3 = Frame(themaincont,padx=10)
thecontent3.grid(row=3,column=1,sticky='e')

thecontent1 = Frame(loadReg,background='#eee')
thecontent1.grid(row=1, column=0, sticky="w")
loadtitle = Frame(thecontent1)
loadbut1 = Button(loadtitle, text='Completed Load', fg='white',bg='green')
loadbut1.grid(row=0,column=1)
Label(loadtitle,text='    ').grid(row=0, column=2,sticky='w')
loadbut2 = Button(loadtitle, text='Update',fg='white',bg='green', command=updatetheload)
loadbut2.grid(row=0,column=3)

loddet = Label(loadtitle, text='Load Details',padx=40)
loddet.grid(row=0, column=0)
loadtitle.grid(row=0,column=0,sticky=E)

n= StringVar()
loddet1 = Label(thecontent1,font=font2, text='Driver Id',bd=3,pady=10)
loddet2 = Label(thecontent1,font=font2, text='Number of Passengers',bd=3,pady=10)
loddet3= Label(thecontent1,font=font2, text='Trip Number',bd=3,pady=10)
loddet4 = Label(thecontent1,font=font2, text='BUS number',bd=3,pady=10)
loddet5 = Label(thecontent1,font=font2, text='Cash deposit',bd=3,pady=10)
loddet6 = Label(thecontent1,font=font2, text='Drivers dept',bd=3,pady=10)
loddet7 = Label(thecontent1,font=font2, text='Load Date',bd=3,pady=10)
loddet8 = Label(thecontent1,font=font2, text='Load From',bd=3,pady=10)
loddet9 = Label(thecontent1,font=font2, text='Load To',bd=3,pady=10)
loddet10 = Label(thecontent1,font=font2, text='Consigner',bd=3,pady=10)
loddet11 = Label(thecontent1,font=font2, text='Active Phone number',bd=3,pady=10)
loddet12= Label(thecontent1,font=font2, text='Trip state',bd=3,pady=10)

loadin1= Entry(thecontent1,font=font2,width=30, bd=3)
loadin2= Entry(thecontent1,font=font2,width=30, bd=3)
loadin3= ttk.Combobox(thecontent1,width=20,textvariable=n)
loadin3['values']= (1,2,3,4,5,6,7,8,9,10)
loadin3.current(1)
loadin4= Entry(thecontent1,font=font2,width=30, bd=3)
loadin5= Entry(thecontent1,font=font2,width=30, bd=3)
loadin6= Entry(thecontent1,font=font2,width=30, bd=3)
loadin7= Entry(thecontent1,font=font2,width=30, bd=3)
loadin8= Entry(thecontent1,font=font2,width=30, bd=3)
loadin9= Entry(thecontent1,font=font2,width=30, bd=3)
loadin10= Entry(thecontent1,font=font2,width=30, bd=3)
loadin11= Entry(thecontent1,font=font2,width=30, bd=3)
k=StringVar()
loadin12= ttk.Combobox(thecontent1,width=20,textvariable=k)
loadin12['values']= ('Active','Loading','Arrived')
loadin12.current(1)

loddet1.grid(row=1,column=0,sticky=W)
loadin1.grid(row=1, column=1,sticky=W)
loddet2.grid(row=2,column=0,sticky=W)
loadin2.grid(row=2, column=1,sticky=W)
loddet3.grid(row=3,column=0,sticky=W)
loadin3.grid(row=3, column=1,sticky=W)
loddet4.grid(row=4,column=0,sticky=W)
loadin4.grid(row=4, column=1,sticky=W)
loddet5.grid(row=5,column=0,sticky=W)
loadin5.grid(row=5, column=1,sticky=W)
loddet6.grid(row=6,column=0,sticky=W)
loadin6.grid(row=6, column=1,sticky=W)
loddet7.grid(row=7,column=0,sticky=W)
loadin7.grid(row=7, column=1,sticky=W)
loddet8.grid(row=8,column=0,sticky=W)
loadin8.grid(row=8, column=1,sticky=W)
loddet9.grid(row=9,column=0,sticky=W)
loadin9.grid(row=9, column=1,sticky=W)
loddet10.grid(row=10,column=0,sticky=W)
loadin10.grid(row=10, column=1,sticky=W)
loddet11.grid(row=11,column=0,sticky=W)
loadin11.grid(row=11, column=1,sticky=W)
loddet12.grid(row=12,column=0,sticky=W)
loadin12.grid(row=12, column=1,sticky=W)

columns3 = (
'#', 'Driver Id', 'Location From', 'Location To', 'Consigner')

tree3 = ttk.Treeview(thecontent2, columns=columns3, show='headings', height=10)
searchfram3 = Frame(thecontent2)
searchfram3.grid(row=3,column=0,sticky="w")

acttivate = Button(searchfram3,text='Activate',bg='orange',fg='white',command=selectitem)
acttivate.grid(row=3,column=0,sticky="w")

tree3.grid(row=0, column=0, sticky='nsew')
# add a scrollbar
scrollbar3 = ttk.Scrollbar(thecontent2, orient=VERTICAL, command=tree3.yview,)
tree3.configure(yscroll=scrollbar3.set)
scrollbar3.grid(row=0, column=3, sticky='ns')
# 'Bus name', 'Bus price', 'Plate Number', 'Condition','Driver'


tree3.heading('#', text='Id No')
tree3.heading('Driver Id', text='Driver id')
tree3.heading('Location From', text='Location From')
tree3.heading('Location To', text='Location To')
tree3.heading('Consigner', text='Consigner')


tree3.column('0', width=80, anchor='c')
tree3.column('1', width=100, anchor='c')
tree3.column('2', width=100, anchor='c')
tree3.column('3', width=100, anchor='c')
tree3.column('4', width=100, anchor='c')

columns4 = (
'#', 'Driver Id', 'Location From', 'Location To', 'Consigner')

tree4 = ttk.Treeview(thecontent3, columns=columns4, show='headings', height=5)
tree4.grid(row=0, column=0, sticky='nsew')
deletebu4 = Button(thecontent3,text='Delete',bg='green',command=delactivate)
deletebu4.grid(row=1,column=0)
# add a scrollbar
scrollbar4 = ttk.Scrollbar(thecontent3, orient=VERTICAL, command=tree4.yview,)
tree4.configure(yscroll=scrollbar4.set)
scrollbar4.grid(row=1, column=3, sticky='ns')

tree4.heading('#', text='Id No')
tree4.heading('Driver Id', text='Driver id')
tree4.heading('Location From', text='Location From')
tree4.heading('Location To', text='Location To')
tree4.heading('Consigner', text='Consigner')


tree4.column('0', width=80, anchor='c')
tree4.column('1', width=100, anchor='c')
tree4.column('2', width=100, anchor='c')
tree4.column('3', width=100, anchor='c')
tree4.column('4', width=100, anchor='c')


# Loading_details.pack(fill= BOTH, expand = True)
# THIS IS THE STAFF MANAGEMENT AND DRIVERS SECTION ONLY
Consinger_addstaff= Frame(workframe)
#THIS IS THE ADMIN REGISTRATION CENTER ALL YOU NEED TO DO IS JUST SIGN UP
adminreg = Frame(Consinger_addstaff,bg='#09003b',height=700, width=800, bd=0, padx=20)
# adminreg.pack()
log_head = Label(adminreg, text='ADMIN - SIGN UP',font=font1,bg='#09003b',fg='lime' )
Fname_box = Label(adminreg, text='First name:', bg='#09003b',fg='white',font=font2)
Lname_box = Label(adminreg, text='Last name:', bg='#09003b',fg='white',font=font2 )
email = Label(adminreg, text='Email:',bg='#09003b',fg='white',font=font2  )
phoneno = Label(adminreg, text='Phone number',bg='#09003b',fg='white',font=font2 )
gender = Label(adminreg, text='Gender:',bg='#09003b',fg='white',font=font2 )
pass_word = Label(adminreg, text='Password:',bg='#09003b',fg='white',font=font2  )
cpass_word = Label(adminreg, text='Confirm Password:',bg='#09003b',fg='white',font=font2 )
office = Label(adminreg, text="Office",bg='#09003b',fg='white',font=font2 )
salary1 = Label(adminreg, text="Salary",bg='#09003b',fg='white',font=font2 )
Address= Label(adminreg, text="Home Address",bg='#09003b',fg='white',font=font2 )

fnam = Entry(adminreg,insertbackground='white',background='#09003b',font=font3,foreground='#fff',width=30)
lastnam = Entry(adminreg,insertbackground='white', background='#09003b',font=font3,foreground='#fff',width=30)
emailin = Entry(adminreg,insertbackground='white', background='#09003b',font=font3,foreground='#fff',width=30)
phonein = Entry(adminreg,insertbackground='white',background='#09003b',font=font3,foreground='#fff',width=30 )
gen = ttk.Radiobutton(adminreg,text='Male',variable=genderdb,value='male')
gen2 = ttk.Radiobutton(adminreg,text='Female',variable=genderdb,value='female')
pass1 = Entry(adminreg,insertbackground='white', show='*',background='#09003b',font=font3,foreground='#fff',width=30 )
pass2 = Entry(adminreg,insertbackground='white', show='*',background='#09003b',font=font3,foreground='#fff',width=30  )
office2 = Entry(adminreg,insertbackground='white',  background='#09003b',font=font3,foreground='#fff',width=30)
Salary = Entry(adminreg,insertbackground='white',  background='#09003b',font=font3,foreground='#fff',width=30)
addressin = Entry(adminreg,insertbackground='white',  background='#09003b',font=font3,foreground='#fff',width=30)
reg_new_user = Button(adminreg, text='Add Staff',bg='#ff008c',fg='#fff',font=font2,activebackground='green',width=15,command=newstaff)
cancel = Button(adminreg, text='Cancle', bg='#ff008c', fg='#fff', font=font2, activebackground='green', width=15, command=canclestaffnav)
#---------------------------- ADMIN PLACE SECTION
log_head.place(relx=0.3, rely=0.04,anchor=CENTER)
Fname_box.place(relx=0.25, rely=0.1,anchor=S)
fnam.place(relx=0.21, rely=0.15,anchor=SW)
Lname_box.place(relx=0.24, rely=0.2,anchor=S)
lastnam.place(relx=0.21, rely=0.25,anchor=SW)
email.place(relx=0.23, rely=0.3,anchor=S)
emailin.place(relx=0.21, rely=0.35,anchor=SW)
phoneno.place(relx=0.25, rely=0.4,anchor=S)
phonein.place(relx=0.21, rely=0.45,anchor=SW)
gender.place(relx=0.25, rely=0.5,anchor=S)
gen.place(relx=0.3, rely=0.55,anchor=SW)
gen2.place(relx=0.42, rely=0.55,anchor=S)
pass_word.place(relx=0.24, rely=0.6,anchor=S)
pass1.place(relx=0.21, rely=0.65,anchor=SW)
cpass_word.place(relx=0.26, rely=0.7,anchor=S)
pass2.place(relx=0.21, rely=0.75,anchor=SW)
office.place(relx=0.21, rely=0.8,anchor=S)
office2.place(relx=0.21, rely=0.85,anchor=SW)
salary1.place(relx=0.21, rely=0.9,anchor=S)
Salary.place(relx=0.21, rely=0.95,anchor=SW)
Address.place(relx=0.55, rely=0.5,anchor=S)
addressin.place(relx=0.5, rely=0.55,anchor=SW)
reg_new_user.place(relx=0.8, rely=0.3,anchor=S)
cancel.place(relx=0.8, rely=0.4,anchor=S)


# DISPLAY THE STAFFS
displayconsingers = Frame(Consinger_addstaff, background='#eee')
columns5 = (
'#', 'Staffs FName','Staffs LName', 'E-mail', 'Phone N0', 'Gender','Password','Office','Salary','Date of Appointment','Home Addr')
disph1 = Label(displayconsingers,text='STAFFS DATA',font=font3)
disph1.place(relx=0.09, rely=0.09,anchor=S)
# disph1.grid(row=0, column=0,sticky='nsew')

tree5 = ttk.Treeview(displayconsingers, columns=columns5, show='headings', height=18)
tree5.place(relx=0.5, rely=0.4,anchor=CENTER)
# define headings

def update():
    for item in tree5.get_children():
        tree5.delete(item)
    inconnection = sqlite3.connect("aktc_main.db")
    icursor = inconnection.cursor()
    icursor.execute("SELECT Staffid,Fname,Lname,Email,Phoneno,Gender,Password,Office,Salary,Date,Address FROM stafflist")
    tt5= icursor.fetchall()
    chek5 = len(tt5)
    for contact5 in tt5:
        tree5.insert('', END, values=contact5)

searchfram5 = Frame(displayconsingers,padx=10,pady=20,bg='#341ff5')
searchfram5.place(relx=0.15, rely=1,anchor=S)
sboxtitle = Label(searchfram5,text='',bg='#341ff5')

deletebu5 = Button(searchfram5,text='Delete',bg='red',fg="white",font=f5,command=deletexcessstaff)
deletebu5.grid(row=3,column=0,sticky='w')
Label(searchfram5,text=' ',bg="#341ff5").grid(row=3, column=1,sticky='w')
AddStaff = Button(searchfram5, text='AddStaff', bg='orange', fg="white", font=f5, command=addstaffnav)
AddStaff.grid(row=3,column=2,sticky='w')
Label(searchfram5,text=' ',bg="#341ff5").grid(row=3, column=3,sticky='w')
updtStaff = Button(searchfram5, text='Update', bg='orange', fg="white", font=f5, command=update)
updtStaff.grid(row=3,column=4,sticky='w')

# add a scrollbar
scrollbar5 = ttk.Scrollbar(displayconsingers, orient=VERTICAL, command=tree5.yview,)
scrollbar5.place(relx=0.95, rely=0.4, anchor='n')
# Staffid,Fname,Lname,Email,Phoneno,Gender,Password,Office,Salary,Date
tree5.configure(yscroll=scrollbar5.set)
tree5.heading('#', text='Id No')
tree5.heading('Staffs FName', text='Staff Fname')
tree5.heading('Staffs LName', text='Staff LName')
tree5.heading('E-mail', text='E-mail')
tree5.heading('Phone N0', text='Phone N0')
tree5.heading('Gender', text='Gender')
tree5.heading('Password', text='Password')
tree5.heading('Office', text='Office')
tree5.heading('Salary', text='Payment')
tree5.heading('Date of Appointment', text='Date of Aptm')
tree5.heading('Home Addr', text='Home Addr')

tree5.column('0', width=80, anchor='c')
tree5.column('1', width=100, anchor='c')
tree5.column('2', width=100, anchor='c')
tree5.column('3', width=100, anchor='c')
tree5.column('4', width=100, anchor='c')
tree5.column('5', width=100, anchor='c')
tree5.column('6', width=100, anchor='c')
tree5.column('7', width=100, anchor='w')
tree5.column('8', width=100, anchor='c')
tree5.column('9', width=100, anchor='c')
tree5.column('10', width=100, anchor='c')

# displayconsingers.pack(fill= BOTH, expand = True)

# DRIVERS SECTION IN THE THAT SECTION
DriverManagement = Frame(workframe)
displayDrivers = Frame(DriverManagement)
columns6 = (
'#', 'Drivers Name', 'E-mail', 'Phone N0', 'Gender','Drivers Id','State_origin','Appointment Date','Licence No')
disph2 = Label(displayDrivers,text='DRIVERS DATA',font=font3)
disph2.place(relx=0.09, rely=0.09,anchor=S)

tdisplay= Frame(displayDrivers)
tdisplay.place(relx=0.5, rely=0.4,anchor=CENTER)
tree6 = ttk.Treeview(tdisplay, columns=columns6, show='headings', height=18)
tree6.grid(row=0, column=0)


searchfram6 = Frame(displayDrivers,padx=10,pady=20,bg='#341ff5')
searchfram6.place(relx=0.15, rely=1,anchor=S)
sboxtitle2= Label(searchfram6,text='Refrence')
sboxtitle.grid(row=3,column=0,sticky='w')
deletebu6 = Button(searchfram6,text='Delete',bg='red',fg="white",font=f5,command=driverdel)
deletebu6.grid(row=4,column=0,sticky='w')
Label(searchfram5,text=' ',bg="#341ff5").grid(row=4, column=1,sticky='w')
AddDriver = Button(searchfram6,text='AddDriver',bg='orange',fg="white",font=f5,command=adddrive)
AddDriver.grid(row=4,column=2,sticky='w')


# tree6.grid(row=0, column=1,columnspan=2,rowspan=2,sticky='nsew')

# add a scrollbar
scrollbar6 = ttk.Scrollbar(tdisplay, orient=VERTICAL, command=tree6.yview,)
scrollbar6.grid(row=0,column=1)
# Driverid,Name,Email,Phoneno,Gender,DrivOfficeid,State_origin,Date,Address,Licenses_no
tree6.configure(yscroll=scrollbar6.set)
tree6.heading('#', text='Id')
tree6.heading('Drivers Name', text='Drivers Name')
tree6.heading('E-mail', text='E-mail')
tree6.heading('Phone N0', text='Phone N0')
tree6.heading('Gender', text='Gender')
tree6.heading('Drivers Id', text='Drivers Id')
tree6.heading('State_origin', text='State_origin')
tree6.heading('Appointment Date', text='Appt Date')
tree6.heading('Licence No', text='Licence No')


tree6.column('0', width=60, anchor='c')
tree6.column('1', width=100, anchor='c')
tree6.column('2', width=150, anchor='c')
tree6.column('3', width=90, anchor='c')
tree6.column('4', width=70, anchor='c')
tree6.column('5', width=90, anchor='c')
tree6.column('6', width=90, anchor='c')
tree6.column('7', width=100, anchor='w')
tree6.column('8', width=100, anchor='c')

# displayDrivers.pack(fill= BOTH, expand = True)
addNdriver = Frame(DriverManagement, bg='#eee', pady=5, padx=10)
# assign_section = Frame(Loading_details, bg='#eee')
drivloadreg = Frame(addNdriver, bg='#eee')
drivloadreg.place(relx=0, rely=0.01)
themaincontd = Frame(drivloadreg)
themaincontd.grid(row=1, column=1)
thecontentd2 = Frame(themaincontd, padx=10)
thecontentd2.grid(row=1, column=1, sticky='e')
Label(themaincontd, text=' ').grid(row=2, column=1)
thecontentd3 = Frame(themaincontd, padx=10)
thecontentd3.grid(row=3, column=1, sticky='w')

thecontentd1 = Frame(drivloadreg, background='#eee')
thecontentd1.grid(row=1, column=0, sticky="w")
loadtitled = Frame(thecontentd1)
loadbut1d = Button(loadtitled, text='View Drivers', fg='white', bg='#341ff5',command=drivenavb)
loadbut1d.grid(row=0, column=1)
Label(loadtitled, text='    ').grid(row=0, column=2, sticky='w')
loadbut2d = Button(loadtitled, text='Update', fg='white', bg='#341ff5',command=Driverregisterd)
loadbut2d.grid(row=0, column=3)

loddetd = Label(loadtitled, text='Load Details', padx=40)
loddetd.grid(row=0, column=0)
loadtitled.grid(row=0, column=0, sticky=E)

selectitem= StringVar()
selectitem2= StringVar()
loddetd1 = Label(thecontentd1, font=font2, text='Driver Name', bd=3, pady=10)
loddetd2 = Label(thecontentd1, font=font2, text='Email', bd=3, pady=10)
loddetd3= Label(thecontentd1, font=font2, text='Gender', bd=3, pady=10)
loddetd4 = Label(thecontentd1, font=font2, text='Phone No', bd=3, pady=10)
loddetd5 = Label(thecontentd1, font=font2, text='Drivers Id', bd=3, pady=10)
loddetd6 = Label(thecontentd1, font=font2, text='State of Origin', bd=3, pady=10)
loddetd7 = Label(thecontentd1, font=font2, text='L.G.A of Origin', bd=3, pady=10)
loddetd8 = Label(thecontentd1, font=font2, text='Salary', bd=3, pady=10)
loddetd9 = Label(thecontentd1, font=font2, text='Licenses No', bd=3, pady=10)
loddetd10 = Label(thecontentd1, font=font2, text='Marital Status', bd=3, pady=10)
loddetd11 = Label(thecontentd1, font=font2, text='Date of Birth', bd=3, pady=10)
loddetd12= Label(thecontentd1, font=font2, text='Years of Experience', bd=3, pady=10)

loadind1= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind2= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind3= ttk.Combobox(thecontentd1, width=20, textvariable=selectitem)
loadind3['values']= ('Male','Female','Others')
loadind3.current(1)
loadind4= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind5= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind6= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind7= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind8= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind9= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind10= ttk.Combobox(thecontentd1, width=20, textvariable=selectitem2)
loadind10['values']= ('Single','Married','Divorced')
loadind10.current(1)
loadind11= Entry(thecontentd1, font=font2, width=30, bd=3)
loadind12= Entry(thecontentd1, font=font2, width=30, bd=3)

loddetd1.grid(row=1,column=0,sticky=W)
loadind1.grid(row=1, column=1,sticky=W)
loddetd2.grid(row=2,column=0,sticky=W)
loadind2.grid(row=2, column=1,sticky=W)
loddetd3.grid(row=3,column=0,sticky=W)
loadind3.grid(row=3, column=1,sticky=W)
loddetd4.grid(row=4,column=0,sticky=W)
loadind4.grid(row=4, column=1,sticky=W)
loddetd5.grid(row=5,column=0,sticky=W)
loadind5.grid(row=5, column=1,sticky=W)
loddetd6.grid(row=6,column=0,sticky=W)
loadind6.grid(row=6, column=1,sticky=W)
loddetd7.grid(row=7,column=0,sticky=W)
loadind7.grid(row=7, column=1,sticky=W)
loddetd8.grid(row=8,column=0,sticky=W)
loadind8.grid(row=8, column=1,sticky=W)
loddetd9.grid(row=9,column=0,sticky=W)
loadind9.grid(row=9, column=1,sticky=W)
loddetd10.grid(row=10,column=0,sticky=W)
loadind10.grid(row=10, column=1,sticky=W)
loddetd11.grid(row=11,column=0,sticky=W)
loadind11.grid(row=11, column=1,sticky=W)
loddetd12.grid(row=12,column=0,sticky=W)
loadind12.grid(row=12, column=1,sticky=W)

columnsd3 = (
'#', 'Bus name', 'Bus price', 'Plate Number', 'Condition','Driver')

treed3 = ttk.Treeview(thecontentd2, columns=columnsd3, show='headings', height=10)

searchframd3 = Frame(thecontentd2)
searchframd3.grid(row=3, column=0, sticky="w")
deletebud3 = Button(searchframd3, text='Delete', bg='#341ff5',fg='white')
deletebud3.grid(row=3, column=1)

treed3.grid(row=0, column=0, sticky='nsew')
# add a scrollbar
scrollbard3 = ttk.Scrollbar(thecontentd2, orient=VERTICAL, command=treed3.yview, )
treed3.configure(yscroll=scrollbard3.set)
scrollbard3.grid(row=0, column=3, sticky='ns')
treed3.heading('#', text='Id No')
treed3.heading('Bus name', text='Bus name')
treed3.heading('Bus price', text='Bus price')
treed3.heading('Plate Number', text='Plate Number')
treed3.heading('Condition', text='Condition')
treed3.heading('Driver', text='Driver')

treed3.column('0', width=70, anchor='c')
treed3.column('1', width=100, anchor='c')
treed3.column('2', width=80, anchor='c')
treed3.column('3', width=100, anchor='c')
treed3.column('4', width=100, anchor='c')
treed3.column('5', width=80, anchor='c')

searchfram4d = Frame(thecontentd2)
searchfram4d.grid(row=3, column=0, sticky="w")
deletebu4d = Button(searchfram4d, text='Delete', bg='#341ff5',fg='white')
deletebu4d.grid(row=3, column=1)

# THE SIDE FOR THE ACTIVE DRIVERS AND THE NON ACTIVE DRIVERS
treed4 = Frame(thecontentd3,)

loddetb1 = Label(treed4, font=font2, text='Veicle Name', bd=3, pady=10)
loddetb2 = Label(treed4, font=font2, text='Veicle Price', bd=3, pady=10)
loddetb3= Label(treed4, font=font2, text='Plate Number', bd=3, pady=10)
loddetb4 = Label(treed4, font=font2, text='Condition', bd=3, pady=10)
loddetb5 = Label(treed4, font=font2, text='Driver', bd=3, pady=10)

loadinb1= Entry(treed4, font=font2, width=30, bd=3)
loadinb2= Entry(treed4, font=font2, width=30, bd=3)
loadinb3= Entry(treed4, font=font2, width=30, bd=3)
loadinb4= ttk.Combobox(treed4, width=20)
loadinb4['values']= ('Ready','Maintainace','Not ready')
loadinb4.current(1)
loadinb5= Entry(treed4, font=font2, width=30, bd=3)

loadinb6= Button(treed4, text='Update',relief=RAISED, fg='white',bg='#341ff5',padx=1,command=RegisterBuses)

loddetb1.grid(row=1,column=0,sticky=W)
loadinb1.grid(row=1, column=1,sticky=W)
loddetb2.grid(row=2,column=0,sticky=W)
loadinb2.grid(row=2, column=1,sticky=W)
loddetb3.grid(row=3,column=0,sticky=W)
loadinb3.grid(row=3, column=1,sticky=W)
loddetb4.grid(row=4,column=0,sticky=W)
loadinb4.grid(row=4, column=1,sticky=W)
loddetb5.grid(row=5,column=0,sticky=W)
loadinb5.grid(row=5, column=1,sticky=W)
loadinb6.grid(row=3, column=2,sticky=W)
treed4.grid(row=0, column=0, sticky='nsew')

# THIS IS MY PROFILE AND IT SHOWS ALL THE PROFILE IN THE WORK
ProfileManger= ttk.Frame(workframe)
Profile = Frame(ProfileManger,padx=10)
resetArea = Frame(Profile, pady=10,padx=10)
loddetp1 = Label(Profile, font=font2, text='Name', bd=3, pady=10)
loddetp2 = Label(Profile, font=font2, text='Email', bd=3, pady=10)
loddetp3= Label(Profile, font=font2, text='Phone Number:', bd=3, pady=10)
loddetp4 = Label(Profile, font=font2, text='Male', bd=3, pady=10)
loddetp5 = Label(Profile, font=font2, text='Password', bd=3, pady=10)
loddetp6 = Label(Profile, font=font2, text='Position/ Office', bd=3, pady=10)
loddetp7 = Label(Profile, font=font2, text='Salary', bd=3, pady=10)
loddetp8 = Label(Profile, font=font2, text='Address', bd=3, pady=10)
loddetp9 = Label(Profile, font=font2, text='Date of Employment', bd=3, pady=10)

loadinp1= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp2= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp3= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp4= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp5= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp6= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp7= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp8= Label(Profile, font=font2, text='Name', bd=3, pady=10)
loadinp9= Label(Profile, font=font2, text='Name', bd=3, pady=10)

password_reset = Button(Profile, text='Reset Admin password',command=showsetpassword)

pasrst_title = Label(resetArea, text='Reset Admin Password')
pasrst_title.grid(row=0,column=2, rowspan=3)
newpass = Label(resetArea, text='Enter New Password:')
newpass.grid(row=1,column=0,)
newpassin= Entry(resetArea, font=font2, width=30, bd=3)
newpassin.grid(row=1,column=2)

confirmpass = Label(resetArea, text='Confirm New Password:')
confirmpass.grid(row=2,column=0,)

confirmpassin= Entry(resetArea, font=font2, width=30, bd=3)
confirmpassin.grid(row=3,column=2,)

changepas = Button(resetArea, text='Update Password',command=setpassdb)
changepas.grid(row=3,column=1)
loddetp1.grid(row=1,column=0,sticky=W)
loadinp1.grid(row=1, column=1,sticky=W)
loddetp2.grid(row=2,column=0,sticky=W)
loadinp2.grid(row=2, column=1,sticky=W)
loddetp3.grid(row=3,column=0,sticky=W)
loadinp3.grid(row=3, column=1,sticky=W)
loddetp4.grid(row=4,column=0,sticky=W)
loadinp4.grid(row=4, column=1,sticky=W)
loddetp5.grid(row=5,column=0,sticky=W)
loadinp5.grid(row=5, column=1,sticky=W)
loddetp6.grid(row=6,column=0,sticky=W)
loadinp6.grid(row=6, column=1,sticky=W)
loddetp7.grid(row=7,column=0,sticky=W)
loadinp7.grid(row=7, column=1,sticky=W)
loddetp8.grid(row=8,column=0,sticky=W)
loadinp8.grid(row=8, column=1,sticky=W)
loddetp9.grid(row=9,column=0,sticky=W)
loadinp9.grid(row=9, column=1,sticky=W)
password_reset.grid(row=10,column=0,sticky=W)


# Profile.pack(fill= BOTH, expand = True)
# ProfileManger.pack(fill= BOTH, expand = True)

#THIS IS MY LOG- IN FRAME  AND  THE TEXT PATTERNS
loginFr= Frame(sub_frm, bg='white',height=700, width=400, bd=0, )
loginFr.grid(row=0, column=2, sticky='ew', padx=10)



slideframe= Frame(sub_frm, height=700, width=500,bg='black')
slideframe.grid(row=0, column=1, padx=10,sticky='ne')

backgsrc = PhotoImage(file= 'img/bg1.png')
backg= backgsrc.subsample(9, 12)
thelogosld = Label(slideframe, image=backg,justify=LEFT, bd=0)
thelogosld.grid(row=0,column=0,sticky="n")
titlewrt = Label(slideframe,text='Our Mission And Vision State',bg='#09003b',fg='white',font= Font(family='comic',size=10,weight='bold',slant='roman', ), justify=CENTER)
titlewrt.grid(row=2,column=0)

write_ups = '''
    'Our mission is to help and sponsor students who are not able due to one case or the other and indigent
     persons achieve their GOD given gifts and also come to the aid of person who needs help; 
     with our system to monitor the activities of our delings'
'''
imgtextwrt = Label(slideframe,text=write_ups,font=font1b, justify=CENTER, bg='#09003b',fg='white')
imgtextwrt.grid(row=3,column=0)

# THE HOME OF THE APP IS FROM HERE
mlogo = PhotoImage(file= 'img/mainjpg.png')
logodic= mlogo.subsample(10, 10)

thelogolgn = Label(loginFr, image=logodic, justify=CENTER)
header = Label(loginFr, text='LOG IN',font=font1,bg='#09003b',fg='#E63B60')
header.place(relx=0.5, rely=0.25,anchor=CENTER)
thelogolgn.place(relx=0.5, rely=0.15,anchor=CENTER)
name_box = Label(loginFr, text='Username ', bg='#09003b',fg='white',font=font2)
pass_word = Label(loginFr, text='Password:',bg='#09003b',fg='white',font=font2)
info = Label(loginFr, text= 'if you are new here sign up  ',bg='#09003b',fg='lime',font=font2)
# log in inputs and get value
identver = StringVar()
userver = StringVar()
# INPUTS OF THE FORM
user = Entry(loginFr,insertbackground='white',textvariable=userver,background='#09003b',font=font3,foreground='#fff',width=30)
identity = Entry(loginFr, insertbackground='white', show='*',textvariable=identver,background='#09003b',font=font3,foreground='#fff',width=30)
send = Button(loginFr, text='Log-In',bg='#ff008c',fg='#fff',width=33,font=f4,activebackground='green',command=lognin)
# my grid for the labels
name_box.place(relx=0.2, rely=0.35,anchor=S)
user.place(relx=0.11, rely=0.4,anchor=SW)
pass_word.place(relx=0.2, rely=0.45,anchor=S)
identity.place(relx=0.11, rely=0.5,anchor=SW)
send.place(relx=0.11, rely=0.58,anchor=SW)
# Secondwind.pack( fill= BOTH, expand = True)
Frstframe.pack(fill=BOTH)
wind.mainloop()