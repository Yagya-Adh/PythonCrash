# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name='Sam'):
    print(f'Hello {name}')


# # Return values
# def getSum(num1, num2):
#     total = num1 + num2
#     return total


# # A lambda function is a small anonymous function.
# # A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# getSum = lambda num1, num2: num1 + num2

# print(getSum(10, 3))



""" function with arg  """
# def mero(name,age):
#     print(f'hello my name is {name} and im {age} years old.')

# mero('yagya',27)




""" function with return value """
# def add(a,b):
#     total = a + b
#     return total

# print(add(2,3)) ##we need to wrap function with print() while calling


""" lambda function  """
getSum = lambda num1, num2: num1 + num2 #this like arrow function in js
print(getSum(10,20))
