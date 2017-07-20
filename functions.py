def multiply(number1, number2):
  product = number1 * number2
  return product

def average(number1, number2):
  av = (number1 + number2) / 2
  return av
  
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

product = multiply(a, b)
print("The product of these numbers is " + str(product))

average = average(a, b)
print("The average of these numbers is " + str(average))
