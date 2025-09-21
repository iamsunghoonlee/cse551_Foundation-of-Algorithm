#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sunghoon Lee

"""
Question: Given two strings (or words) w1 and w2, find the minimum number of operations 
(insert, delete, replace) to convert w1 into w2.
This is also known as Edit Distance problem. Write a Dynamic Programming with memoization. 
You need write two functions:

1-) Write recursive DP function with memoization table to find minimum number of operations.
2-) Write a function to backtrack the memoization table and print the actual operations 
(insert, delete, replace) to convert w1 into w2.
"""


w1 = "professor" #8
w2 = "confession" #9
ans = 0 # initialize ans variable to 0

# WRITE YOUR CODE HERE
def editDisMem(w1, w2, m, n, mem):
    if m == 0:
        mem[m][n] = n
        return n
    
    if n == 0:
        mem[m][n] = m
        return m
    
    if mem[m][n] != -1:
        return mem[m][n]
    
    if w1[m-1] == w2[n-1]:
        mem[m][n] = editDisMem(w1, w2, m-1, n-1, mem)
        return mem[m][n]
    
    mem[m][n] = 1 + min(
        editDisMem(w1, w2, m-1, n, mem),    # delete
        editDisMem(w1, w2, m, n-1, mem),    # insert
        editDisMem(w1, w2, m-1, n-1, mem)   # replace
    )
    return mem[m][n]


def backtrack(mem, m, n):
    op = []
    while mem[m][n] != -1:
        if mem[m][n] == 1 + mem[m][n-1]:
            n = n-1
            # print("case insert  m:", m, "n:", n)
            op.insert(0, "insert")
        elif mem[m][n] == 1 + mem[m-1][n]:
            m = m-1
            # print("case delete  m:", m, "n:", n)
            op.insert(0, "delete")
        elif mem[m][n] == 1 + mem[m-1][n-1]:
            m, n = m-1, n-1
            # print("case replace  m:", m, "n:", n)
            op.insert(0, "replace")
        elif mem[m][n] == mem[m-1][n-1]:
            m, n = m-1, n-1
            # print("case4 match  m:", m, "n:", n)
            op.insert(0, "match")
        else:
            break
    print("m:", m, "n:", n)
    return op


def runEditDis(w1, w2):
    m = len(w1)
    n = len(w2)
    mem = [[-1 for i in range(n+1)] for j in range(m+1)]
    
    op_count = editDisMem(w1, w2, m, n, mem)
    [print(m) for m in mem]
    print(backtrack(mem, m, n))
    return op_count

print(runEditDis(w1, w2))