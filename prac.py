# import re


# def calculator(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             return 'Error: Division by zero'
#         else:
#             return num1 / num2
#     else:
#         return 'Invalid operator'


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter an operator (+, -, *, /): ")


# result = calculator(num1, num2, operator)


# def calculator(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             return "Error: Division by zero"
#         else:
#             return num1 / num2
#     else:
#         return "Invalid operator"


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter an operator (+, -, *, /): ")

# result = calculator(num1, num2, operator)
# print(f"The result of {num1} {operator} {num2} is: {result}")


# def calculator(num1, num2, operator):
#     operations = {
#         '+': num1 + num2,
#         '-': num1 - num2,
#         '*': num1 * num2,
#         '/': "Error: Division by zero" if num2 == 0 else num1 / num2
#     }
#     return operations.get(operator, 'Invalid operator')


# # Input: Two numbers and an operator
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter an operator (+, -, *, /): ")

# # Calculate the result
# result = calculator(num1, num2, operator)

# # Print the result
# print(f"The result of {num1} {operator} {num2} is: {result}")

# # end

# # Temperature Code


# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32


# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9


# def convert_temperature(temp, scale):
#     if scale.lower() == 'c':
#         return celsius_to_fahrenheit(temp)
#     elif scale.lower() == 'f':
#         return fahrenheit_to_celsius(temp)
#     else:
#         return 'Invalid scale. Use "C" for Celsius or "F" for Fahrenheit.'


# temperature = float(input("Enter the temperature: "))
# scale = input("Is the temperature in celsius or Fahrenheit? (C/F): ")

# converted_temp = convert_temperature(temperature, scale)

# if scale.lower() == 'c':
#     print(f"{temperature}°C is {converted_temp:.2f}°F")
# elif scale.lower() == 'f':
#     print(f"{temperature}°F is {converted_temp:.2f}°C")
# else:
#     print(converted_temp)

# # End

# # FizzBuzz Code


# def fizz_buzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)


# fizz_buzz()

# # End

# #  password strenght checker


# def check_password(password):
#     if len(password) < 8:
#         return "Password too short! Must be at least 8 characters long."

#     if not any(char.isdigit() for char in password):
#         return "Password must contain at least one digit."

#     if not any(char.isupper() for char in password):
#         return "Password must contain at least one uppercase letter."

#     if not any(char.islower() for char in password):
#         return "Password must contain at least one lowercase letter."

#     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         return "Password must contain at least one special letter."

#     return "Password is strong!"


# password = input("Enter your password: ")
# result = check_password(password)
# print(result)

# # end

# # calculate the total price of items in a shopping cart

# shopping_cart = [
#     {"name": "Apple", "price": 0.50, "quantity": 4},
#     {"name": "Banana", "price": 0.30, "quantity": 6},
#     {"name": "Milk", "price": 1.20, "quantity": 1},
# ]


# def calculate_total(cart):
#     total = 0
#     for item in cart:
#         item_total = item["price"] * item["quantity"]
#         total += item_total
#     return total


# total_cost = calculate_total(shopping_cart)
# print(f"Total cost: ${total_cost:.2f}")

# # end

# # calculate the avaerage grade of each student

# grades = {
#     "Alice": [85, 90, 78],
#     "Bob": [75, 88, 82],
#     "Charlie": [92, 95, 91],
# }


# def calculate_average(grades_list):
#     total = sum(grades_list)
#     return total / len(grades_list)


# def generate_report(grades_dict):
#     for student, grades_list in grades_dict.items():
#         average_grade = calculate_average(grades_list)
#         print(f"{student}'s average grade: {average_grade:.2f}")


# generate_report(grades)

# # end

# # inventory management

# inventory = [
#     {"item": "Laptop", "stock": 10},
#     {"item": "Mouse", "stock": 50},
#     {"item": "Keyboard", "stock": 20}
# ]


# def update_stock(inventory, sales):
#     for sale in sales:
#         for item in inventory:
#             if item["item"] == sale["item"]:
#                 item["stock"] -= sale["quantity"]
#                 break


