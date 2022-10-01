#Import the required Libraries
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
import os # for linking the file
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("400x200")
win.configure(bg='#A52A2A') 
win.title("Hero Overseas")
def open_popup():
    # filename= 'login.py'
    # os.system(filename) #Open file [same as Right Click open]
    # os.system('tkinter'+ filename)
    
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("Child Window")
   Label(top, text= "Welcome to Hero Overseas!", font=('Mistral 18 bold')).place(x=150,y=80)

Label(win, bg="#A52A2A",text=" Please login to take the test!", font=('Anton')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Login now", command= open_popup).pack()
win.mainloop()