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


    def createDB(entryNum,listOfHeaders):
        datEntry = []
        with open('GeneratedDataset.csv',"w",newline='') as csvfile:
            if "Name (Fixed)" in listOfHeaders:
                print("Here")
            
            
        
        print("Done!")