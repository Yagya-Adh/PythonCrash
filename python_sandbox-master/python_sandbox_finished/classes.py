# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:

    # Constructor
    def __init__(self, name, email, age):

        # Note # python has self  instead of this
        self.name = name
        self.email = email
        self.age = age

        # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
        # Encapsulated variables are declares with '_' in the constructor.
        self._private = 1000

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

   # function for encap variable
    def print_encap(self):
        print(self._private)


yagya = User('Yagya Adhikari', 'yagya@mail.com', 27)

# print(type(yagya))
# print(type(yagya.age))

# print(yagya.name)
# print(yagya.email)
# print(yagya.age)

# print(yagya.greeting())


# yagya.has_birthday()
# print(yagya.greeting())

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        # Called proper parent class constructor to make this as proper child inehriting all methods.
        User.__init__(self, name, email, age)
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


#  Init user object
yagya = User('Yagya Adhikari', 'yagya@mail.com', 27)

# Init customer object
ananda = Customer('Ananda Adhikari', 'ananda@mail.com', 25)

ananda.set_balance(500)
print(ananda.greeting())

yagya.has_birthday()
print(yagya.greeting())

# Encapsulation -->
# yagya.print_encap()
# yagya._private = 800  # Changing for yagya
# yagya.print_encap()

# # Method inherited from parent
# # Changing the variable for yagya doesn't affect janets variable --> Encapsulation
# ananda.print_encap()
# ananda._private = 600
# ananda.print_encap()

# # Similary changing ananda's doesn't affect yagya's variable.
# yagya.print_encap()
