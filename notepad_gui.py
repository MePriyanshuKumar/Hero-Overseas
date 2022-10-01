#starting complete notepad GUI for Hero Overseas

from copy import copy
from tkinter import *

from click import command
class notepad:
    

    # Function declaration
    def newFile():
        pass

    def openFile():
        pass

    def saveFile():
        pass

    def quitApp():
        pass

    def cut():
        pass

    def copy():
        pass

    def paste():
        pass

    def about():
        pass

    if __name__ == '__main__':
          #Basic setup
        root = Tk()
        root.title("Untitled - Notepad")

        root.wm_iconbitmap("icons8-notepad.ico")

        root.geometry("640x788")
        # add textarea
        TextArea = Text(root, font="lucida 13")
        file = None
        TextArea.pack(fill = BOTH)
        
        #Menubar option
        MenuBar = Menu(root)
        #Filemenu starts
        FileMenu = Menu(MenuBar, tearoff=0)


    #To open a new file
        FileMenu.add_command(label="New", command=newFile)

        #To open already existing file
        FileMenu.add_command(label="Open", command=openFile)
        
        #To save current file
        FileMenu.add_command(label="Save", command=saveFile)

        FileMenu.add_separator()
        FileMenu.add_command(label= "Exit", command = quitApp)
        MenuBar.add_cascade(label = "File", menu=FileMenu)
        #Filemenu ends

        #Edit menu starts
        EditMenu = Menu(MenuBar,tearoff=0)
        # To give feature of cut, copy and paste
        EditMenu.add_command(label = "Cut", command=cut)
        EditMenu.add_command(label = "Copy", command=copy)
        EditMenu.add_command(label = "Paste", command=paste)

        MenuBar.add_cascade(label = "Edit", menu = EditMenu)
        # Edit menu ends

        # Help menu starts
        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label = "About Notepad", command = about)
        MenuBar.add_cascade(label="Help", menu= HelpMenu)
        # Help menu ends


        root.config(menu=MenuBar)


        root.mainloop()
