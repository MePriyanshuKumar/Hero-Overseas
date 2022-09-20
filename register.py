from atexit import register
from tkinter import *
# from ast import main
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # == =text variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
     

        # ====bg image====
        self.bg = ImageTk.PhotoImage(
            file=r"D:\Projects\Hero Overseas\bg-reg.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        # ====left image====
        self.bg1 = ImageTk.PhotoImage(
            file=r"D:\Projects\Hero Overseas\login.png")
        bg_lbl = Label(self.root, image=self.bg1)
        bg_lbl.place(x=50, y=100, width=470, height=550)

        #  main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=700, height=550)

        # register label
        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="orange", bg="white")
        register_lbl.place(x=20, y=20)

        # ====row 1
        # labels and entry fields
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname ,font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # == row 2
        # contact us
        contact = Label(frame, text="Mobile No", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        # email address
        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # row 3
        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=240)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=270, width=250)

        confirm_pswd = Label(frame, text=" Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=240)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=270, width=250)

        # checkbox=====
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check, text="I Agree the Terms & Conditions", font=(
            "italic", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=330)

        # button register now
        img = Image.open(r"D:\Projects\Hero Overseas\register-now-btn.jpeg")
        img = img.resize((150, 100), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage,command = self.register_data, borderwidth=0, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=10, y=380, width=200)

        # login btn
        img1 = Image.open(r"D:\Projects\Hero Overseas\login-now-btn.jpg")
        img1 = img1.resize((150, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        b1.place(x=330, y=380, width=200)

        # ===== Function declarations =====

    def register_data(self):
        if self.var_fname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" :
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root", password = "root@123", database = "herooverseas")
            # add
            my_cursor = conn.cursor()
            # validation
            query = ("SELECT * FROM register WHERE email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            #fetch data from database
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist , please try signing in")
            else:
                #data enter
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_pass.get()))    
                conn.commit()
                conn.close()
                messagebox.showinfo("Success!", "Register successfully")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
