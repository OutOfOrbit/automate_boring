# Setting this up to get an error on purpose...
#
#def div42by(divideBy):
#    return 42 / divideBy
#
#print(div42by(2))
#print(div42by(11))
#print(div42by(0))
#print(div42by(21))
#print(div42by(42))
#
# Instead of getting that long error and the program EXITING WITHOUT COMPLETING THE REMAINING COMMANDS...
# ... can use a "try/except" statement
#
#def div42by(divideBy):
#    try:
#        return 42 / divideBy
#    except ZeroDivisionError:
#        print('Error: You tried to divide by zero.')
#
#print(div42by(2))
#print(div42by(11))
#print(div42by(0))
#print(div42by(21))
#print(div42by(42))

# Can also use a general "try/except" without specifying which Error to watch for (run this & answer with a string)
#print("How many cats do you have?")
#numCats = input()
#if int(numCats) >= 4:
#    print("Ok, you're not tooo crazy.")
#else:
#    print("You really are crazy!")
#
# Now try again
print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("Ok, you're not tooo crazy.")
    else:
        print("You really are crazy!")
except:
    print("Sorry, you need to enter a number(digits)")