import json as j


class Records(object):
    CurrentRecords = {}

    #==============================================================
    # Load or create a JSON file that will store record information
    # 
    # Notes: Need to work in logic for when there is no file existing
    #==============================================================
    def LoadJSON():
        try:
            with open('Records.json','r+') as file:
                print("Accessing data now... \n")
                Records.CurrentRecords = j.load(file)
                 
           
        except Exception as e:
            print("There appears to be an error accessing the data. Let me pull up the error now: \n" + str(e))
    

    #==========================================================
    # Create a record object to house new character information
    # then serilize the object to store in JSON
    #==========================================================
    def CreateJSONRecord(self):

        #LoadJSON records
        Records.LoadJSON()

        #Construction
        print(Records.CurrentRecords)

        #Create a dictonary of persons data  
        Records.CurrentRecords[self.name] = {
                 "Name" : str(self.name)
                ,"Multi-verse" : str(self.multiverse)
                ,"Bio" :  str(self.bio)
                ,"ImageLocation" : str(self.imageLocation)
                }
        
        #SerializeJSON
        Records.SerializeJSON()


    #==========================================================
    # Serialize acquired data into JSON format
    #==========================================================
    def SerializeJSON():
        # Serializing JSON  
        JSON_Object = j.dumps(Records.CurrentRecords, indent = 4) 
  
       #Write to file
        with open("Records.json", "w") as outfile: 
            outfile.write(JSON_Object)

    #==========================================================
    # Constructor for the Record class
    #==========================================================
    def __init__(self, Name, Multiverse, Bio, ImageLocation):
        self.name = Name
        self.multiverse = Multiverse
        self.bio = Bio
        self.imageLocation = ImageLocation

        #Create JSON entry for future look ups
        Records.CreateJSONRecord(self)
    
    #==========================================================
    # Search for a specific record
    #==========================================================
    def LookForARecord(Character):
        Records.LoadJSON()
        print("Name: " + Records.CurrentRecords[Character]["Name"] + "\n")
        print("Bio: " + Records.CurrentRecords[Character]["Bio"]+ "\n")
        print("Multi-Verse: " + Records.CurrentRecords[Character]["Multi-verse"] + "\n")
                    
      
       
        
    


