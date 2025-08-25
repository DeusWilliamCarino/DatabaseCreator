from module import dbmodules as useModule


# names =data["Firstname"]
# #print(len(data["Firstname"]))
# listOFNames = []
# listOFCountry = []
# filename = "records try.csv"
# rowsforcsv = ["Full Name","Country"]
# dataToCSV = []



# #print(useModule.onlyUnique(names))
# fnamesList =db_col.firstnames
# lnamesList = db_col.lastnames
# countryList = db_col.countrylist

# for x in range (1000):
#     fname = fnamesList[random.randint(0,len(fnamesList)-1)]
#     lname = lnamesList[random.randint(0,len(lnamesList)-1)]
#     country = countryList[random.randint(0,len(countryList)-1)]

#     wholename = fname + " " + lname 
#     listOFNames.append(wholename)
#     listOFCountry.append(country)


# for x in range(len(listOFNames)-1):
#         dataToCSV.append([listOFNames[x],listOFCountry[x]])
# # writing to csv file
# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
#     # writing the fields
#     csvwriter.writerow(rowsforcsv)
#     csvwriter.writerows(dataToCSV)
