#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Sunghoon Lee

# Question: We want to invest in a company in NY Stock market next year. Its stock price changes seasonally 
# during the year. We have the daily stock price of this company for the last year (365 daily prices). 
# Some days it increases, some day it decreases. We want to invest in it and maximize our profit. 
# What was the best time to buy (e.g Apr15) and sell (e.g. Sep15) this stock last year? We can buy and sell only once 
# in a year, so don't want to pay too much taxes. 

# In order to make it easier for you, just use the daily price of 9 days at below, instead of 365 days. 
# And also just print out the max profit that we can make. No need to print out start & finish index (day).

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array

# (Hint: When you read it you should be able to figure it out to find daily differences (negative/positive values) 
# and apply Maximum Subarray Sum algorithm.)

# Please download the below Python code templates and write Maximum Subarray Sum algorithm in 3 different ways: 
# O(n^2), O(n logn), O(n).

# WRITE YOUR CODE HERE
def change_in_arr(A):
    delta_arr = []
    for i in range(len(A)-1):
        change = A[i+1] - A[i]
        delta_arr.append(change)
    return delta_arr

def kadanesAlgorithm(arr):
    local_max = arr[0]
    global_max = arr[0]
    
    for i in range(1, len(arr)):
        local_max = max(arr[i], local_max + arr[i])
        if local_max > global_max:
            global_max = local_max
    
    return global_max

A = change_in_arr(arr)
ans = kadanesAlgorithm(A)
print(ans)                         # printing the max possible subarray sum, as ans