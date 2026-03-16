"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return 

        oldToNew = {}
        nodesToVisit = {node}

        while nodesToVisit:
            curNode = nodesToVisit.pop()

            if curNode not in oldToNew: 
                oldToNew[curNode] = Node(curNode.val)

            newNode = oldToNew[curNode]

            for neigh in curNode.neighbors:
                if neigh not in oldToNew: 
                    oldToNew[neigh] = Node(neigh.val)
                    nodesToVisit.add(neigh)

                newNode.neighbors.append(oldToNew[neigh])
        

        return oldToNew[node]
