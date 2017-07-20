# Function definitions go at the top of your file

# returns the total of all the numbers from 1 to n
def numbers(n):
  total = 0
  for i in range(1, n + 1):
    total = total + i
  return total
  
# returns a string with all the numbers from 1 to n
def numbersString(n):
  wholeString = ""
  for i in range(1, n + 1):
    wholeString = wholeString + str(i) + " "
  return wholeString

# Your main code goes down here

user_input = int(input("Pick a number"))
total = numbers(user_input)
print(total)
bigString = numbersString(user_input)
print(bigString)
