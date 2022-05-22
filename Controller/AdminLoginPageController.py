from tkinter import *
from tkinter import messagebox
from View.AdminLoginPageView import *
from Model.LoginPageModel import *
from Controller.AdminWorkController import *

class AdminLoginPageController():
    def __init__(self, root):
        self.root = root
        self.toplv = Toplevel(root)
        self.model = AdminLoginPageModel()
        self.view = AdminLoginPageView(self.toplv)
        self.view.entry_username.configure(textvariable=self.model.username)
        self.view.entry_password.configure(textvariable=self.model.password)
        self.view.button_login.configure(command=self.login)
        self.toplv.mainloop()

    def login(self):
        if self.model.check_account():
            self.model.username.set("")
            self.model.password.set("")
            self.view.entry_username.config(textvariable =self.model.username)
            self.view.entry_password.config(textvariable =self.model.password)
            self.toplv.withdraw()
            self.new_root = AdminWorkController(self.root)

        else:
            messagebox.showerror("Error","Username or password incorrect")
            self.model.username.set("")
            self.model.password.set("")
            self.view.entry_username.config(textvariable =self.model.username)
            self.view.entry_password.config(textvariable =self.model.password)
