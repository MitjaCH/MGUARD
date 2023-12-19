import tkinter as tk
from tkinter import StringVar
from tkinter.font import Font
import db_conn

class Fonts:
    def __init__(self):
        self.titleFont = Font(family="Helvetica", size=36, weight="bold", slant="roman")
        self.textFont = Font(family="Helvetica", size=15, weight="bold", slant="roman")
        self.entryFont = Font(family="Helvetica", size=13, slant="roman")
        self.entryTitle = Font(family="Helvetica", size=10)
        self.errorFont = Font(family="Helvetica", size=7)

class Login:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.configure(bg="#383838")

        self.load_users()
        self.fonts = Fonts()

        self.username_var = StringVar()
        self.password_var = StringVar()

        self.canvas = tk.Canvas(self.window, bg="#383838", height=500, width=800, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0.0, 0.0, 800.0, 77.0, fill="#0075FF", outline="")

        self.userEntry = tk.Entry(textvariable=self.username_var, bd=0, bg="#0075FF", fg="#ffffff", highlightthickness=0, font=self.fonts.entryFont)
        self.userEntry.place(x=248.0, y=183.0, width=304.0, height=71.0)
        self.userLabel = tk.Label(text="Username", bd=0, bg="#0075FF", fg="#ffffff", highlightthickness=0, font=self.fonts.entryTitle)
        self.userLabel.place(x=248.0, y=183.0, width=70.0, height=25.0)

        self.passEntry = tk.Entry(bd=0, textvariable=self.password_var, bg="#0075FF", fg="#ffffff", highlightthickness=0, font=self.fonts.entryFont, relief=tk.FLAT, show='•')
        self.passEntry.place(x=248.0, y=276.0, width=304.0, height=75.0)
        self.passLabel = tk.Label(text="Password", bd=0, bg="#0075FF", fg="#ffffff", highlightthickness=0, font=self.fonts.entryTitle)
        self.passLabel.place(x=248.0, y=276.0, width=70.0, height=25.0)

        self.errorLabel = tk.Label(bg="#FF0004", fg="#FFFFFF", font=self.fonts.errorFont, borderwidth=0, highlightthickness=0)
        self.errorLabel.place(x=248.0, y=95.0, width=304.0, height=71.0)
        self.errorLabel.place_forget()

        self.loginBTN = tk.Button(text="Login", font=self.fonts.textFont, borderwidth=0, highlightthickness=0, command=self.login, relief=tk.FLAT, bg="#00ff8c", fg="#ffffff")
        self.loginBTN.place(x=197.0, y=369.0, width=197.0, height=46.0)

        self.canvas.create_text(331.0, 16.0, anchor="nw", text="LOGIN", fill="#FFFFFF", font=self.fonts.titleFont)

        self.registerBTN = tk.Button(text="Registrieren", font=self.fonts.textFont, borderwidth=0, highlightthickness=0, command=self.open_register, relief=tk.FLAT, bg="#00ff8c", fg="#ffffff")
        self.registerBTN.place(x=407.0, y=369.0, width=197.0, height=46.0)

        self.window.resizable(False, False)
        self.window.mainloop()

    def load_users(self):
        print("Loaded Users")

    def login(self):
        print("Login!")

    def open_register(self):
        print("Opened Register")

    def open_manager(self):
        print("Opened Manager")


class Register:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x500")
        self.window.configure(bg="#383838")

        self.key = self.load_key()
        self.fonts = Fonts()
        
        self.username_var = StringVar()
        self.password_var = StringVar()
        self.email_var = StringVar()
        
        self.canvas = tk.Canvas(self.frame, bg="#383838", height=500, width=800, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(0.0, 0.0, 800.0, 77.0, fill="#FF4B4B", outline="")
        self.canvas.create_text(260.0, 16.0, anchor="nw", text="Registrierung", fill="#FFFFFF", font=self.titleFont)
        
        self.email_entry = tk.Entry(bd=0, bg="#FF4B4B", fg="#ffffff", highlightthickness=0, textvariable=self.email_var)
        self.email_entry.place(x=248.0, y=118.0, width=304.0, height=75.0)

        self.email_label = tk.Label(text="E-Mail", bd=0,bg="#FF4B4B", fg="#ffffff", highlightthickness=0, font=self.entryTitle)
        self.email_label.place(x=248.0, y=118.0, width=50.0, height=25.0)

        self.username_entry = tk.Entry(bd=0, bg="#FF4B4B", fg="#ffffff", highlightthickness=0, textvariable=self.username_var)
        self.username_entry.place(x=248.0, y=218.0, width=304.0, height=75.0)

        self.username_label = tk.Label(text="Username", bd=0,bg="#FF4B4B", fg="#ffffff", highlightthickness=0, font=self.entryTitle)
        self.username_label.place(x=248.0, y=218.0, width=70.0, height=25.0)
        
        self.password_entry = tk.Entry(bd=0, bg="#FF4B4B", fg="#ffffff", highlightthickness=0, textvariable=self.password_var)
        self.password_entry.place(x=248.0, y=318.0, width=304.0, height=75.0)

        self.password_label = tk.Label(text="Password", bd=0,bg="#FF4B4B", fg="#ffffff", highlightthickness=0, font=self.entryTitle)
        self.password_label.place(x=248.0, y=318.0, width=70.0, height=25.0)
        
        self.error_Label = tk.Label(text="", fg="red", font=("Arial", 12), bg="#FF4B4B")
        self.error_Label.place(x=248.0, y=80.0, width=304.0, height=25.0)
        
        self.registerBTN = tk.Button(borderwidth=0, highlightthickness=0, fg="#ffffff", bg="#FF4B4B", text="Registrieren", command=self.register, relief="flat")
        self.registerBTN.place(x=310.0, y=404.0, width=179.0, height=49.0)
        
        self.login = tk.Button(text="Zurück zur Anmeldung", fg="#ffffff", bg="#FF4B4B", borderwidth=0, highlightthickness=0, command=self.open_login)
        self.login.place(x=663.0, y=453.0, width=137.0, height=47.0)
        
        self.window.resizable(False, False)
        self.window.mainloop()


    def load_key(self):
        print("Loaded Key")

    def register(self):
        print("Registered.")



    def open_login(self):
        print("Opened Login")


if __name__ == "__main__":
    Login()
