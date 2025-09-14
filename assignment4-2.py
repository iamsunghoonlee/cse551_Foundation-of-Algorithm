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

from sys import maxsize                              # import max int for initialization

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array
ans = -maxsize - 1                             # initialize ans variable to -intmax

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


def find_max_cross_subarray(A, low, mid, high):
    left_sum = -maxsize - 1
    right_sum = -maxsize - 1
    
    l_sum = 0
    r_sum = 0
    # if low == high:
    #     return (low, high, A[low])
    
    # left portion
    for i in range(mid, low - 1, -1):
        l_sum = l_sum + A[i]
        if l_sum > left_sum:
            left_sum = l_sum
            max_left = i
    
    # right portion
    for j in range(mid+1, high+1):
        r_sum = r_sum + A[j]
        if r_sum > right_sum:
            right_sum = r_sum
            max_right = j
           
    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A, low, high):
    if low==high:
        return (low, high, A[low])
    else:
        mid = (low+high)//2
        (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(A, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_cross_subarray(A, low, mid, high)
        
        if left_sum >= right_sum and left_sum>= cross_sum:
            return (left_low, left_high, left_sum)
        
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        
        else: # cross_sum >= left_sum and cross_sum >= right_sum
            return (cross_low, cross_high, cross_sum) 


def DivideAndConquer(arr, ans):
    A = change_in_arr(arr)
    # print(A)
    high = len(A)-1
    low, high, sum = find_max_subarray(A, 0, high)
    return low, high, sum

low, high, ans1 = DivideAndConquer(arr, ans)
print(low, high)