From tkinter import *
Import sqlite3
Import tkinter.Ttk as ttk
Import tkinter.Messagebox as tkMessageBox

Root = Tk()
Root.Name("contact list")
Width = seven-hundred
Top = four hundred
Screen_width = root.Winfo_screenwidth()
Screen_height = root.Winfo_screenheight()
X = (screen_width/2) - (width/2)
Y = (screen_height/2) - (top/2)
Root.Geometry("%dxp.Cd+%d+%d" % (width, peak, x, y))
Root.Config(bg="#6666ff")

FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
Address = StringVar()
Contact = StringVar()


Def Database():
    conn = sqlite3.Connect("pythontut.Db")
    cursor = conn.Cursor()
    cursor.Execute("CREATE table IF no longer EXISTS `member` (mem_id INTEGER no longer NULL  primary KEY AUTOINCREMENT, firstname textual content, lastname text, gender text, age textual content, deal with text, touch text)")
    cursor.Execute("select * FROM `member` ORDER with the aid of `lastname` ASC")
    fetch = cursor.Fetchall()
    for records in fetch:
        tree.Insert('', 'quit', values=(statistics))
    cursor.Near()
    conn.Near()

Def SubmitData():
    if  FIRSTNAME.Get() == "" or LASTNAME.Get() == "" or GENDER.Get() == "" or AGE.Get() == "" or deal with.Get() == "" or touch.Get() == "":
        result = tkMessageBox.Showwarning('', 'Please whole the required subject', icon="caution")
    else:
        tree.Delete(*tree.Get_children())
        conn = sqlite3.Join("pythontut.Db")
        cursor = conn.Cursor()
        cursor.Execute("INSERT INTO `member` (firstname, lastname, gender, age, deal with, contact) VALUES(?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.Get()), str(LASTNAME.Get()), str(GENDER.Get()), int(AGE.Get()), str(cope with.Get()), str(contact.Get())))
        conn.Commit()
        cursor.Execute("pick * FROM `member` ORDER by `lastname` ASC")
        fetch = cursor.Fetchall()
        for statistics in fetch:
            tree.Insert('', 'stop', values=(facts))
        cursor.Near()
        conn.Near()
        FIRSTNAME.Set("")
        LASTNAME.Set("")
        GENDER.Set("")
        AGE.Set("")
        address.Set("")
        touch.Set("")

Def UpdateData():
    if GENDER.Get() == "":
       result = tkMessageBox.Showwarning('', 'Please whole the specified field', icon="warning")
    else:
        tree.Delete(*tree.Get_children())
        conn = sqlite3.Connect("pythontut.Db")
        cursor = conn.Cursor()
        cursor.Execute("replace `member` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `deal with` = ?, `touch` = ? Where `mem_id` = ?", (str(FIRSTNAME.Get()), str(LASTNAME.Get()), str(GENDER.Get()), str(AGE.Get()), str(cope with.Get()), str(touch.Get()), int(mem_id)))
        conn.Devote()
        cursor.Execute("pick * FROM `member` ORDER by using `lastname` ASC")
        fetch = cursor.Fetchall()
        for statistics in fetch:
            tree.Insert('', 'end', values=(facts))
        cursor.Close()
        conn.Near()
        FIRSTNAME.Set("")
        LASTNAME.Set("")
        GENDER.Set("")
        AGE.Set("")
        deal with.Set("")
        touch.Set("")
        
    
Def OnSelected(occasion):
    worldwide mem_id, UpdateWindow
    curItem = tree.Recognition()
    contents =(tree.Object(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.Set("")
    LASTNAME.Set("")
    GENDER.Set("")
    AGE.Set("")
    address.Set("")
    touch.Set("")
    FIRSTNAME.Set(selecteditem[1])
    LASTNAME.Set(selecteditem[2])
    AGE.Set(selecteditem[4])
    cope with.Set(selecteditem[5])
    contact.Set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.Identify("contact list")
    width = four hundred
    peak = 300
    screen_width = root.Winfo_screenwidth()
    screen_height = root.Winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)

    UpdateWindow.Geometry("%dxp.Cd+%d+%d" % (width, peak, x, y))
    if 'NewWindow' in globals():
        NewWindow.Wreck()

    FormTitle = body(UpdateWindow)
    FormTitle.P.C.(facet=top)
    ContactForm = frame(UpdateWindow)
    ContactForm.P.C.(side=pinnacle, pady=10)
    RadioGroup = body(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, fee="Male",  font=('arial', 14)).%(facet=LEFT)
    lady = Radiobutton(RadioGroup, textual content="lady", variable=GENDER, price="girl",  font=('arial', 14)).%(facet=LEFT)
    
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.%(fill=X)
    lbl_firstname = Label(ContactForm, textual content="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.Grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 14), bd=five)
    lbl_lastname.Grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.Grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=five)
    lbl_age.Grid(row=three, sticky=W)
    lbl_address = Label(ContactForm, textual content="cope with", font=('arial', 14), bd=five)
    lbl_address.Grid(row=four, sticky=W)
    lbl_contact = Label(ContactForm, text="contact", font=('arial', 14), bd=5)
    lbl_contact.Grid(row=5, sticky=W)

    firstname = access(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.Grid(row=zero, column=1)
    lastname = access(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.Grid(row=1, column=1)
    RadioGroup.Grid(row=2, column=1)
    age = access(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.Grid(row=three, column=1)
    deal with = access(ContactForm, textvariable=address,  font=('arial', 14))
    deal with.Grid(row=4, column=1)
    touch = entry(ContactForm, textvariable=touch,  font=('arial', 14))
    contact.Grid(row=five, column=1)
    

    btn_updatecon = Button(ContactForm, textual content="replace", width=50, command=UpdateData)
    btn_updatecon.Grid(row=6, columnspan=2, pady=10)


Def DeleteData():
    if not tree.Choice():
       end result = tkMessageBox.Showwarning('', 'Please pick some thing First!', icon="warning")
    else:
        end result = tkMessageBox.Askquestion('', 'Are you certain you need to delete this document?', icon="warning")
        if end result == 'sure':
            curItem = tree.Focus()
            contents =(tree.Item(curItem))
            selecteditem = contents['values']
            tree.Delete(curItem) 
            conn = sqlite3.Connect("pythontut.Db")
            cursor = conn.Cursor()
            cursor.Execute("DELETE FROM `member` in which `mem_id` = %d" % selecteditem[0])
            conn.Devote()
            cursor.Close()
            conn.Near()
    
Def AddNewWindow():
    global NewWindow
    FIRSTNAME.Set("")
    LASTNAME.Set("")
    GENDER.Set("")
    AGE.Set("")
    address.Set("")
    contact.Set("")
    NewWindow = Toplevel()
    NewWindow.Identify("touch listing")
    width = 400
    peak = 300
    screen_width = root.Winfo_screenwidth()
    screen_height = root.Winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.Geometry("%dxp.Cd+%d+%d" % (width, peak, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.Destroy()
    
    FormTitle = frame(NewWindow)
    FormTitle.Percent(aspect=pinnacle)
    ContactForm = frame(NewWindow)
    ContactForm.Percent(facet=top, pady=10)
    RadioGroup = body(ContactForm)
    Male = Radiobutton(RadioGroup, textual content="Male", variable=GENDER, value="Male",  font=('arial', 14)).Percent(side=LEFT)
    girl = Radiobutton(RadioGroup, textual content="lady", variable=GENDER, cost="lady",  font=('arial', 14)).%(aspect=LEFT)
    
    
    lbl_title = Label(FormTitle, text="adding New Contacts", font=('arial', sixteen), bg="#66ff66",  width = three hundred)
    lbl_title.P.C.(fill=X)
    lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.Grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, textual content="Lastname", font=('arial', 14), bd=five)
    lbl_lastname.Grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=five)
    lbl_gender.Grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.Grid(row=three, sticky=W)
    lbl_address = Label(ContactForm, text="address", font=('arial', 14), bd=5)
    lbl_address.Grid(row=four, sticky=W)
    lbl_contact = Label(ContactForm, text="contact", font=('arial', 14), bd=five)
    lbl_contact.Grid(row=five, sticky=W)

    firstname = entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.Grid(row=0, column=1)
    lastname = entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.Grid(row=1, column=1)
    RadioGroup.Grid(row=2, column=1)
    age = access(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.Grid(row=3, column=1)
    deal with = access(ContactForm, textvariable=cope with,  font=('arial', 14))
    deal with.Grid(row=4, column=1)
    contact = access(ContactForm, textvariable=touch,  font=('arial', 14))
    contact.Grid(row=five, column=1)
    

    btn_addcon = Button(ContactForm, textual content="save", width=50, command=SubmitData)
    btn_addcon.Grid(row=6, columnspan=2, pady=10)



    

Pinnacle = body(root, width=500, bd=1, relief=strong)
Pinnacle.Percent(facet=top)
Mid = body(root, width=500,  bg="#6666ff")
Mid.P.C.(facet=pinnacle)
MidLeft = frame(Mid, width=a hundred)
MidLeft.P.C.(side=LEFT, pady=10)
MidLeftPadding = frame(Mid, width=370, bg="#6666ff")
MidLeftPadding.Percent(side=LEFT)
MidRight = frame(Mid, width=one hundred)
MidRight.%(facet=right, pady=10)
TableMargin = body(root, width=500)
TableMargin.P.C.(side=pinnacle)
Lbl_title = Label(pinnacle, text="touch control machine", font=('arial', 16), width=500)
Lbl_title.Percent(fill=X)

Btn_add = Button(MidLeft, textual content="+ add NEW", bg="#66ff66", command=AddNewWindow)
Btn_add.Percent()
Btn_delete = Button(MidRight, textual content="DELETE", bg="crimson", command=DeleteData)
Btn_delete.P.C.(side=right)

Scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
Scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
Tree = ttk.Treeview(TableMargin, columns=("MemberID", "Firstname", "Lastname", "Gender", "Age", "cope with", "contact"), height=400, selectmode="prolonged", yscrollcommand=scrollbary.Set, xscrollcommand=scrollbarx.Set)
Scrollbary.Config(command=tree.Yview)
Scrollbary.P.C.(side=right, fill=Y)
Scrollbarx.Config(command=tree.Xview)
Scrollbarx.%(side=backside, fill=X)
Tree.Heading('MemberID', text="MemberID", anchor=W)
Tree.Heading('Firstname', textual content="Firstname", anchor=W)
Tree.Heading('Lastname', text="Lastname", anchor=W)
Tree.Heading('Gender', textual content="Gender", anchor=W)
Tree.Heading('Age', text="Age", anchor=W)
Tree.Heading('address', textual content="deal with", anchor=W)
Tree.Heading('contact', textual content="touch", anchor=W)
Tree.Column('#zero', stretch=NO, minwidth=0, width=0)
Tree.Column('#1', stretch=NO, minwidth=zero, width=0)
Tree.Column('#2', stretch=NO, minwidth=0, width=80)
Tree.Column('#3', stretch=NO, minwidth=zero, width=120)
Tree.Column('#four', stretch=NO, minwidth=0, width=90)
Tree.Column('#5', stretch=NO, minwidth=0, width=eighty)
Tree.Column('#6', stretch=NO, minwidth=zero, width=a hundred and twenty)
Tree.Column('#7', stretch=NO, minwidth=zero, width=120)
Tree.Percent()
Tree.Bind('<Double-Button-1>', OnSelected)

If __name__ == '__main__':
    Database()
    root.Mainloop()
