"""Provides a scripting component.
Remember to change type hint (Python only)
    Inputs:
        n: Number of steps (int)
        p: (Randomly Walking) Point (int list)
    Output:
        l: Point List (list of int list)"""

__author__ = "Zoe De Simone after Bill Xu's 2D implementation for DEA3306"
__version__ = "2020.02.15"

import rhinoscriptsyntax as rs
import random as rand
import ghpythonlib.treehelpers as th

# Define our Step Set (List here):
steplist = ((0,0,1), (0,1,0), (1,0,0), (0,0,-1), (0,-1,0), (-1,0,0))

# Define our Point List l
l = []

# Start from a given point p (e.g., (0,0,0))
# We have p as input value

# Add p to point list l
l.append(p)

# Repeat steps below for given times n
for i in range(n):

    # Randomly selected a step s from step set
    # Generate a rand int from 0 to 5
    r = rand.randint(0,len(steplist)-1)
    # Pick r-th element from our steplist
    step = steplist[r]

    # Move and Update P according to s
    p = [p[0]+step[0], p[1]+step[1],p[2]+step[2]]

    # Add new p to l
    l.append(p)

#Convert Python tree to GH tree (Python only)
l=th.list_to_tree(l)
