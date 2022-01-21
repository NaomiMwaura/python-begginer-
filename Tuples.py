print('creating_tuples')
one_member_tuple=('only member',)
one_member_tuple="only memeber",
one_member_tuple=(['only member',])
print(one_member_tuple)
tup=('strings', 'lists', 'int')
print(tup)
print('empty_tuples_1')
empty_tuple=()
print(empty_tuple)

print('creating_empty_tuples_2')
print(())

tupp='uninterupted', 'files'
print(tupp)

print('nesting_of_tuples')

main_tuple=(one_member_tuple, tup, empty_tuple , tupp)
print(main_tuple)

print('concatenation_of_tuples')

tuple2 = ('print', 'me')
tuple3 = ('give', 'output')
print(tuple2 + tuple3)

print('slicing_in_tuples')
thetuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(thetuple1[1:])
print(thetuple1[::-1])
print(thetuple1[3:])

print('deleting_tuples')
tuple4 = (1, 2)
del tuple4


print(len(tuple1))


list1 = [0, 1, 3]
print(tuple(list1))
print(tuple('python'))

print('repetition_in_tuples')
tuple5 = ('better ')*3
print(tuple5)

print('converting_lists_to_a_tuple')
list1 = '2, 6, 8',
print(tuple(list1))
list2 = 'just you',
print(tuple(list2))

print('tuples_in_a_loop')
tupple6 = ('python',)
n = 5
for i in range(int(n)):
    tupple6 = (tupple6, )
    print(tuple6)






