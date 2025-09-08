import json
import random
import csv
from data.dataCollection import db_col

with open('data/firstNamesSP.json', 'r') as f:
    dataJson  = json.load(f)
    


class dbmodules:
    def checkdupes(list):
        dupes = {}
        placer = []
        for count in range(len(list)):
            if list[count]["name"] not in placer:
                placer.append(list[count]["name"])
            else:
                if list[count]["name"] in dupes:
                    dupes.update({list[count]["name"]:  dupes[list[count]["name"]]+1})
                else:
                    dupes[list[count]["name"]] = 1
        return dupes
    
    def onlyUnique(list):
        uniqueVals = []
        for count in range(len(list)):
            if list[count]["name"] not in uniqueVals:
                uniqueVals.append(list[count]["name"])

        return uniqueVals
    @classmethod
    def genNames(cls,ver):
        if ver == 1:
            return dataJson["Firstname"][random.randrange(0,len(dataJson["Firstname"])-1)]
        else:
            return db_col.firstname[random.randrange(0,len(db_col.firstname)-1)] + " " +db_col.lastname[random.randrange(0,len(db_col.lastname)-1)]
    @classmethod
    def genHeaders(cls,hlist):
        placer = []
        for name in hlist:
            if name == "Names (Fixed)" or name == "Names":
                placer.append("Name of Person")
            elif name == "Gender":
                placer.append("Gender")
            elif name == "Country":
                placer.append("Country")
        
        return placer

    
    def addToBeGenerated(name,setOfNames):
        if name in setOfNames:
            return "Its already chosen"
        else:
            setOfNames.append(name)
            return setOfNames
    
    def removeToBeGenerated(name,setOfNames):
        if name in setOfNames:
            setOfNames.remove(name)
            return setOfNames
        else:
            return "It has not been chosen yet"
        
    @classmethod
    def createDB(cls,entryNum,listOfHeaders):
        datEntry = []
        print(cls.genHeaders(listOfHeaders))
        print(entryNum)
        print(cls.genNames(0))

        # with open('GeneratedDataset.csv',"w",newline='') as csvfile:
        #     print("Hi")