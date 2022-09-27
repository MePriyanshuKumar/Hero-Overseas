from ast import main
from  tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk #pip install pillow

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()




class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title ("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"D:\Projects\Hero Overseas\test.jpg")
        lbl_bg  = Label(self.root,image= self.bg)
        lbl_bg.place(x =0, y=0, relwidth=1, relheight=1)

    
    
        # frame
        frame = Frame(self.root, bg="black")
        frame.place(x = 500, y = 150, width= 340, height= 450)

        img1 = Image.open(r"D:\Projects\Hero Overseas\circle-logo.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS) # ANTIALIAS Convert high level image into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        #put image into label
        lblimg1 = Label(image = self.photoimage1, bg="black", borderwidth = 0)
        lblimg1.place(x=610, y=150, width=100, height=100)

        #after logo
        get_str = Label(frame, text ="Get Started", font=("Anton", 20, "bold"), fg="white", bg= "black")
        get_str.place(x=95, y=100)

        # labels for username
        username = lbl = Label(frame, text ="Username", font=("Anton", 15, "bold"), fg="white", bg= "black")
        username.place(x= 70, y= 150)
        #entry
        self.txtuser = ttk.Entry(frame, font=("Anton", 15, "bold"))
        self.txtuser.place(x=40, y= 180, width=270)

        #labels for password
        password = lbl = Label(frame, text ="Password", font=("Anton", 15, "bold"), fg="white", bg= "black")
        password.place(x= 70, y= 225)

        #entry
        self.txtpass = ttk.Entry(frame, font=("Anton", 15, "bold"))
        self.txtpass.place(x=40, y= 250, width=270)

        #----Icon Images--
        #for username
        img2 = Image.open(r"D:\Projects\Hero Overseas\uicon.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS) 
        self.photoimage2 = ImageTk.PhotoImage(img2)

        #put image into label
        lblimg1 = Label(image = self.photoimage2, bg="black", borderwidth = 0)
        lblimg1.place(x=540, y=300, width=25, height=25)
        #for password
        img3 = Image.open(r"D:\Projects\Hero Overseas\pass.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS) 
        self.photoimage3 = ImageTk.PhotoImage(img3)
        #put image into label
        lblimg1 = Label(image = self.photoimage3, bg="black", borderwidth = 0)
        lblimg1.place(x=540, y=375, width=25, height=25)

        #login button
        loginbtn = Button(frame,command = self.login, text="Login", font=("Anton", 15, "bold"),bd=3, relief=RIDGE, fg="white", bg="darkorange",activeforeground="white",activebackground="darkorange" )
        loginbtn.place(x=110, y=300,width=120, height=35)

        #register buttons
        registerbtn = Button(frame, text="New User Register", command=self.register_window,font=("Anton", 10, "bold"),borderwidth=0, relief=RIDGE, fg="white", bg="black",activeforeground="white",activebackground="black" )
        registerbtn.place(x=13, y=350,width=160)
        #forgot password
        forgetbtn = Button(frame, text="Forgot Password ?",command=self.forgot_password_window, font=("Anton", 10, "bold"),borderwidth=0, relief=RIDGE, fg="white", bg="black",activeforeground="white",activebackground="black" )
        forgetbtn.place(x=10, y=370,width=160)




    #register window opening after selcting register btn
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app =Register(self.new_window)

    #logic of login
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error: Login failed", "All field requiered!")
        elif self.txtuser.get() =="herooverseas@gmail.com" and self.txtpass.get()=="priyanshu@overseas":
            messagebox.showinfo("Success!" ,"Welcome to herooverseas!")
        else:
            #connecting mysql database in login page so that we can fetch the email and password from register user db
            conn = mysql.connector.connect(host = "localhost", user = "root",password ="root@123",database = "herooverseas")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register where email = %s and password = %s",(self.txtuser.get(),self.txtpass.get()))

            row  = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","Invalid Username and password")
            else:
                open_main = messagebox.askyesno("YesNo","Access only admin")                
                if open_main > 0 :
                    self.new_window  = Toplevel(self.root)
                    self.app = listening(self.new_window) #must be change after
                else:
                    if not open_main :
                        return
            conn.commit()
            conn.close()                


   #========================Reset Password =============================
    def reset_pass(self):
        if self.txt_contact.get() =="" and self.txt_new_password.get() =="":
            messagebox.showerror("Error","Select the Phone number and new password to reset your password")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root",password ="root@123",database = "herooverseas")
            my_cursor = conn.cursor()
            qury=("SELECT * FROM register WHERE email=%s and contact=%s")
            vlue = (self.txtuser.get(), self.txt_contact.get())
            my_cursor.execute(qury,vlue)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct Phone number")
            else:
                query = ("UPDATE register SET password=%s WHERE email=%s")
                value = (self.new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with new password!")








   # =======================ForgotPasswordWindow================================================================
                
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error","Please enter the email address to reset the password")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root",password ="root@123",database = "herooverseas")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email = %s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2 = Toplevel()    
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text = "Forgot Password",font=("Anton", 20, "bold"), fg="red",bg="white")
                l.place(x = 0, y = 0, relwidth=1)
                #inside frame for resetting the password

                contact = Label(self.root2, text="Mobile No", font=( "Anton", 15, "bold"), bg="white", fg="black")
                contact.place(x=50, y=80)

                self.txt_contact = ttk.Entry(self.root2, font=("Anton", 15))
                self.txt_contact.place(x=50, y=110, width=250)

                #new password 
                new_password = Label(self.root2,text="New Password", font=("Anton", 15,"bold"),bg ="white",fg="black")
                new_password.place(x=50, y=170)

                self.new_password = ttk.Entry(self.root2,font=("Anton", 15))
                self.new_password.place(x=50, y=200, width=250)
                
                btn = Button(self.root2,text = "Reset",command = self.reset_pass,font=("Anton", 15,"bold"),fg="white", bg= "green")
                btn.place(x=50, y=280)



                        


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
            "Anton", 20, "bold"), fg="orange", bg="white")
        register_lbl.place(x=20, y=20)

        # ====row 1
        # labels and entry fields
        fname = Label(frame, text="First Name", font=("Anton", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname ,font=("Anton", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=(
            "Anton", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("Anton", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # == row 2
        # contact us
        contact = Label(frame, text="Mobile No", font=(
            "Anton", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("Anton", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        # email address
        email = Label(frame, text="Email", font=(
            "Anton", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("Anton", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # row 3
        pswd = Label(frame, text="Password", font=(
            "Anton", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=240)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("Anton", 15))
        self.txt_pswd.place(x=50, y=270, width=250)

        confirm_pswd = Label(frame, text=" Confirm Password", font=(
            "Anton", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=240)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("Anton", 15))
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
            "Anton", 15, "bold"), bg="white", fg="black")
        b1.place(x=10, y=380, width=200)

        # login btn
        img1 = Image.open(r"D:\Projects\Hero Overseas\login-now-btn.jpg")
        img1 = img1.resize((150, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=(
            "Anton", 15, "bold"), bg="white", fg="black")
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
    main()

    