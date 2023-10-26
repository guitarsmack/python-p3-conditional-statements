#!/usr/bin/env python3

import ipdb

def admin_login(username, password):
    match_user = username == "admin" or username == "ADMIN"
    match_password = password == "12345"
    # ipdb.set_trace()
    if match_password and match_user:
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature and temperature < 65:
        return "It's a little chilly out there!"
    elif 85 < temperature:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    three = num % 3 == 0
    five = num % 5 == 0
    # ipdb.set_trace()
    if three and five:
        return "FizzBuzz"
    elif three and not five:
        return "Fizz"
    elif five and not three:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None