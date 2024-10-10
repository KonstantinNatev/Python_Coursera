# EVERY ELEMENTS IN TUPLE ARE IMMUTABLE

my_tuple = (1, 'str', 3.5, True)

# Find out the count of certain element
count = my_tuple.count(3.5)
index = my_tuple.index(3.5)

for item in my_tuple:
    print(item)

print(my_tuple[1])
print(count)
print(index)
