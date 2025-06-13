# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 14:07:13 2025

@author: DELL
"""

from collections import defaultdict, deque

def parse_input(file_name):
    graph = defaultdict(deque)
    with open(file_name, 'r') as f:
        for line in f:
            node, edges = line.strip().split(": ")
            graph[int(node)] = deque(map(int, edges.split()))
    return graph

def find_start_node(graph):
    in_deg = defaultdict(int)
    out_deg = defaultdict(int)

    nodes = set(graph.keys())
    for u in graph:
        out_deg[u] += len(graph[u])
        for v in graph[u]:
            in_deg[v] += 1
            nodes.add(v)

    start = None
    for node in nodes:
        out_d = out_deg[node]
        in_d = in_deg[node]
        if out_d - in_d == 1:
            start = node  # this is the only valid start node
        elif in_d - out_d > 1 or out_d - in_d > 1:
            raise Exception("Graph does not have an Eulerian path.")
    return start or next(iter(graph))  # fallback to any node if graph is Eulerian cycle

def find_eulerian_path(graph):
    graph_copy = {u: deque(v) for u, v in graph.items()}
    path = []
    stack = [find_start_node(graph)]

    while stack:
        current = stack[-1]
        if graph_copy.get(current):
            next_node = graph_copy[current].popleft()
            stack.append(next_node)
        else:
            path.append(stack.pop())
    return path[::-1]

if __name__ == "__main__":
    # 🔽 Change this to your input file name
    input_file = "dataset_30187_6.txt"

    # 🔽 Change this to your desired output file name
    output_file = "output.txt"

    graph = parse_input(input_file)
    path = find_eulerian_path(graph)

    with open(output_file, 'w') as f:
        f.write(" ".join(map(str, path)))

    print("Eulerian path written to", output_file)
