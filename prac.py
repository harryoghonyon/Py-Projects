import re


def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 'Error: Division by zero'
        else:
            return num1 / num2
    else:
        return 'Invalid operator'


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")


result = calculator(num1, num2, operator)


def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print(f"The result of {num1} {operator} {num2} is: {result}")


def calculator(num1, num2, operator):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': "Error: Division by zero" if num2 == 0 else num1 / num2
    }
    return operations.get(operator, 'Invalid operator')


# Input: Two numbers and an operator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Calculate the result
result = calculator(num1, num2, operator)

# Print the result
print(f"The result of {num1} {operator} {num2} is: {result}")

# end

# Temperature Code


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def convert_temperature(temp, scale):
    if scale.lower() == 'c':
        return celsius_to_fahrenheit(temp)
    elif scale.lower() == 'f':
        return fahrenheit_to_celsius(temp)
    else:
        return 'Invalid scale. Use "C" for Celsius or "F" for Fahrenheit.'


temperature = float(input("Enter the temperature: "))
scale = input("Is the temperature in celsius or Fahrenheit? (C/F): ")

converted_temp = convert_temperature(temperature, scale)

if scale.lower() == 'c':
    print(f"{temperature}°C is {converted_temp:.2f}°F")
elif scale.lower() == 'f':
    print(f"{temperature}°F is {converted_temp:.2f}°C")
else:
    print(converted_temp)

# End

# FizzBuzz Code


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()

# End

# password strenght checker


def check_password(password):
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters long."

    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."

    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special letter."

    return "Password is strong!"


password = input("Enter your password: ")
result = check_password(password)
print(result)

# end

# calculate the total price of items in a shopping cart

shopping_cart = [
    {"name": "Apple", "price": 0.50, "quantity": 4},
    {"name": "Banana", "price": 0.30, "quantity": 6},
    {"name": "Milk", "price": 1.20, "quantity": 1},
]


def calculate_total(cart):
    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
    return total


total_cost = calculate_total(shopping_cart)
print(f"Total cost: ${total_cost:.2f}")

# end

# calculate the avaerage grade of each student

grades = {
    "Alice": [85, 90, 78],
    "Bob": [75, 88, 82],
    "Charlie": [92, 95, 91],
}


def calculate_average(grades_list):
    total = sum(grades_list)
    return total / len(grades_list)


def generate_report(grades_dict):
    for student, grades_list in grades_dict.items():
        average_grade = calculate_average(grades_list)
        print(f"{student}'s average grade: {average_grade:.2f}")


generate_report(grades)

# end

# inventory management

inventory = [
    {"item": "Laptop", "stock": 10},
    {"item": "Mouse", "stock": 50},
    {"item": "Keyboard", "stock": 20}
]


def update_stock(inventory, sales):
    for sale in sales:
        for item in inventory:
            if item["item"] == sale["item"]:
                item["stock"] -= sale["quantity"]
                break


sales = [
    {"item": "Laptop", "quantity": 2},
    {"item": "Mouse", "quantity": 5},
    {"item": "Keyboard", "quantity": 1}
]

update_stock(inventory, sales)

for item in inventory:
    print(f"Item: {item['item']}, Stock: {item['stock']}")

# end

# Contact Management System

contacts = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
    "Bob": {"phone": "987-654-3210", "email": "bob@example.com"}
}


def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}


def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found")


def search_contact(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"


add_contact(contacts, "Charlie", "555-555-5555", "charlie@example.com")

remove_contact(contacts, "Alice")

result = search_contact(contacts, "Bob")
print(result)

for name, info in contacts.items():
    print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
