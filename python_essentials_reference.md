🧠 Python "Anti-Blank Screen" Reference Guide

🎯 CORE PRINCIPLE: The 3-Step Anti-Panic Strategy

When the screen is blank and you feel stuck, STOP trying to remember the whole program. Instead:

Identify the Action: What do I need to do? (e.g., store a number, make a decision, repeat a task).

Find the Recipe: Look below for the correct structural "recipe."

Copy the Structure: Write out the structure first, then focus on filling in the unique details.

1. DATA STORAGE RECIPES (Variables & Collections)

1A. Basic Variable Assignment

(Stores a single value of any type.)

# [Type 1] Text (String)
user_name = "Chris"

# [Type 2] Whole Number (Integer)
player_score = 42

# [Type 3] Decimal Number (Float)
damage_multiplier = 1.5

# [Type 4] True/False (Boolean)
is_running = True


1B. List (Ordered Collection)

(Stores an ordered sequence of items, accessed by index [0, 1, 2...])

# Recipe: Create a list of items
my_inventory = ["Sword", "Shield", "Potion"]

# Recipe: Add an item to the end of the list
my_inventory.append("Armor")

# Recipe: Access a specific item (0 is the first item)
print(my_inventory[0])


1C. Dictionary (Key/Value Collection)

(Stores data in pairs; accessed by a custom "key" name.)

# Recipe: Create a dictionary
player_stats = {
    "name": "Chris",
    "level": 5,
    "health": 100
}

# Recipe: Access a value using its key
print(player_stats["name"])

# Recipe: Change a value
player_stats["health"] = 90


2. CONTROL FLOW RECIPES (Decisions & Repetition)

2A. Making a Decision (The IF/ELIF/ELSE Structure)

(Runs different blocks of code based on a condition.)

user_input = 15

# Recipe: Check one condition, then check a second, then default.
if user_input > 20:
    print("Too high!")
elif user_input == 15:
    print("Perfect!")
else:
    print("Too low.")


2B. Repeating a Task (The FOR Loop)

(Runs a block of code a specific number of times or for every item in a list.)

# Recipe 1: Repeat 5 times
for i in range(5):
    print(f"Loop count: {i}")

# Recipe 2: Repeat for every item in a list
inventory = ["Potion", "Key", "Map"]
for item in inventory:
    print(f"Checking item: {item}")


2C. Looping Until a Condition is Met (The WHILE Loop)

(Runs a block of code continuously until the condition becomes False.)

health = 10

# Recipe: Loop while a condition is True
while health > 0:
    print(f"Health remaining: {health}")
    health -= 1 # MUST update the variable to avoid an infinite loop!

print("Game over.")


3. CODE REUSABILITY RECIPES (Functions)

3A. Defining a Basic Function

(A block of reusable code that performs a specific action.)

# Recipe: Define a function that takes no input (arguments)
def greet_user():
    print("Welcome back!")

# How to call the function:
greet_user()


3B. Function with Input and Output

(A function that accepts data and returns a result.)

# Recipe: Define a function that takes two numbers and returns their sum
def calculate_sum(num1, num2):
    result = num1 + num2
    return result

# How to call and store the result:
total = calculate_sum(10, 5)
print(total) # Output: 15


4. INPUT/OUTPUT & EXTERNAL CODE

4A. Getting User Input

(Pauses the program and waits for the user to type something.)

# Recipe: Get text input from the user
user_response = input("What is your name? ")
print(f"Hello, {user_response}")

# NOTE: Input is ALWAYS a String (text). Use int() to convert to a number!
age = int(input("How old are you? "))


4B. Using External Code (Modules)

(Allows you to use powerful, pre-written code, like your Python projects.)

# Recipe: Import an external module (e.g., the 'random' module)
import random

# Recipe: Use a function from that module
dice_roll = random.randint(1, 6)
print(f"Rolled a {dice_roll}")
