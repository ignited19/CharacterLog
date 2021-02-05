#=============================================
# This class handles the GUI portion of the
# bat computer
#=============================================
from tkinter import *


class BatGUI():
    

    def LaunchGUI():
        
        User_Input = ""
        GUI = Tk()

        #Assign the dimensions of the GUI window
        GUI.minsize(width = "600", height = "600")
        GUI.maxsize(width = "600", height = "600")
        GUI.configure(background='black')

        
        #Add background image
        #Background_Image = PhotoImage("")
        #Background_Label = Label(GUI, image=Background_Image)
        #Background_Label.place(x=100, y=100, relwidth=1, relheight=1)


        #Entry
        CharacterEntry = Entry(GUI, textvariable = User_Input)
        CharacterEntry.pack(side = BOTTOM)
       
       
        #MainLoop
        GUI.mainloop()


