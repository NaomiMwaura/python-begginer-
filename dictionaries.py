#Dictionaries are used to store data values in key:value pairs
#A dictionary is a collection which is ordered, changable and do not allow duplicates
#They are written in curly brackets {} and have key values
#each pair is separated by a comma and key values are separated by a colon
dict = {
    'kenya' : 'Nairobi',
    'Ugamnda' : 'Kampala',
    'Tanzania' : 'Dodoma',
    'Somalia' : 'Mogadishu',
}
print(dict)
dict2 = {
    'Brand' : 'Ford',
    'Moedel' : 'Mustang',
    'Year' : 1964
}
print(dict2)
#Dictionary items are ordered, changable and do not allow duplicates
#presented in key:value pairs_reffered to using the key name
dict3 = {
    "Phill" : 30,
    "Cecil" : 25,
    "Omi" : 22,
    "Amo" : 20,
    "Max" : 16,
}
print(dict3)
print(dict3["Omi"])
print(dict3)
#Dictionaries cannot have two items with the same key
#lengt of a dictionary
print(len(dict3), len(dict2))
#dictionary data types
#dictionaries can be of any data types
thisdict = {
    "Brand" : "Ford",
    "Electric" : False,
    "Colors" : ['red', 'black', 'white', 'blue'],
    "year" : 1964,
}
print(thisdict)
#dictionaries are defined as data types 'dict'
print(type(thisdict))
mydict = {
    'United_Arab_Emirates' : 'Abu_Dhabi',
    'Japan' : 'Tokyo',
    'Thiland' : 'Bangkok',
    'China' : 'Beijing',
    'Qatar' : 'Doha',
}
x = mydict['Thiland']
print(x)

y = mydict['China']
print(y)

r = mydict.get('Qatar')
print(r)

x1 = mydict.keys()
print(x1)
x2 = mydict.values()
print(x2)

#Getting items in a dictionary
#The items methods changes the dictionary into tuples in a list
x = mydict.items()
print (x)

#changing the values in the dictionary
dictionary1 = {
    'brand' : 'ford',
    'model' : 'mustang',
    'electric' : False,
    'year' : 1964
}
print(dictionary1)
#before the change
y = dictionary1.values()
print(y)

dictionary1['year'] = 2020
#after the change
y = dictionary1.values()
print(y)

x = dictionary1.keys()
print(x)

dictionary1['model'] = "mercedes"
x = dictionary1.keys()
print(x)
#to check if keys exist in a dictionary
if 'model' in dictionary1:
    print('yes, "model" is one of the keys in dictionary1')

if "year" in dictionary1:
    print("yes, 'year' is one on the keys in dictionary1")

#updating a dictionary using update() command
cardict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}
print(cardict)
cardict.update({"Color" : "Red",})
print(cardict)

cardict.update({"Color" : ["Red", "Black", "White", "Grey"],})
print(cardict)
#deleting items in the dictionary using .pop(), while
# .del() copletely deletes the dictionary
#.clear() clears all the items in the dictionary
# .popitem() removes a random item in the dictionary
#loops in dictionaries, for function is used in looping through a dictionary

cardict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}
#to print all key names in the dictionary
for (x) in cardict:
    print(x)
for (x) in cardict.keys():
    print(x)
#to print all values in the dictionary
for (x) in cardict:
    print(cardict[x])
for (x) in cardict.values():
    print(x)
#to output both keys and values
for (x,y) in cardict.items():
    print(x,y)
#coping a dictionary
cardict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}
dictionary2 = cardict.copy()
print(dictionary2)

dictionary3 = dict(cardict)
print(dictionary3)
#nested dictionaries
famdict = {
    'child1': {
    'name' : 'naomi',
    'year': 2000,
    },
    'child2' : {
        'name' : 'amos',
        'year' : 2002,
    },
    'child3' : {
    'name' : 'max',
    'year' : 2006
    }
}

print(famdict)

child1 = {
        'name': 'naomi',
        'year': 2000,
}
child2 = {
        'name': 'amos',
        'year': 2002,
}
child3 = {
        'name': 'max',
        'year' : 2006,
}

myfamily = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3,
}
print(myfamily)