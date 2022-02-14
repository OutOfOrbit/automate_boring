# Scope is EITHER local or global.  It CAN NOT be both (same variable name can have different values).
# A Global variable is destroyed when the program ends.
# Think of Local variables as being temporary, as they are DESTROYED when the function ends.
# A "Local" variable CAN NOT be used OUTSIDE the function.
# However, code in a "Local" scope **CAN** use "Global" variables.

#def spam():
#    eggs = 99
#    saussage = ()
#    print(f"The value of the 'eggs' variable in the 'spam' function is {eggs}")
#    
#def bacon():
#    ham = 101
#    eggs = 0
#    print(f"The value of the 'eggs' variable in the 'bacon' function is {eggs}")
#
#spam()
#bacon()
#
# A function can access a Global variable UNLESS a function with the same name is defined locally.
# HOWEVER...  in order to **modify** a global variable FROM WITHIN A FUNCTION, need to
# ...add a "Global statement" to the top of the function

eggs = 33

def spam():
#    global eggs
    eggs = 99

spam()

print(eggs)
