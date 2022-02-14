# Some functions have "keyword arguments" which default to a certain value when they are run.
#
# For example, the "print" function usually adds a "newline" character to the end of the line that it prints.
# When can override this by doing as follows...
print('Hollow ', end='')
print('World')
#
# Also... when feeding multiple strings to a print function, they are automatically separated by a single space by default.
# We can use the "sep" keyword argument to change what is used to separate the arguments!
print('cat', 'dog', 'bird', 'donkey', sep='CRAP!!')