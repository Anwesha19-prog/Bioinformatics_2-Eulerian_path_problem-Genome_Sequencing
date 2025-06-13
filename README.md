# Bioinformatics_2-Eulerian_path_problem-Genome_Sequencing

**README: Eulerian Path Problem Solver (Python)**

**Problem Overview**

An Eulerian path in a directed graph is a path that visits every edge exactly once but does not need to return to the starting node. For a graph to contain an Eulerian path, it must satisfy the following conditions:

At most one node has (out-degree) = (in-degree + 1) (start node).

At most one node has (in-degree) = (out-degree + 1) (end node).

All other nodes must have equal in-degree and out-degree.

The graph must be weakly connected (you can reach all nodes ignoring direction).

**Why Is This Problem Important?**

Eulerian paths are used in:

DNA sequencing (reconstructing sequences from reads)

Data routing in networks

Reconstruction of ordered sequences from fragmented data

In bioinformatics, Eulerian paths help reconstruct genomes when the complete circular structure isn't available, unlike in the Eulerian cycle problem.

**Problem Statement**

You are given the adjacency list of a directed graph that has an Eulerian path. Your task is to return the sequence of nodes visited in an Eulerian path.

**Input Format**

A text file (input.txt) with each line of the format:

node: neighbor1 neighbor2 ...

**Example:**

0: 2
1: 3
2: 1
3: 0 4
6: 3 7
7: 8
8: 9
9: 6

**Output Format**

A text file (output.txt) containing a space-separated list of nodes in a valid Eulerian path.

Example:

6 7 8 9 6 3 0 2 1 3 4

**How to Use**

**Requirements**

Python 3.x

**Steps**

Save your adjacency list in input.txt.

Run the script:

python eulerian_path.py

View the output in output.txt.
 
**How It Works**

This script uses a modified Hierholzer's Algorithm:

Identifies the start node (where out-degree = in-degree + 1).

Performs DFS traversal to build the path using a stack.

Reverses the final path to present the correct order.

All edges are used exactly once, and the path starts and ends at valid points as per the Eulerian path definition.

**Project Structure**

BioinformaticsII_solving_eulers_theorem.py       # Python script /n
dataset.txt              # Input adjacency list /n
output.txt             # Eulerian path result /n
README.md              # This file 

**Sample Run**
**Input:**

6: 3 7
7: 8
8: 9
9: 6
3: 0 4
0: 2
2: 1
1: 3

**Output:**

6 7 8 9 6 3 0 2 1 3 4

**Notes**

If the graph doesn't meet the Eulerian path conditions, the output may be incomplete or invalid.

Only one valid path is returned (if multiple exist).

