"""
Student Name: Ash Hoskins, Student #S559245
Course: CSIS 44-609 - Data Analytics Fundamentals
Professor Denise Case
Domain: Geospatial data
Module 3: Assignment 1 Task 5.

Working with Tuples and Dictionaries.

"""

lakelat = (48.053, 44.757, 42.845, 42.248, 43.628)
lakelong = (-87.097, -82.334, -86.947, -81.148, -77.617)

with open("Lakes.txt", "r") as fileObject:
    text = fileObject.read()
    items = text.split(',')
    values = set(items) 

#Zip each tuple to make long/lat coordinates of each great lake
combine = zip(lakelat,lakelong)
print()
print("Combines list of longitude and Latitude coordinates of the Great Lakes: ", list(combine))

#concatenation the list even though it makes no sense
conc = lakelat + lakelong
print()
print("A Concatenation of the coordinates:" ,conc)

#Check tuple for 42.845 in lake latitude tuple
hasfirtytwo = 42.845 in lakelat
print()
print(f"{hasfirtytwo = }")

#Testing tuple indexing
first = lakelat[0]
second = lakelat[1]
third = lakelat[2]
last = lakelat[-1]
print()
print("The elements of the lake lattitude tuple are: ")
print(f"{first = }")
print(f"{second = }")
print(f"{third = }")
print(f"{last = }")


#Set tuples to sets and test intersection, union, and difference
set1 = set(lakelat)
set2 = set(lakelong)

#Union
Union = set1 | set2
#intersection Set to intersect self, to display something other than false.
Intersection = set1 & set1
#Difference
Difference = set1 - set2

print()
print(f"{Union = }")
print(f"{Intersection = }")
print(f"{Difference = }")

print(values)


#Word Count dictionary from lakes.txt 
word_counts_dict = {}
for word in items:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

print("The words are unique from the lakes.txt list: ", word_counts_dict)

#Character count dictionary from lakes.txt
characters = {}
for word2 in text:
    if word2 in characters:
        characters[word2] += 1
    else:
        characters[word2] = 1

print("Individual Character counts from the lakes.txt list: ", characters)

#Dictionary of Lakes.txt with Longtitude and Latitude sets
information = {
    "Name" : items,
    "Latitude" : lakelat,
    "Longitude" : lakelong
}

for key, value in information.items():
    print(key, value)

#Comprehension - This is going to suck so bad
something = {word: text.count(word) for word in text}

print()
print("Individual Character counts utilizing comprehension from file read")
print()
print(something)


