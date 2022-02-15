# Can get the LENGTH of a List the same way as a String, using the "len function"
from re import I


word = 'Wordy\n'
words = len(word)
print(words)

stuff = [53,77,82,39,57,65,41,6]
whatLength = len(stuff)
print(whatLength)

# Lists can be CONCATENATED just like Strings, using +
stuff2 = ['Boston cream','Blueberry','Apple fritter']
stuff3 = [3,2,1]
stuff4 = ['fish','chicken','pasta','\n']
print(stuff + stuff3)
print(stuff2 + stuff4)
word2 = 'Loud'
print(word + word2)

# Lists can be REPLICATED just like strings, using *
print(word * 4)
print(stuff4 *3)