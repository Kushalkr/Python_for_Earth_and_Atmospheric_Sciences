#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Kushal Keshavamurthy Raviprakash
"""

a = ["Luke", "Leia", "Obiwan"]
b = ["Yoda", "Vader", "Death Star"]
c = ["Storm Trooper", "R2D2"]

# Solution:

d = a + b + c # concatenating the list items.

# Method 1: using del
print("Method 1: Using del")
print("Before: ", d)
del d[4], d[4], d[4]
# Err what?! yeah that's right. because 4 is the index "Vader"
# in the list d. but when you delete "Vader", "Death Star"
# occupies index 4 and same happens to "Storm Trooper".
print("After: ",d,"\n")

# Method 2: Using the remove(method)
d = a + b + c     # Resetting list d
print("Method 2: Using remove()")
print("Before: ", d)
d.remove('Vader')
d.remove('Death Star')
d.remove('Storm Trooper')
print("After: ",d,"\n")

# Method 3: Using the pop() method
d = a + b + c     # Resetting list d
print("Method 3: Using pop()")
print("Before: ", d)
d.pop(4)
d.pop(4)
d.pop(4)
print("After: ",d,"\n")

# Part two of the exercise

address = [1001, "East", "10th", "street", "GY428", "Bloomington", "IN", 47408]

print(address[0] + address[-1])
address[1] = "North"
print(address)
