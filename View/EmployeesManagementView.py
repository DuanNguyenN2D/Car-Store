from tkinter import *
from tkinter.ttk import Treeview

class EmployeesManagementView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768")
        self.root.resizable(0, 0)
        self.root.title("Employees Management")

        self.label = Label(self.root)
        self.label.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(master = self.root, file="./Images/EmployeeManagement.png")
        self.label.configure(image=self.img)

        self.columns = ("id", "name","role","phone","phone_sub", "age","wage", "username")
        self.tree = Treeview(root)
        self.tree.place(x=20, y=103, width=730, height=635)
        self.tree.configure(
            columns = self.columns,
            selectmode ="extended"
        )

        self.tree.heading("id", text="ID", anchor=CENTER)
        self.tree.heading("name", text="Name", anchor=W)
        self.tree.heading("role", text="Role", anchor=W)
        self.tree.heading("phone", text="Phone", anchor=CENTER)
        self.tree.heading("phone_sub", text="Phone(Sub)", anchor=CENTER)
        self.tree.heading("age", text="Age", anchor=CENTER)
        self.tree.heading("wage", text="Wage", anchor=E)
        self.tree.heading("username", text="Username", anchor=W)
        
        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=CENTER)
        self.tree.column("#2", stretch=NO, minwidth=0, width=180)
        self.tree.column("#3", stretch=NO, minwidth=0, width=90)
        self.tree.column("#4", stretch=NO, minwidth=0, width=90, anchor=CENTER)
        self.tree.column("#5", stretch=NO, minwidth=0, width=90, anchor=CENTER)
        self.tree.column("#6", stretch=NO, minwidth=0, width=50, anchor=CENTER)
        self.tree.column("#7", stretch=NO, minwidth=0, width=90, anchor=E)
        self.tree.column("#8", stretch=NO, minwidth=0, width=90)

        self.contacts = []

        self.entry_id = Entry(self.root)
        self.entry_id.place(relx=0.6578, rely=0.547, width=365, height=30)
        self.entry_id.configure(background = "#fcdefc")
        self.entry_id.configure(font="Itim 18")
        self.entry_id.configure(relief="flat")

        self.button_search = Button(self.root)
        self.button_search.place(relx=0.6164, rely=0.5486,height=25, width=50)
        self.button_search.configure(relief="flat")
        self.button_search.configure(overrelief="flat")
        self.button_search.configure(activebackground="#fcdefc")
        self.button_search.configure(foreground="#fcdefc")
        self.button_search.configure(background="#fcdefc")
        self.button_search.configure(borderwidth="0")
        self.img_search = PhotoImage(master=self.root, file="./images/button_search.png")
        self.button_search.configure(image=self.img_search)

        self.button_add_employee = Button(self.root)
        self.button_add_employee.place(relx=0.6625, rely=0.638)
        self.button_add_employee.configure(relief="flat")
        self.button_add_employee.configure(overrelief="flat")
        self.button_add_employee.configure(activebackground="#ffffff")
        self.button_add_employee.configure(foreground="#ffffff")
        self.button_add_employee.configure(background="#ffffff")
        self.button_add_employee.configure(borderwidth="0")
        self.img_add = PhotoImage(master = self.root, file="./Images/Button_AddEmployee.png")
        self.button_add_employee.configure(image=self.img_add)

        self.button_update_employee = Button(self.root)
        self.button_update_employee.place(relx=0.6625, rely=0.7161)
        self.button_update_employee.configure(relief="flat")
        self.button_update_employee.configure(overrelief="flat")
        self.button_update_employee.configure(activebackground="#ffffff")
        self.button_update_employee.configure(foreground="#ffffff")
        self.button_update_employee.configure(background="#ffffff")
        self.button_update_employee.configure(borderwidth="0")
        self.img_update = PhotoImage(master = self.root,file="./images/Button_UpdateEmployee.png")
        self.button_update_employee.configure(image=self.img_update)

        self.button_del_employee = Button(self.root)
        self.button_del_employee.place(relx=0.6625, rely=0.7968)
        self.button_del_employee.configure(relief="flat")
        self.button_del_employee.configure(overrelief="flat")
        self.button_del_employee.configure(activebackground="#ffffff")
        self.button_del_employee.configure(foreground="#ffffff")
        self.button_del_employee.configure(background="#ffffff")
        self.button_del_employee.configure(borderwidth="0")
        self.img_del = PhotoImage(master = self.root,file="./images/Button_DeleteEmployee.png")
        self.button_del_employee.configure(image=self.img_del)

        self.button_exit = Button(self.root)
        self.button_exit.place(relx=0.718, rely=0.8763)
        self.button_exit.configure(relief="flat")
        self.button_exit.configure(overrelief="flat")
        self.button_exit.configure(activebackground="#ffffff")
        self.button_exit.configure(foreground="#ffffff")
        self.button_exit.configure(background="#ffffff")
        self.button_exit.configure(borderwidth="0")
        self.img_exit = PhotoImage(master=self.root,file="./Images/Button_Exit.png")
        self.button_exit.configure(image=self.img_exit)

        self.button_logout = Button(self.root)
        self.button_logout.place(relx=0.9277, rely=0.0156)
        self.button_logout.configure(relief="flat")
        self.button_logout.configure(overrelief="flat")
        self.button_logout.configure(activebackground="#ffffff")
        self.button_logout.configure(foreground="#ffffff")
        self.button_logout.configure(background="#ffffff")
        self.button_logout.configure(borderwidth="0")
        self.img_logout = PhotoImage(master = self.root, file="./images/Button_Logout.png")
        self.button_logout.configure(image=self.img_logout)