#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Kushal Keshavamurthy Raviprakash
"""

myaddress = {'street':"1001 E10th Street, GY428", 'city':"Bloomington",
 'state':"IN", 'PIN':"47408"}
print(myaddress)

fulladdress = myaddress['street'] + \
myaddress['city'] + \
myaddress['state'] + myaddress['PIN']

print(fulladdress)

print(myaddress.keys())
myaddress['PIN'] = "47405"
