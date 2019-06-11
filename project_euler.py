#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:59:56 2018

@author: loukj.smalbil
"""

import numpy as np

#Returns the sum of all numbers that are a multiplication of 3 or 5
def mod_sum_funct():
    sumVar = []
    for i in range(0, 1000):
        if (i % 3 == 0):
            sumVar.append(i)
        if (i % 5 == 0):
            sumVar.append(i)
    np.array(sumVar)
    sumVar = np.unique(sumVar)
    return(sum(sumVar))
     
#Returns the sum of the even fibonacci numbers below a certain value
def fibonacci():
    length = int(input("Enter the highest number here: "))
    fibo_list = [1,2]
    counter = 0
    even_fibo_list = []
    
    while (counter < length):
        if (fibo_list[-1] > 4000000):
            fibo_list.remove(fibo_list[-1])
            break
        new_value = fibo_list[counter] + fibo_list[counter + 1]
        fibo_list.append(new_value)
        counter = counter + 1
    
    for number in fibo_list:
        if (number % 2 == 0):
            even_fibo_list.append(number)
    
    return(sum(even_fibo_list)) 

#Returns the larges prime factors of a given number
def large_prime():
    #number = int(input("Enter number here:" ))
    number = 13195
    list_of_factors = []
    list_of_primes = []
    
    for factor in range(1, number):
        if (number % factor == 0):
            list_of_factors.append(factor)
    
    for prime in list_of_factors:
        list_of_primes.append(prime)
        
    
            
    
    
    
    
    
    
    
    
