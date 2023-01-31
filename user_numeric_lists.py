"""

Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Domain: Geospatial data
Module 3: Assignment 1 Task 3.

Working with List.


"""

# import some modules first - how many can you make use of?


import statistics as stats
import numpy as np
import random as rn
import math

#Creats a numpy array from DSCI Measurments.
data = np.loadtxt('DSCI.txt', dtype='int')

#Declare and create lists for Task 3.
list1 = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]
listx = [*range(10)]
listy =[]
listy2 = []
i = 0

#Convert numpy array from DSCI measurements file to List elements data type apparently not needed in this project
for n in data:
    listy.append(n)

#Task 3 Step 4.) Create listy so the values are pretty much linear, 
#but not exactly - we'll draw a straight-line through the data to make predictions.
while i != len(listx):
    listy2.append(listx[i] + rn.randrange(0,10))
    i+= 1

# define some functions
#Task 3. List 1: function that takes all data from a given list 
#and provides all statistical information.
def superstats(info):
    s1 = [stats.mean(info), stats.median(info), stats.mode(info), stats.pstdev(info), stats.variance(info)]
    return s1

#Task 3 List 2: Calculates correlation between two lists and 
#predicts new y value based on future value of 15; returns list with both results.
def corr(xlist, ylist):
    fv = 15
    slope, intercept = stats.linear_regression(xlist, ylist)
    y = float(slope * fv + intercept)
    xx = stats.correlation(xlist, ylist)
    s2 = [xx, y]
    return s2
    
#Task 3 List 3. Utilizing built in python functions on lists. Returns list of results.
def list3(newlist):
    minx = np.min(newlist)
    maxx = np.max(newlist)
    lenx = len(newlist)
    sumx = sum(newlist)
    avgx = round(sumx/lenx)
    setx = set(newlist)
    sort1x = sorted(newlist)
    sort2x = sorted(newlist, reverse= True)

    s3 = [minx, maxx, lenx, sumx, avgx, setx, sort1x, sort2x]
    return s3

#Task 3 List 4. List methods
def methody(anotherlist1, anotherlist2):
    
    anotherlist1.append(700)
    print("Appended list with the value 700: ", anotherlist1)
    anotherlist1.extend(anotherlist2)
    print("Extended list with a 2nd list: ", anotherlist1)
    anotherlist1.insert(5, 277)
    print("Inserted value of 277 at position 5 of the list ", anotherlist1)
    anotherlist1.remove(700)
    print("Removed 700 from the list", anotherlist1)
    number = anotherlist1.count(93)
    print("The number of times 93 exists in the list is: ", number, " Times")
    lst = sorted(anotherlist1)
    print("Display the list sorted",lst )
    rlist = sorted(anotherlist1, reverse= True)
    print("Display the list reverse sorted", rlist)
    print("The first element in the list: ", anotherlist1[0],)
    anotherlist1.pop(0)
    print("The Resulting list after the removal of the first elemental is", anotherlist1)
    v = len(anotherlist1)
    print("The Last Element on the list is ", anotherlist1[v-1])
    anotherlist1.pop(v-1)
    print("Removal of the Last element in the list results the final list of: ", anotherlist1)

    return anotherlist1


#Task 3. List 5. List Transformations. Filter function that 
#returns boolean on if the value is less than or equal to 100 
def filter1(list2):
    if list2 <= 100:
        return True
    else:
        return False

#Task 3. List 5 Map function utilizes the map method of taking the 
#cube root of each element in a given list
def map1(it):
    
    zz = list(map(lambda x: np.cbrt(x), it))
    aa =np.around(zz, decimals=2)

    return aa

#Task 3 List 5 Calculating the Volume of a given list of sides. 
#Utlizing the Map method.
def vol(attribute):
    dz = list(map(lambda x: math.pow(x,3), attribute))

    return dz

#Task 3 List 6. Use List Comprehension to get x such that x is less than or equal to 100
def comp1(list): 

    da = [x for x in list if x <= 100]
    return da

#Task 3 List 6. USe list comprehension to get x^3 for each value in the list.
#for simplistic reasonings used listx instead of list1; so the terminal isn't spammed with alot of numbers.
def comp2(list):
    db = [math.pow(x,3) for x in list]
    return db

#Task 3 list 6. Custom Transformation
def comp3 (list):
    dc = [x for x in list if x <= 100]
    dd = np.around([np.sqrt(x) for x in dc], 2)
    return dd


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?
    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = length * width  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    statinfolisty = superstats(listy)
    correl = corr(listx, listy)
    builtin = list3(listy)


print()
print("List 1 Tasks are as follows:")
print()
print("The Mean of List y is: ", statinfolisty[0], " The Median is: ", statinfolisty[1], " The Mode is: ", statinfolisty[2])
print("The Standard Dev is: ", round(statinfolisty[3], 2), " and the variance is: ", statinfolisty[4])
print()
print("List 2 Tasks are as follows:")
print("Calculating the future prediction between two lists provides: ", round(correl[1],2), " at future value 15")
print("The correlation percentage between the teo list is: " , round(correl[0],2))
print()
print("List 3 Tasks are as follows: ")
print("The Minimum value on the list is: ", builtin[0], " The maximuim value on the list is: ", builtin[1], " The Length of the list is: ", builtin[2], "The Sum of the List is:", builtin[3])
print("The Length of the Average of the list is: ", builtin[4], " The Set of the List is", builtin[5])
print("The List being sorted directly is: ", builtin[6])
print("The List being reversed sorted is: ", builtin[7])
print()
print("List 4 Tasks are as follows: ")
methody(listx, listy)
print()
print("List 5 Tasks are as follows:")
print("Elements in the list that are less than or equal to 100", list(filter(filter1, list1)))
print("Using a map to take the cube root of the list", map1(listx))
print("Calculating the volume of a list of sides: Starting list is", listx)
print("Resulting list of Volumes is", vol(listx))
print()
print("List 6 Task list are as follows:")
print("Utilize List Comprehension to get values of 100 or less", comp1(listx))
print("Utilize List Comprhension to raise each element to the power of 3: Used list y for simpler display", comp2(listy))
print("A custom transformation that looks for entries under 100 and square roots the element", comp3(listx))

# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

