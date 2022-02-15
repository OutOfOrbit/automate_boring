# Accessing items in a List spam = ['cat', 'dog', 'bird', 'horse', 'monkey', 'fish', 'frog'] print(spam[3])

# Accessing items in nested Lists
spam = [['cat', 'dog', 'bird'],['horse', 'monkey', 'fish', 'frog']]
print(spam[0])
print(spam[1][2])


# Accessing items in nested Lists **starting from the end**
spam = [['cat', 'dog', 'bird'],['horse', 'monkey', 'fish', 'frog']]
print(spam[1][-1])


# Concatenate List
spam1 = ['cat', 'dog', 'bird']
spam2 = ['horse', 'monkey', 'fish', 'frog']
print(spam1 + spam2)

# Use a slice to get a series of values from a list ****the output of a SLICE is a LIST****
spam3 = ['cat','dog','bird','donkey','dinosaur','skunk','horse', 'monkey', 'fish', 'frog']
print(spam3[:3])

# Assign a new value to a List item (by index)
spam3 = ['cat','dog','bird','donkey','dinosaur','skunk','horse', 'monkey', 'fish', 'frog']
spam3[2] = 'YABADABADOOOO!'
print(spam3)

# Assign a new value to a SERIES of List items (using a SLICE)
spam3 = ['cat','dog','bird','donkey','dinosaur','skunk','horse', 'monkey', 'fish', 'frog']
spam3[1:3] = '$$$$$','%%%%%'
print(spam3)

# Assign a new value to a SERIES of List items (using a SLICE)
spam3 = ['cat','dog','bird','donkey','dinosaur','skunk','horse', 'monkey', 'fish', 'frog']
del spam3[4]
print(spam3)

# There is even a "list function" that returns a List of the values that were passed to it as a String
print(list('Howdy!'))

# Use the "in" operator to determine if an item is IN a list
print('BULL' in stuff4)

# Use the "not in" operator to determine if an item is NOT IN a list
print('BULL' not in stuff4)