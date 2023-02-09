from tkinter import *
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import filedialog
import tkinter.messagebox
from tkinter import messagebox
import os
from psutil import net_io_counters
import mysql.connector as mysql
from mysql.connector import Error


class Window:
    def __init__(self, master):

        global window

        window = tk.Tk()
        self.mainFrame = Frame(master)
        self.mainFrame.pack(side=TOP,padx=100,  pady=100)
        

        btn_login = Button(self.mainFrame, text="Begin",command = self.begin, font=('arial', 18), width=35 )
        btn_login.grid(row=4, columnspan=2, pady=20)


    def begin(self):
        self.mainFrame.destroy()
        openwindow = Main()


class Main:     
    def __init__(self):
        #self.frame = Frame(master)
        #self.frame.pack(padx=10, pady=10)
        Top = Toplevel()

        #self.frame = Frame(Top)
        #self.frame.pack(padx=10, pady=10)
        self.LoginFrame = Frame(Top)
        self.LoginFrame.pack(side=TOP,padx=100,  pady=100)
        
        lbl_username = Label(self.LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        
        lbl_password = Label(self.LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        
        self.lbl_result1 = Label(self.LoginFrame, text="", font=('arial', 18))
        self.lbl_result1.grid(row=3, columnspan=2)
        
        self.username = Entry(self.LoginFrame, font=('arial', 20), width=15)
        self.username.grid(row=1, column=1)
        
        self.password = Entry(self.LoginFrame, font=('arial', 20), width=15, show="*")
        self.password.grid(row=2, column=1)
        
        btn_login = Button(self.LoginFrame, text="Login",command = self.Login, font=('arial', 18), width=35 )
        btn_login.grid(row=4, columnspan=2, pady=20)
       
        lbl_register = Label(self.LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', self.ToggleToRegister)
    
   
    def ToggleToRegister(self, event=None):
        self.LoginFrame.destroy()
        openwindow = Register()

        
    def Login(self):
        Database()
        try:
            conn = mysql.connect(host="localhost", user="root", password="", database="db_member")
            if conn.is_connected():
                cursor = conn.cursor()

        except Error as e:
            messagebox.showinfo("Host  not found")

        
        if self.username.get() == "" and self.password.get() == "":
            lbl_result1.config(text="Please complete the required field!", fg="orange")
            
        else:
            username = self.username.get()
            password = self.password.get()
            
            cursor.execute(f"SELECT username, password FROM member WHERE username = '{username}' AND password = '{password}'")
            result = cursor.fetchone()
                    
            if result is None:

                messagebox.showinfo("Invalid {username} or {password}")
                print("invalid")

            else:
                self.lbl_result1.config(text="You are successfully Logged Ind", fg="red")
                self.LoginFrame.destroy()
                openwindow = Netrecon()

   
class Register:
    def __init__(self):
        top = Toplevel()
    
        self.RegisterFrame = Frame(top)
        self.RegisterFrame.pack(side=TOP, padx=100 ,pady=100)
        
        lbl_username = Label(self.RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl_username.grid(row=1)

        lbl_password = Label(self.RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=2)
        
        lbl_firstname = Label(self.RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
        lbl_firstname.grid(row=3)
        
        lbl_lastname = Label(self.RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
        lbl_lastname.grid(row=4)
        
        self.lbl_result2 = Label(self.RegisterFrame, text="", font=('arial', 18))
        self.lbl_result2.grid(row=5, columnspan=2) 
        
        self.username = Entry(self.RegisterFrame, font=('arial', 20), width=15)
        self.username.grid(row=1, column=1)
        
        self.password = Entry(self.RegisterFrame, font=('arial', 20),  width=15, show="*")
        self.password.grid(row=2, column=1)
        
        self.firstname = Entry(self.RegisterFrame, font=('arial', 20), width=15)#textvariable needed here 
        self.firstname.grid(row=3, column=1)
        
        self.lastname = Entry(self.RegisterFrame, font=('arial', 20),  width=15) #textvariable needed here 
        self.lastname.grid(row=4, column=1)
        
        btn_Register = Button(self.RegisterFrame, text="Register", font=('arial', 18), width=35, command=self.register)
        btn_Register.grid(row=6, columnspan=2, pady=20)
        
        lbl_login = Label(self.RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>',self.ToggleToLogin)

       
    def ToggleToLogin(self, event=None):
        self.RegisterFrame.destroy()
        Main()
       

    def Table(self):
        Connect_db()
       
        cursor.execute("DROP TABLE IF EXISTS member;")

        cursor.execute("CREATE TABLE member(username varchar(255),password varchar(255),firstname varchar(255),lastname varchar(255))")
        
        conn.commit()
        messagebox.showinfo("Table exists")

        self.Exit()

    def Exit(self):
        root.destroy()
        exit()
    
    def register(self):
        #Database()
        Connect_db()
        USERNAME = self.username.get()
        PASSWORD = self.password.get()
        FIRSTNAME = self.firstname.get()
        LASTNAME = self.lastname.get()
        print(self.username.get())
        conn = mysql.connect(host="localhost",user="root",password="",database="db_member")

        if conn.is_connected():

            cursor = conn.cursor()
            query = "INSERT INTO member(username, password, firstname, lastname) VALUES(%s, %s, %s, %s)"
            cursor.execute(query,(USERNAME, PASSWORD, FIRSTNAME, LASTNAME))

            conn.commit()
            messagebox.showinfo("Registration Succesfull")
            self.lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()
class Connect_db:
    def __init_(self):
        Database()
        try:
            conn = mysql.connect(host="localhost",user="root",password="",database="db_member")
            if conn.is_connected():
                cursor = conn.cursor()

                conn.close()

        except Error as e:
            
            root.destroy() 

class Database:
    def __init__(self):
        conn = mysql.connect(host="localhost",user="root",password="")
        if conn.is_connected():
            cursor =conn.cursor()
            try:
                cursor.execute(f"IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'db_member')")
                cursor.execute(f"CREATE DATABASE db_member")

                conn.commit()
                print("database created")
                cursor.close()
                conn.close()

            except Error as e:
                pass
                conn.close()  
           
                
class Netrecon:
    def __init__(self):
        top = Toplevel()
        
        top_frame = Frame(top)
        top_frame.pack(side="top", fill="x")

        bottom_frame = Frame(top)
        bottom_frame.pack(side="bottom", fill="x")

        main = Frame(top)
        main.pack(fill='both', expand=True)

        self.terminal = Text(main, wrap='word')
        self.terminal.pack(fill='both', expand=True)
        
        self.entry = Entry(top)
        self.entry.pack(side='top', fill='x')

        nmap_button = Button(top_frame, text="Network Scan",command=self.run_nmap)
        nmap_button.pack(side='left')

        searchsploit_button = Button(top_frame, text="Exploit_db",command=self.run_searchsploit)
        searchsploit_button.pack(side='left')

        dns_button = Button(top_frame, text="DNS",command=self.dnsrecon)
        dns_button.pack(side='left')

        open_file_button = Button(bottom_frame, text="Open File", command=self.open_file)
        open_file_button.pack(side='right')

        save_button = Button(bottom_frame, text="Save",command=self.save_output)
        save_button.pack(side='left')

        clear_button = ttk.Button(bottom_frame, text="Clear",command=self.clear_output)
        clear_button.pack(side='left')


    def run_nmap(self):
        target = self.entry.get()
        output = subprocess.run(["Nmap", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())

    def run_searchsploit(self):
        search_term = self.entry.get()
        output = subprocess.run(["Searchsploit", search_term], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())


    def save_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.terminal.get("1.0", "end"))
            tkinter.messagebox.showinfo("Info", "File saved successfully")
        else:
            tkinter.messagebox.showinfo("Error", "Failed to save file.")

    def dnsrecon(self):
        target = self.entry.get()
        output = subprocess.run(["dnsrecon","-d", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.terminal.insert('end', output.stdout.decode())

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"),
                                                          ("All Files", "*.*")])
        try:
            with open(file_path, "r") as file:
                contents = file.read()
                self.terminal.insert("end", contents)   
        except:
            messagebox.showerror("Error", "Could not open the file.")

    def clear_output(self):
        self.terminal.delete("1.0", "end")



root = Tk()
root.title("NetReconTool")
window = Window(root)
root.mainloop()
