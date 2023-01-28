"""
Modify this docstring.

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

#Convert numpy array from DSCI measurements file to List elements data type
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
    min = min(newlist)
    max = max(newlist)
    len = len(newlist)
    sum = sum(newlist)
    avg = round(sum/len)
    set = set(newlist)
    sort1 = sorted(newlist)
    sort2 = sorted(newlist, reverse= True)

    s3 = [min, max, len, sum, avg, set, sort1, sort2]
    return s3

#Task 3 List 4. List methods
def methody(anotherlist1, anotherlist2):
    
    lst = anotherlist1.append(700)
    lst = anotherlist1.extend(anotherlist2)
    lst = anotherlist1.insert(5, 277)
    lst = anotherlist1.remove(700)
    lst = anotherlist1.append(lst.count(93))
    lst = anotherlist1.sort()
    lst = anotherlist1.sort(reverse = True)
    lst.pop(0)
    
    v = len(lst)
    
    lst.pop(v-1)
    return lst
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
print(list(filter(filter1, list1)))
print(vol(listx))



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

