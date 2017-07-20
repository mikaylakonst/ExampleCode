# This is a for loop.
# x takes on the values 1, 2, 3, and 4.
# The left end of the range is inclusive.
# The right end of the range is exclusive.
# In other words, the range is [1, 5).

for x in range(1, 5):
  print(x)

# This is a while loop.
# Every time the loop executes,
# x is printed, and then x is increased by 1.
# x takes on the values 1, 2, 3, and 4.
# This loop does the same thing as the for loop above.

x = 1
while x < 5:
  print(x)
  x = x + 1

# This is also a while loop.
# A loop that starts with while True
# will run forever unless it is broken
# by a break statement.
# This loop does the same thing as the loops above.

x = 1
while True:
  print(x)
  x = x + 1
  if x >= 5:
    break
