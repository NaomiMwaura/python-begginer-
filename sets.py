'''sets are collecton of elements with no repeat and no insertion order
are used in situatins were there is need or importance for things to be grouped together and not what order they were included
A set is alomst similar to a dictionary and its acollection that is unordered, unchangable and unindexed (so you cannot define them by order)
 and do not allow duplicate values
 sets have curly braces unlike lists'''

set1= {"apple", 'banana', 'cherry'}
print(set1)
#sets do not allow duplicates, the duplicate values are ignored.
set2={'Xiaomi', 'samsung', 'apple', 'sony', 'LG', 'Xiaomi'}
print(set2)
print(len(set2))
set2={'Xiaomi', 'samsung', 'apple', 'sony', 'LG', 'Xiaomi'}
print(set2.pop())
print(set2)
#print(set2.append('oraimo'))
print(set2)
#print(set2.count('Xiaomi'))
set1.update(set2)
print(set1)
#sets can be of different data types
set3= {True, False, 'string', 3, 3.14}
print(set3)
print(type(set1))
print(type(set2))
print(type(set3))

#to access an item in the set you use 'for' loop
for x in set2:
    print(x)
for y in set1:
    print(y)
#print(xiaomi in set2)
#to add items in a set use the .add() and .update() function. you can add lists, tuples or even dictionaries in a set.
set3= {True, False, 'string', 3, 3.14}
set3.add('oraimo')
print(set3)
set2.update(set3)
print(set2)
list1=['morning', 'afternoon', 'evening', 'night']
tup1=('prefer', 'favour', 'like', 'choose')
dict1 = {
    'child1' : {
    'name': 'naomi',
    'ae': 22
    },
    'child2' : {
    'name': "amo",
    'age': 20
    },
    'child3' : {
    'name': 'max',
    'age': 16
    },
}

print(list1)
print(tup1)
print(dict1)

set3.update(list1, tup1, dict1)
print(set3)
set2.update(dict1)
print(set2)
#to remove items from a set use .remov() OR .discard()
set3.remove(True)
print(set3)
set1.discard('banana')
print(set1)
#.clear() empties the set
set1.clear()
print(set1)
#del() deletes the whole set
del(set3)

#to join sets use ,union() or .update() functions
set4={'html', 'java', 'python'}
set5={'css', 'c', 'c++', 'python'}
print(set4)
print(set5)
set6=set4.union(set5)
print(set6)
set4.update(set5)
print(set4)
#the .intersection_update() retains the item that is common or duplicates in both sets
setx={'html', 'java', 'python'}
sety={'css', 'c', 'c++', 'python'}
setx.intersection_update(sety)
print(setx)
#keep all but not duplicates
set_x={'html', 'java', 'python'}
set_y={'css', 'c', 'c++', 'python'}
z=set_x.symmetric_difference_update(set_y)
print(z)
x=set_x.symmetric_difference(set_y)
print(x)

set_x.issubset(set_y)
print()
myset={'cherries', 'apples', 'minions'}
if 'minions' is  myset:
    print('yes !')

print(my_set)

