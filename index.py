class Calculator:
    """A simple calculator class for basic operations."""
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return "Error: Division by zero!" if b == 0 else a / b


class Love:
    def lovedata(self, new_name):
        return new_name.lower() == "love"


# Chatbot logic
name = input("Enter Your Name: ")
Myobj = Love()

if name:
    bot = "moon"
    calc = Calculator()

    # Map user commands to calculator methods
    operations = {
        "add": ("Addition", calc.add), "+": ("Addition", calc.add),
        "sub": ("Subtraction", calc.sub), "-": ("Subtraction", calc.sub),
        "mul": ("Multiplication", calc.mul), "*": ("Multiplication", calc.mul),
        "div": ("Division", calc.div), "/": ("Division", calc.div),
    }

    print(f"Hello I'm {bot}: How can I help today?")

    while True:
        user_input = input(f"{name}: ").lower()

        if user_input in ["exit", "quit", "bye"]:
            print(f"{bot}: Goodbye {name}, have a great day!")
            break

        elif user_input == "name":
            new_name = input(f"Change The Bot {bot} Name into: ")
            if new_name:
                bot = new_name
                print("Love detected! Beginning chat ❤️" if Myobj.lovedata(new_name)
                      else f"Bot name changed! Now I am {bot}.")
            else:
                print(f"{bot}: Please provide a valid new name.")

        elif user_input in ["hi", "hello"]:
            print(f"{bot}: Hi {name}, how can I help you?")

        elif user_input in operations:
            try:
                num1, num2 = float(input("First Number: ")), float(input("Second Number: "))
                op_name, op_func = operations[user_input]
                print(f"{bot}: The {op_name} Of Two Numbers Is: {op_func(num1, num2)}")
            except ValueError:
                print(f"{bot}: Please enter valid numbers!")

        else:
            print(f"{bot}: Sorry, I didn't understand that.")
