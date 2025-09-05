# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: write your name here
# Function to perform Kruskal's algorithm for single link k-clustering

class UnionFind:
    def __init__(self, V): self.parent = [i for i in range(V)]; self.rank = [0 for i in range(V)] 
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, x, y):
        s1, s2 = self.find(x), self.find(y)
        if s1 != s2:
            if self.rank[s1] > self.rank[s2]: self.parent[s2] = s1
            elif self.rank[s1] < self.rank[s2]: self.parent[s1] = s2
            else: self.parent[s2] = s1; self.rank[s1] += 1


def greedy_clustering_kruskal(distance_matrix, k):
# WRITE YOUR CODE HERE
    # 1. distanc_matrix to edges (undirected graph)
    edges = []
    for i, dis_list in enumerate(distance_matrix):
        for j, dis in enumerate(dis_list):
            if i > j:
                edges.append([i, j, dis])  
    # 2. Sort Edges
    sorted_edges = sorted(edges, key=lambda edges: edges[2])
    
    # 3. merge edges till "cluster_count == k"
    uf = UnionFind(len(distance_matrix))
    cluster_count = len(distance_matrix)
    
    for edge in sorted_edges:
        if cluster_count == k:
            break
        n1, n2, w = edge
        
        if uf.find(n1) != uf.find(n2):
            uf.union(n1, n2)
            cluster_count -= 1
    
    clusters = {}
    for i in range(len(distance_matrix)):
        if uf.find(i) not in clusters.keys():
            clusters[uf.find(i)] = []
        clusters[uf.find(i)].append(i)
    
    # return sorted_edges    
    # return clusters
    return list(clusters.values()) # Return the clusters
    

# Use this input
distance_matrix = [
[0, 38, 17, 28, 88, 59, 13],
[38, 0, 52, 49, 83, 91, 59],
[17, 52, 0, 46, 34, 77, 80],
[28, 49, 46, 0, 5, 53, 62],
[88, 83, 34, 5, 0, 43, 33],
[59, 91, 77, 53, 43, 0, 27],
[13, 59, 80, 62, 33, 27, 0]
]


# Set k=2 for number of clusters
k = 2
clusters = greedy_clustering_kruskal(distance_matrix, k)
print(clusters)

# Print the resulting clusters
print("Resulting Clusters:", clusters)