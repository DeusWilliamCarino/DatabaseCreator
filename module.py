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
            jsondata = dataJson["Firstname"][random.randrange(0,len(dataJson["Firstname"])-1)]
            jsondata["lastname"] = db_col.lastname[random.randrange(0,len(db_col.lastname)-1)]
            return jsondata
        else:
            return db_col.firstname[random.randrange(0,len(db_col.firstname)-1)] + " " +db_col.lastname[random.randrange(0,len(db_col.lastname)-1)]
        
    @classmethod
    def genHeaders(cls,hlist):
        placer = []
        for name in hlist:
            if name == "Names (Fixed)" or name == "Names":
                placer.append("Fullname")
            elif name == "Gender":
                placer.append("Gender")
            elif name == "Country":
                placer.append("Country")       
        return placer
    
    @classmethod
    def genData(cls,hlist):
        placer = {}
        for name in hlist:
            if name == "Names (Fixed)":
                jsondata = dataJson["Firstname"][random.randrange(0,len(dataJson["Firstname"])-1)]
                jsondata["lastname"] = db_col.lastname[random.randrange(0,len(db_col.lastname)-1)]
                jsondata["fullname"] = jsondata["name"] + " "+ jsondata["lastname"]
                return jsondata
            else:
                if name =="Names":
                   placer["Firstname"] = db_col.firstname[random.randrange(0,len(db_col.firstname)-1)] 
                   placer["lastname"] = db_col.lastname[random.randrange(0,len(db_col.lastname)-1)]
                   placer["fullname"] = placer["Firstname"] +" "+placer["lastname"]
                elif name == "Gender":
                    placer["gender"]= db_col.genders[random.randrange(0,len(db_col.genders)-1)]
                elif name == "Country":
                    placer["country"]=db_col.countrylist[random.randrange(0,len(db_col.countrylist)-1)]
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

        with open('GeneratedDataset.csv',"w",newline='') as csvfile:
            headers = cls.genHeaders(listOfHeaders)
            compare = [item.lower() for item in headers]
            writer = csv.writer(csvfile)

            writer.writerow(headers)
            
            for z in range(int(entryNum)):
                dataTB = []
                dict = cls.genData(listOfHeaders)
                for x in compare:
                    dataTB.append(dict[x])
                writer.writerow(dataTB)