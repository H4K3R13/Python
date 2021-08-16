# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:48:07 2021

@author: Arjun C
"""

# Creating a Dictionary 
Dict = {1: 'Apple', 2: 'Banana', 3: 'Carrot'}
print(Dict)

#Values(): Returns a list of all the values in the dictionary
print("Dictionery values are:", Dict.values() )

#keys() :Returns a list containing the dictionary's keys
print("Keys are:",Dict.keys())

#Items(): Returns a list containing a tuple for each key value pair
print("Dictionary iems are:",Dict.items())

#Copy() : Returns a copy of the dictionary
x=Dict.copy()
print("Copied dictionery:",x)

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])

# accessing a element using get() method
print("Accessing an element using get:")
print(Dict.get(3))

#pop() :Removes the element with the specified key
x=Dict.pop(1)
print(x)
print(Dict)

#Popitem() : Removes the last inserted key-value pair
x=Dict.popitem()
print(x)
print(Dict)

#delete a dictionary element with del.
Dict[4]="Egg"
print(Dict)
del Dict[4]
print(Dict)

#Clear(): Removes all the elements from the dictionary
Dict.clear()
print(Dict)

#Dictionary is mutable.
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print(monthNumbers)

# Dictionary is mutable.Add a new entry
monthNumbers['June'] = 6

# change an existing entry
monthNumbers['May'] = 'V'
print(monthNumbers)

 #Dick_Key are view object.Dynamically reflect changes associated with it
birthStones = {'Jan':'Garnet', 'Feb':'Amethyst', 'Mar':'Acquamarine',
'Apr':'Diamond', 'May':'Emerald'}
months = birthStones.keys()
print(type(months))
print(months)
birthStones['June'] = 'Pearl'
print(months)

#For loop to print dict.
keys = []
for e in monthNumbers:
 keys.append(str(e))
 print(keys)

#sort() to sort Dictionary keys 
keys.sort()
print(keys)

#Dictionary key with more than one values-list of values,set of values.
Dict1={'A':{'apricot','Avocado'},'G':['grape','guava'],'F':'Fig'}
print(Dict1)
print(Dict1['A'])

#Nesting of dictionary
Dict2={'A':{'AP':{'apricot','Avocado'}},'G':{'grape','guava'},'F':'Fig'}
print(Dict2)
print(Dict2['A']['AP'])

#dict() method to create dictionary
keys=[1,2,3,4]
values=[100,200,300,400]
x=dict(zip(keys,values))
print(x)