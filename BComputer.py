import GUI as BG
import Records as BR
import Dialogue as BD


#BG.BatGUI.LaunchGUI()

BD.Dialogue.MainUserSelection()
User_Selection = int(input())




if(User_Selection == 1):

    Name = str(input("Name: "))
    MultiVerse = str(input("Multi-Verse: "))
    Bio = str(input("Bio: "))
    ImageLocation = str(input("ImageLocation: " ))

    BR.Records(Name, MultiVerse, Bio, ImageLocation)

elif(User_Selection == 2):
    RecordToSearch = str(input("Who are you looking for? \n"))
    BR.Records.LookForARecord(RecordToSearch)  
    



