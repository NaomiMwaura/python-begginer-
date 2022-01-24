# A tuple is similar to a list except that is a fixed_length and immutable. They are used for small collections of values that don'tneed change, they are represented by () and not [].
one_member_tuple=("only tuple",)
# a tuple can be written without the brackets
tupp= 'clear_beer',
# tuples can be empty
tuple1=()
#tuple concatenation
tuple2=('Geneva', 'conference',)
tuple3=("tuple', 'play",)
print(tuple2 + tuple3)
#nesting of tuples
tuple4='wild', 'house'
tuple5=(tuple2, tuple3, tuple4)
print(tuple5)
# repetition in tuples
tuple2 = (tuple2)*3
print(tuple2)
#slicin tuples
countries= 'mauritius', 'madagascar', 'seychelles', 'comoros', 'eritrea', 'sao_tome_and_principe', 'cape_verde'
print(countries[0:])
print(countries[2])
print(len(tuple5), len(tuple2), len(countries))
#converting lists into a tuples
list1=[1, 2, 3, 4]
print(tuple(list1))
print(tuple('python'))

