"""
Modify this docstring.

"""

# imports first
import random as rn


countries = ['Chile', "United States", "Canada", "Mexico", "Columbia"]
cities = ['Santiago', "Los Angelas", "Toronto", "Tijuana", "Bogota"]
landscape = ['Mountains', 'Plains', 'Artic', 'Desert', "Forest"]
dsci = ['D1', 'D3', 'D1','D4', 'D0']
rainfall = ['Less than 3000', 'Less than 2000', 'Less than 3000', 'Less than 1000', 'Greater than 3000']

#with open("DSCI.txt", "r") as fileObject:
#    text = fileObject.read()
#    items = text.split() 
#    values = set(items) 

#String Lists 1. Using Python Built-in Functions 
list1 = list(zip(countries, cities, landscape, dsci, rainfall))

# reusable functions next

#String Lists 2. Random Choice function information
def city(name, sets):
    cn, ci, ld, ds, rain = zip(*sets)
    i = 0

    while name != ci[i]:
        i+=i 
    
    if name == ci[i]:
        print(name, " Is The Capital of: ", cn[i] )
        print("The landscape is generally made up of: ", ld[i])
        print("The Drough Severity and Coverage Index is: ", ds[i])
        print("This DSCI indicated a rain fall of", rain[i], "mm per year")






# call functions and execute code
#Randomly select a city and pass it to the function
z = rn.choice(['Santiago', "Los Angelas", "Toronto", "Tijuana", "Bogota"])
city(z, list1)

#print()
#print("The list of DSCI values for Santiago are: ", items)


# use if __name__ == "__main__":
