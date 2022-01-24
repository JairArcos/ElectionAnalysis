import string


counties = ["Arapahoe","Denver","Jefferson"]
x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

#Iterate through a Dictionary
counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county in counties_dict:
    print (county)
  
for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)

#Get the values of a Dictionary
for voters in counties_dict.values():
    print(voters)

#List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#using F-string
ounties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")