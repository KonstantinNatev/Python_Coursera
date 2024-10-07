string = 'Hello'
array = ['Creme World', 'Python', 'Cherry World', 'Apple World']

for letter in string:
    print(letter)

for index in range(10):
    print('Looping...', index)

# display the index of position and the value in array
#  enumerate() returns a tuple containing a count (from start which defaults to 0)
for idx, item in enumerate(array):
    print(idx, item)

count = 0

while count < len(array):
    print("word from array", array[count])
    count += 1