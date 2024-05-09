from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        def dfs(node, path, paths):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:  # Leaf node
                paths.append(path[:])  # Append a copy of the current path
            else:
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)
            path.pop()  # Backtrack

        if not root:
            return []
        
        paths = []
        dfs(root, [], paths)
        return paths
