# Getting started with WHILE loops
#spam = 0
#while spam < 5:
#    print('Hollow World from Hell!')
#    spam = spam +1
#
# WHILE loop - Example 2
#name = ''
#while name != 'your name':
#    name = input("Please print your name and press Enter: ")
#print("Thanks dufus!")
#
# Breaking out of an INFINITE LOOP!!!
#name = ''
#while True:
#    name = input("Please print your name and press Enter: ")
#    if name == 'your name':
#        break
#print("Thanks dufus!")
#
# Using CONTINUE to jump back to the start of the loop!!!
spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
