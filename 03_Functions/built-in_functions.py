# Need to start by "importing" the function
# To use a function, specify the module name + dot + the function name
import random

guess = random.randint(1,10)
print(guess)
#
# Import MULTIPLE MODULES on the same line just by separating the module names by a comma
import random, sys, os, math
#
# ALTERNATIVE FORM of "import" statement
# If done this way, you no longer have to specify the module name when calling the funtion
# Downside is that the code is less "readable"
from random import *
x = randint(91,99)
print(x)
#
# Example of a useful function in a module:  Quit program before it reaches the end using:  sys.exit()
import sys
print('start')
sys.exit()
print('end')
