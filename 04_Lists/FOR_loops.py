# A "for" loop repeats a code block once for each value in a List (or list-like value).
for i in range(5):
    print(i)

print(range(4))

# These "list-like values" are of the "SEQUENCES" data-type
# The "list function" creates a list from a sequence...
new_list = list(range(5))
print(new_list[2])

letters = list('Yikes!')
print(letters[4])

increment_list = list(range(0,100,7))
print(increment_list)

# **** Get the list of indexes of items inside a List using "range(len())" *****
supplies = ['pens','staplers','flame-throwers','binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i] + '\n')
