# My first python program - Hello World
import numbers

print("Hello World")

# variable
age = 20
age = 30
price = 19.1
first_name = "Tony"
is_online = True
print(age)
print(price)
print(first_name)
print(is_online)

# input received
name = input("Enter your name: ")
print("hello "+ name)

# Type conversion
birth_year = input("Enter your birth year: ")
age = 2026  - int(birth_year)
print(age)

sell_price = 100
cost_price = input("Enter your cost price: ")
profit = sell_price  - int(float(cost_price))
print(profit)

# calulator
first_number = input("Enter your first number: ")
second_number = input("Enter your second number: ")
sum = int(first_number) + int(second_number)
print(f"the sum of two number is {sum}")