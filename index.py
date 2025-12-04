
# # # # # # # # content=["awsome","super",'fantastic']
# # # # # # # # x,y,z =content
# # # # # # # z = -3255522
# # # # # # # x= 1.75
# # # # # # # def myfunc():
# # # # # # #     # global z
# # # # # # #     # z="awsome"
# # # # # # #     print("python is ",int(x))
# # # # # # # myfunc ()
# # # # # # # print("second commond ",complex(z))
# # # # # # import random
# # # # # # print (random.randrange (100 and 1000))
# # # # # a= 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Esse ab molestiae totam, facilis quisquam voluptatem recusandae quam soluta dicta. Debitis unde cum ipsum, eaque nam voluptatum voluptate et totam vel'
# # # # # if 'dolr'in a:
# # # # #   print (len(a))
# # # # # b = "Hello, World!"
# # # # # print(b.split(","))
# # # # age = 21
# # # # txt =f"my name is jayachadran {age:2f}"
# # # # print (txt)
# # # txt = "we are called indian \n viking\' from the north"
# # # print (txt)

# # class mycls():
# #     def __len__(self):
# #         return 0

# # myobj = mycls()
# # print(bool(myobj))
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def add(self):
#       data = self.name + self.age
#       return data
#   def sub(self):
#      data = self.name - self.age
#      return data
# myobject = Person(56, 36)

# print (myobject.sub())
# Ask for user's name
class Calculator:
    """A simple calculator class for basic operations."""

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b
class Love:
    def lovedata(self,new_name):
        lovedata = new_name =="love"
        return lovedata

# Chatbot logic
name = input("Enter Your Name: ")


if name:
    bot = "moon"
    calc = Calculator()
    # Myobj = Love()  # create calculator object
    print(f"Hello I'm {bot}: How can I help today?")
# if Myobj ==True:
    # print(Myobj.lovedata("love"))  


    while True:
        user_input = input(f"{name}: ").lower()

        # Exit condition
        if user_input in ["exit", "quit", "bye"]:
            print(f"{bot}: Goodbye {name}, have a great day!")
            break
        elif user_input in ["name"]:
    # Remove the keyword "name" and trim spaces
            new_name = input(f"Change The BOt {bot} Name into :")    
            if new_name:
             bot = new_name
             print(f"Bot name changed! Now I am {bot}.")
            else:
             print(f"{bot}: Please provide a valid new name.")



        # Greeting response
        elif user_input in ["hi", "hello"]:
             print(f"{bot}: Hi {name}, how can I help you?")

        # Addition
        elif user_input in ["add", "+"]:
            try:
                num1 = float(input("First Number: "))
                num2 = float(input("Second Number: "))
                print(f"{bot}: The Addition Of Two Numbers Is: {calc.add(num1, num2)}")
            except ValueError:
                print(f"{bot}: Please enter valid numbers!")

        # Subtraction
        elif user_input in ["sub", "-"]:
            try:
                num1 = float(input("First Number: "))
                num2 = float(input("Second Number: "))
                print(f"{bot}: The Subtraction Of Two Numbers Is: {calc.sub(num1, num2)}")
            except ValueError:
                print(f"{bot}: Please enter valid numbers!")

        # Multiplication
        elif user_input in ["mul", "*"]:
            try:
                num1 = float(input("First Number: "))
                num2 = float(input("Second Number: "))
                print(f"{bot}: The Multiplication Of Two Numbers Is: {calc.mul(num1, num2)}")
            except ValueError:
                print(f"{bot}: Please enter valid numbers!")

        # Division
        elif user_input in ["div", "/"]:
            try:
                num1 = float(input("First Number: "))
                num2 = float(input("Second Number: "))
                print(f"{bot}: The Division Of Two Numbers Is: {calc.div(num1, num2)}")
            except ValueError:
                print(f"{bot}: Please enter valid numbers!")

        # Default response
        else:
            print(f"{bot}: Sorry, I didn't understand that.")

