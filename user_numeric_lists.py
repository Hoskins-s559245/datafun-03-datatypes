"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math
import statistics as stats
import numpy as np
import random as rn
from example_numeric_lists import score_list

#Creats a numpy array from DSCI Measurments.
data = np.loadtxt('DSCI.txt', dtype='int')

#Declare and create lists for Task 3.
list1 = score_list
listx = [*range(10)]
listy =[]
listy2 = []
i = 0

#Convert numpy array from DSCI measurements file to List elements file type
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
def superstats(information):
    s1 = [stats.mean(information), stats.median(information), stats.mode(information), stats.pstdev(information), stats.variance(information)]
    return s1

def corr()






def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = 0  # fix this
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

