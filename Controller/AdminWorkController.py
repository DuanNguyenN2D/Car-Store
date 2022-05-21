from tkinter import *
from tkinter import messagebox
from Controller.InventoryManagementController import *
from Controller.EmployeesManagementController import *
from View.AdminWorkView import *
from Model.AdminWorkModel import *

class AdminWorkController():
    def __init__(self, root):
        self.root = root
        self.window = Tk()
        self.model = AdminWorkModel()
        self.view = AdminWorkView(self.window)
        self.view.button_inventory.configure(command=self.inventory)
        self.view.button_quit.configure(command=self.logout)
        self.view.button_employee.configure(command=self.employee)
        self.window.mainloop()

    def inventory(self):
        self.wd=InventoryManagementController(self.window)

    def invoice(self):
        pass

    def employee(self):
        self.wd=EmployeesManagementController(self.window)
    
    def logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.window.destroy()
            self.root.deiconify()