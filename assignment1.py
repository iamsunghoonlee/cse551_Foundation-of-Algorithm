#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sunghoon Lee


# ''' --- Input values --- '''

department = [ [2, 1, 4, 5, 3], # Department preference list
[4, 2, 1, 3, 5],
[2, 5, 3, 4, 1],
[1, 4, 3, 2, 5],
[2, 4, 1, 5, 3] ]

employee = [ [5, 1, 2, 4, 3], # Employee preference list
[3, 2, 4, 1, 5],
[2, 3, 4, 5, 1],
[1, 5, 4, 3, 2],
[4, 2, 5, 3, 1] ]

N = 5 # Number of department & employee

# WRITE YOUR CODE HERE

from collections import deque

def inverse_order(preference):
    inverse_preference = []
    for pref in preference:
        inverse = [0]*len(pref)
        for i, p in enumerate(pref):
            inverse[p-1] = i
        inverse_preference.append(inverse)
    return inverse_preference


def stable_matching(department, employee, N):
    employee_rev = inverse_order(employee)    
    match_dep = [-1 for i in range(N)] # -1: no match, 0 ~ N-1: match 
    match_emp = [-1 for i in range(N)] # -1: no match, 0 ~ N-1: match
    free_dep = deque(range(N)) # index of free departments
    next_idx = [0]*N # tracking progress

    while free_dep: # while some "Dep" is free
        dep = free_dep[0] # "Selected Dep" (remove 1st from "free_dep")
        idx = next_idx[dep]
        assert idx < N

        candidate_emp = department[dep][idx] - 1 # "1st Emp" on "Selected Dep" list
        next_idx[dep] += 1
        current_dep = match_emp[candidate_emp]


        # case 1 : "Emp" is free
        if current_dep == -1:
            match_dep[dep] = candidate_emp # assign "New Dep"
            match_emp[candidate_emp] = dep
            free_dep.popleft()

        # case 2: "Emp" is not free & prefers "New Dep" to "Current Dep"    
        elif employee_rev[candidate_emp][dep] < employee_rev[candidate_emp][current_dep]:
            match_dep[current_dep] = -1
            match_emp[candidate_emp] = dep
            match_dep[dep] = candidate_emp # assign "New Dep"

            free_dep.appendleft(current_dep) # "Current Dep" goes to 1st of free_dep
            free_dep.popleft()
            
        # case 3: "Emp" is not free & prefers "Current Dep" to "New Dep"
        else: # "Emp" rejects "Dep" 
            continue # "Dep" goes back to free_dep

    return match_dep

print(stable_matching(department, employee, 5))


''' --- Visualizing the result, Printing the output --- '''

Names = [ ['HR', 'CRM', 'Admin', 'Research', 'Development'], # Initialize the mapping of names
          ['Adam', 'Bob', 'Clare', 'Diane', 'Emily'] ]

print('Result is:-')
match = stable_matching(department, employee, 5)

for i in range(N):
    print(Names[0][i], ":", Names[1][match[i]]) # Map the result to the names