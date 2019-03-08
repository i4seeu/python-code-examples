#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:00:09 2019

@author: nmalango
"""

from random import randint
lottery_number = randint(1,10)
guess = eval(input("Guess the lottery number: "))

if lottery_number == guess:
    print("Correct")
else:
    print("Incorrent , the correct number is : ", lottery_number)

#multiple conditional statemets

grade = eval(input("Enter your grade here : "))
if grade >=90:
    print("A")
elif grade >=70:
    print("B")
elif grade >= 50:
    print("C")
else:
    print("F")