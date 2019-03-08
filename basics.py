#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:39:44 2019

@author: nmalango
"""
#printing out something to the screen

print("Welcome to the basics of python programming language")

#how to get an input from the user

name = input("Enter your name here: ")
print("Your name is :", name)

#To get a number from the user input we use the eval fuction

number = eval(input("Enter a number :"))
print("The square of the numbeer you have entered is : ",number*number)

#variables
num1 = 8
num2 = 14

print("The sum of the two numbers is : ",num1+num2)

#printing 2 statemets in a single line
print("Noordeen",end=' ')
print("Malango")