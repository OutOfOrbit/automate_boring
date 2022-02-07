# BREAK, CONTINUE, and PASS work the same both WHILE loops & FOR loops
# Example 1: BREAK
avail = 5
req = int(input("How many candies do you want? "))
i = 1
while i <= req:
    if i > avail:
        print("--- OUT OF STOCK ---")
        break
    print('Candy!')
    i += 1
print("Bye-bye!\n")
#
# Example 2:  CONTINUE skips the current iteration only but then continues on with the next iteration
#             The % sign is used to mean "divisible by"
for i in range(1,22):
    if i % 3 == 0 or i % 5 ==0:
        continue
    print(i)
print("Bye-bye!")