# sales = [
#     {"item": "Laptop", "quantity": 2},
#     {"item": "Mouse", "quantity": 5},
#     {"item": "Keyboard", "quantity": 1}
# ]

# update_stock(inventory, sales)

# for item in inventory:
#     print(f"Item: {item['item']}, Stock: {item['stock']}")

# # end

# # # Contact Management System

# contacts = {
#     "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
#     "Bob": {"phone": "987-654-3210", "email": "bob@example.com"}
# }


# def add_contact(contacts, name, phone, email):
#     contacts[name] = {"phone": phone, "email": email}


# def remove_contact(contacts, name):
#     if name in contacts:
#         del contacts[name]
#     else:
#         print("Contact not found")


# def search_contact(contacts, name):
#     if name in contacts:
#         return contacts[name]
#     else:
#         return "Contact not found"


# add_contact(contacts, "Charlie", "555-555-5555", "charlie@example.com")

# remove_contact(contacts, "Alice")

# result = search_contact(contacts, "Bob")
# print(result)

# for name, info in contacts.items():
#     print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# # end

# # To-Do List Manager

# def add_task(to_do_list):
#     task = input("Enter the task you want to add: ").strip()
#     if task:
#         to_do_list.append({"task": task, "completed": False})
#     else:
#         raise ValueError("Task cannot be empty.")


# def complete_task(to_do_list):
#     try:
#         task_number = int(
#             input("Enter the task number to mark as completed: "))
#         if 1 <= task_number <= len(to_do_list):
#             to_do_list[task_number - 1]["completed"] = True
#         else:
#             raise IndexError("Invalid task number.")
#     except ValueError:
#         print("Please enter a valid number.")
#     except IndexError as ie:
#         print(f"Error: {ie}")


# def view_tasks(to_do_list):
#     if not to_do_list:
#         print("Your to-do list is empty.")
#     else:
#         for i, task in enumerate(to_do_list, 1):
#             status = "Completed" if task["completed"] else "Not Completed"
#             print(f"{i}. {task['task']} - {status}")


# to_do_list = []

# while True:
#     print("\nTo-Do List Manager")
#     print("1. Add Task")
#     print("2. Complete Task")
#     print("3. View Tasks")
#     print("4. Exit")

#     try:
#         choice = int(input("Choose an option (1-4): "))

#         if choice == 1:
#             add_task(to_do_list)
#         elif choice == 2:
#             complete_task(to_do_list)
#         elif choice == 3:
#             view_tasks(to_do_list)
#         elif choice == 4:
#             print("Goodbye")
#             break
#         else:
#             raise ValueError("Please choose a valid option (1-4).")

#     except ValueError as ve:
#         print(f"Input Error: {ve}")

# End

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

#  file reading
# import sys


# def read_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"Error: {file_name} not found.")
#         sys.exit(1)


# if len(sys.argv) != 2:
#     print("Usage: python script.py <filename>")
#     sys.exit(1)

# file_name = sys.argv[1]
# content = read_file(file_name)
# print(content)

# end


# practicing and working with libaries

# import numpy as np

# first_numbers = np.array([1, 2, 3, 4, 5])

# second_numbers = np.array([6, 7, 8, 9, 10])

# total_showings = first_numbers + (10 / second_numbers)

# rounded_figures = np.round(total_showings, 2)

# for num in rounded_figures:
#     print(num)


# import pandas as pd

# data = {
#     "Name": ['Alice', 'Benson', 'Cordelia', 'Damson'],
#     "Age": [20, 25, 30, 45]
# }

# df = pd.DataFrame(data)

# ages = df["Age"]

# filtered_df = df[df["Age"] > 25]

# print("DataFrame:\n", df)
# print("\nAges:\n", ages)
# print("\nFiltered DataFrame:\n", filtered_df)

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)

# plt.title('Simple Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.show()

# import requests

# url = 'https://jsonplaceholder.typicode.com/posts/1'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print("User ID:", data['userId'])
#     print("Body:", data['body'])
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

# import requests
# import json

# url = 'https://jsonplaceholder.typicode.com/posts/1'

# response = requests.get(url)

# data = response.json()

# with open('response.json', 'w') as file:
#     json.dump(data, file, indent=4)
