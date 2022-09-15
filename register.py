from atexit import register
from tkinter import*
# from ast import main
from tkinter import ttk
from tkinter import messagebox


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+1+0")



if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
