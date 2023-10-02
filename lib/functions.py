#!/usr/bin/env python3

def greet_programmer():
    '''This function should print "Hello, programmer!"'''
    print("Hello, programmer!")
   

def greet(name):
    '''This function should print "Hello, {name}!"'''
    print(f"Hello, {name}!")
    

def greet_with_default(name="programmer"):
    '''This function should print "Hello, {name}!" with a default of "programmer".'''
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    '''This function should calculate the sum of num1 and num2.'''
    return num1 + num2
    pass

def halve(number):
    '''This function should halve the input number.'''
    return number / 2
    pass
