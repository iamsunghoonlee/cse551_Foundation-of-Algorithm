#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Sunghoon Lee

"""
Problem: We have 5 software engineers: s1, s2, s3, s4, s5 and 5 projects: p1, p2, p3, p4, p5. 
You can see the skills match between the software engineers and the projects. 
Which means that engineer has skills (Java, C++, Python etc) to work on those projects.
- Each engineer can work on 0 or 1 project. (Exception: s3 can work up to 2 projects)
- Each project receives 0 or 1 engineer. (Exception: p2 can receive up to 2 engineers)
{s1} - {p1, p2}
{s2} - {p2}
{s3} - {p1, p3, p4}
{s4} - {p2, p4}
{s5} - {p2, p5}
Find the maximum number of assignments between them in O(nm) time, 
where n is the number of nodes (engineers + projects) and m is the links between them. 
Print both the max number and also the assignments between them.

This is a version of Bipartite Matching as we discussed in the class. 
Please download the below Python code templates and write the Ford-Fulkerson algorithm in O(nm). 
We already provided Augmenting paths with DFS for you.
"""

# Define the graph structure based on skill matches
engineers = ['s1', 's2', 's3', 's4', 's5']
projects = ['p1', 'p2', 'p3', 'p4', 'p5']
# Adjacency list: which engineers can work on which projects
adjacency_list = {
    's1': ['p1', 'p2'],
    's2': ['p2'],
    's3': ['p1', 'p3', 'p4'],
    's4': ['p2', 'p4'],
    's5': ['p2', 'p5']
}

# Special constraints
max_assignments = {
    's1': 1, 's2': 1, 's3': 2, 's4': 1, 's5': 1, # Engineers
    'p1': 1, 'p2': 2, 'p3': 1, 'p4': 1, 'p5': 1 # Projects
}

# Keep track of assignments
engineer_to_project = {} # Map of engineer -> list of projects
project_to_engineers = {} # Map of project -> list of engineers
# Initialize empty assignments
for e in engineers:
    engineer_to_project[e] = [] 
for p in projects:
    project_to_engineers[p] = []
        
def dfs(engineer, visited):
    """Depth-first search to find augmenting path"""
    # Try each project the engineer can work on
    for project in adjacency_list[engineer]:
        if project not in visited:
            visited.add(project)                                                 # to not join in same location?
            # If project can accept more engineers or we can reassign
            if (len(project_to_engineers[project]) < max_assignments[project] or # more engineers to project 
                any(dfs(e, visited) for e in project_to_engineers[project])):    # can reassign engineer to other projects
                # If the engineer can take another assignment
                if len(engineer_to_project[engineer]) < max_assignments[engineer]:
                    # Assign project to engineer
                    engineer_to_project[engineer].append(project)
                    project_to_engineers[project].append(engineer)
                    return True
                
    return False

def maximum_bipartite_matching():
    # WRITE YOUR CODE HERE
    match_count = 0
    visited = set()
    for engineer in engineers:
        project_count = 0
        while project_count < max_assignments[engineer]:
            if dfs(engineer, visited):
                match_count += 1
                project_count += 1
        visited.clear()
    return match_count



# Run the maximum bipartite matching algorithm
print("Maximum number of assignments: ")
print(maximum_bipartite_matching())
print("\nAssignments:")
print(engineer_to_project)