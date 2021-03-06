# This is a for loop.
# x takes on the values 0, 1, 2, 3, and 4.
# The left end of the range is inclusive.
# The right end of the range is exclusive.
# In other words, the range is [0, 5).

for x in range(0, 5):
  print(x)
  
# This is another for loop.
# x takes on the values 0, 1, 2, 3, and 4. In other words,
# x takes on all values between 0 (inclusive) and 5 (exclusive).
# This loop is equivalent to the for loop above
# and prints the exact same thing.

for x in range(5):
  print(x)
  
# This for loop does the same thing as the other ones.
# x goes from 0 to 5 by steps of size +1.
# As before, the 0 is inclusive and the 5 is exclusive,
# so x takes on the values 0, 1, 2, 3, and 4.
for x in range(0, 5, 1):
  print(x)

# This is a while loop.
# Every time the loop executes,
# x is printed, and then x is increased by 1.
# x takes on the values 0, 1, 2, 3, and 4.
# This loop does the same thing as the for loop above.

x = 0
while x < 5:
  print(x)
  x = x + 1

# This is also a while loop.
# A loop that starts with while True
# will run forever unless it is broken
# by a break statement.
# This loop does the same thing as the loops above.

x = 0
while True:
  print(x)
  x = x + 1
  if x >= 5:
    break

