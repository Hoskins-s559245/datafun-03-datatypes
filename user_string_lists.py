"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Domain: Geospatial data
Module 3: Assignment 1 Task 4.

Working with String Lists
"""

# imports first
import random as rn


countries = ['Chile', "United States", "Canada", "Mexico", "Columbia"]
cities = ['Santiago', "Washington D.C", "Ottowa", "Tijuana", "Bogota"]
landscape = ['Mountains', 'Plains', 'Artic', 'Desert', "Forest"]
dsci = ['D1', 'D3', 'D1','D4', 'D0']
rainfall = ['Less than 3000', 'Less than 2000', 'Less than 3000', 'Less than 1000', 'Greater than 3000']


#String Lists 3. Get Unique Words from file
with open("DSCI.txt", "r") as fileObject:
    text = fileObject.read()
    items = text.split() 
    values = set(items) 

#String Lists 1. Using Python Built-in Functions 
list1 = list(zip(countries, cities, landscape, dsci, rainfall))

# reusable functions next

#String Lists 2. Random Choice function information
def city(name, sets):
    cn, ci, ld, ds, rain = zip(*sets)
    i = 0

    while name is not ci[i]:
        i = i + 1 
    
    if name == ci[i]:
        print(name, " Is The Capital of: ", cn[i] )
        print("The landscape is generally made up of: ", ld[i])
        print("The Drough Severity and Coverage Index is: ", ds[i])
        print("This DSCI indicates a rain fall of", rain[i], "mm per year")
        i = 0



# call functions and execute code
#Randomly select a city and pass it to the function
z = rn.choice(['Santiago', "Washington D.C", "Ottowa", "Tijuana", "Bogota"])
city(z, list1)

#Set value of length of values from DSCI file.
dz = len(values)



# use if __name__ == "__main__":
#String Lists 3. Get Unique Words from file
if __name__ == "__main__":

    print()
    print("The list of DSCI values for Santiago are: ", items)
    print("List of Unique DSCI Values for Santiago are: ", values)
    print("List of Values sorted:", sorted(values))
    print("The length of the list is: ", dz)
    
