from ast import main
from  tkinter import*
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk #pip install pillow
class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title ("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"D:\Projects\Hero Overseas\bg.jpg")
        lbl_bg  = Label(self.root,image= self.bg)
        lbl_bg.place(x =0, y=0, relwidth=1, relheight=1)

    
    
        # frame
        frame = Frame(self.root, bg="black")
        frame.place(x = 610, y = 170, width= 340, height= 450)

        img1 = Image.open(r"D:\Projects\Hero Overseas\circle-logo.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS) # ANTIALIAS Convert high level image into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        #put image into label
        lblimg1 = Label(image = self.photoimage1, bg="black", borderwidth = 0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        #after logo
        get_str = Label(frame, text ="Get Started", font=("times new roman", 20, "bold"), fg="white", bg= "black")
        get_str.place(x=95, y=100)

        # labels for username
        username = lbl = Label(frame, text ="Username", font=("times new roman", 15, "bold"), fg="white", bg= "black")
        username.place(x= 70, y= 155)
        #entry
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y= 180, width=270)

        #labels for password
        password = lbl = Label(frame, text ="Password", font=("times new roman", 15, "bold"), fg="white", bg= "black")
        password.place(x= 70, y= 225)

        #entry
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y= 250, width=270)

        #----Icon Images--
        #for username
        img2 = Image.open(r"D:\Projects\Hero Overseas\uicon.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS) 
        self.photoimage2 = ImageTk.PhotoImage(img2)

        #put image into label
        lblimg1 = Label(image = self.photoimage2, bg="black", borderwidth = 0)
        lblimg1.place(x=650, y=323, width=25, height=25)
        #for password
        img3 = Image.open(r"D:\Projects\Hero Overseas\pass.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS) 
        self.photoimage3 = ImageTk.PhotoImage(img3)
        #put image into label
        lblimg1 = Label(image = self.photoimage3, bg="black", borderwidth = 0)
        lblimg1.place(x=650, y=395, width=25, height=25)

        #login button
        loginbtn = Button(frame,command = self.login, text="Login", font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, fg="white", bg="red",activeforeground="white",activebackground="red" )
        loginbtn.place(x=110, y=300,width=120, height=35)

        #register buttons
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"),borderwidth=0, relief=RIDGE, fg="white", bg="black",activeforeground="white",activebackground="black" )
        registerbtn.place(x=14, y=350,width=160)
        #forgot password
        forgetbtn = Button(frame, text="Forgot Password ?", font=("times new roman", 10, "bold"),borderwidth=0, relief=RIDGE, fg="white", bg="black",activeforeground="white",activebackground="black" )
        forgetbtn.place(x=10, y=370,width=160)

    #logic of login
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error: Login failed", "All field requiered!")
        elif self.txtuser.get() =="herooverseas@gmail.com" and self.txtpass.get()=="priyanshu@overseas":
            messagebox.showinfo("Success!" ,"Welcome to herooverseas!")
        else:
            messagebox.showerror("Invalid!", "Invalid username or password!!")


if __name__ == "__main__":
    root = Tk()
    app = Login_window(root)
    root.mainloop()