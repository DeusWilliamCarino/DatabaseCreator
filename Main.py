import json
import random
from data.dataCollection import trialME
import csv

with open('data/firstNamesSP.json', 'r') as f:
    data  = json.load(f)

names =data["Firstname"]
#print(len(data["Firstname"]))
listOFNames = []
listOFCountry = []
listOfGender = []

for x in range (1000):
    fname = names[random.randint(0,len(names)-1)]
    wholename = fname["name"] + " " + names[random.randint(0,len(names)-1)]["name"] 
    listOFNames.append(wholename)
    listOFCountry.append(fname["country"])
    listOfGender.append(fname["gender"])



filename = "records try.csv"
rowsforcsv = ["Full Name","Country","Gender"]

dataToCSV = []

for x in range(len(listOFNames)-1):
        dataToCSV.append([listOFNames[x],listOFCountry[x],listOfGender[x]])
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(rowsforcsv)
    csvwriter.writerows(dataToCSV)
        