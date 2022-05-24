from tkinter import *

class UpdateEmployeeView:
    def __init__(self, root,controller):
        root.geometry('1366x768')
        root.resizable(False, False)
        root.title('Update Employee')

        self.label = Label(root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master=root,file="./images/UpdateEmployee.png")
        self.label.configure(image=self.img)

        self.entry_name = Entry(root)
        self.entry_name.place(x=320, y=350, width=280, height=32)
        self.entry_name.configure(font="Itim 14")
        self.entry_name.configure(relief="flat")
        self.entry_name.configure(bg="#EECCEE")

        self.entry_age = Entry(root)
        self.entry_age.place(x=320, y=420, width=280, height=32)
        self.entry_age.configure(font="Itim 14")
        self.entry_age.configure(relief="flat")
        self.entry_age.configure(bg="#EECCEE")

        self.entry_phone_sub = Entry(root)
        self.entry_phone_sub.place(x=320, y=492, width=280, height=32)
        self.entry_phone_sub.configure(font="Itim 14")
        self.entry_phone_sub.configure(relief="flat")
        self.entry_phone_sub.configure(bg="#EECCEE")

        self.entry_wage = Entry(root)
        self.entry_wage.place(x=840, y=350, width=250, height=32)
        self.entry_wage.configure(font="Itim 14")
        self.entry_wage.configure(relief="flat")
        self.entry_wage.configure(bg="#EECCEE")

        self.entry_phone = Entry(root)
        self.entry_phone.place(x=840, y=420, width=280, height=32)
        self.entry_phone.configure(font="Itim 14")
        self.entry_phone.configure(relief="flat")
        self.entry_phone.configure(bg="#EECCEE")

        self.entry_role = Entry(root)
        self.entry_role.place(x=840, y=492, width=280, height=32)
        self.entry_role.configure(font="Itim 14")
        self.entry_role.configure(relief="flat")
        self.entry_role.configure(bg="#EECCEE")

        self.entry_username = Entry(root)
        self.entry_username.place(x=320, y=563, width=280, height=32)
        self.entry_username.configure(
            font="Itim 14",
            relief="flat",
            bg="#EECCEE")

        self.entry_password = Entry(root)
        self.entry_password.place(x=840,y=563, width=280, height=32)
        self.entry_password.configure(
            font="Itim 14",
            relief="flat",
            bg="#EECCEE")

        # Add
        self.button_update = Button(root)
        self.button_update.place(x=455, y=630)
        self.button_update.configure(borderwidth="0")
        self.button_update.configure(background="#E7E7E7")
        self.button_update.configure(activebackground="#E7E7E7")
        self.img_update = PhotoImage(master=root,file="./images/Button_Update.png")
        self.button_update.configure(image=self.img_update)

        # Clear
        self.button_clear = Button(root)
        self.button_clear.place(x=633, y=630)
        self.button_clear.configure(borderwidth="0")
        self.button_clear.configure(background="#E7E7E7")
        self.button_clear.configure(activebackground="#E7E7E7")
        self.img_clear = PhotoImage(master=root,file="./images/Button_Clear.png")
        self.button_clear.configure(image=self.img_clear)

        # Exit
        self.button_exit = Button(root)
        self.button_exit.place(x=805, y=630)
        self.button_exit.configure(borderwidth="0")
        self.button_exit.configure(background="#E7E7E7")
        self.button_exit.configure(activebackground="#E7E7E7")
        self.img_exit = PhotoImage(master=root,file="./images/Button_Exit.png")
        self.button_exit.configure(image=self.img_exit)

        # Log out
        self.button_logout = Button(root)
        self.button_logout.place(x=1263, y=12)
        self.button_logout.configure(borderwidth="0")
        self.button_logout.configure(background="white")
        self.button_logout.configure(activebackground="white")
        self.img_logout = PhotoImage(master=root,file="./images/Button_Logout.png")
        self.button_logout.configure(image=self.img_logout)

        self.entry_name.insert(0,controller.val[1])
        self.entry_role.insert(0,controller.val[2])
        self.entry_role["state"]=DISABLED
        self.entry_phone.insert(0,controller.val[3])
        self.entry_phone_sub.insert(0,controller.val[4])
        self.entry_age.insert(0,controller.val[5])
        self.entry_wage.insert(0,controller.val[6])
        self.entry_username.insert(0,controller.val[7])
        self.entry_username["state"]=DISABLED
        self.entry_password.insert(0,controller.pw)
