#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:30:59 2019

@author: nmalango
"""

current_number = 1
prev_number = 0
second_prev = 1
fibonacci_number = eval(input("How many numbers in fibonacci do you want to print? : "))
for i in range(fibonacci_number):
    current_number = prev_number + second_prev
    second_prev = prev_number
    prev_number = current_number
    print(current_number, end=" ")