# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        
        #==================== BFS ====================#
        # Ideology is different as we have an array / list to 
        # Track what nodes we need to check
        if root is None:
            level = []
        else:
            level = [root]
            
        depth = 0
        
        # Loops till there are no nodes left with each traversal being another depth added
        while level:
            depth += 1
            queue = []
            
            # This then checks each node and adds its left and right
            # If possible 
            for stage in level:
                if stage.left:
                    queue.append(stage.left)
                if stage.right:
                    queue.append(stage.right)
            level = queue
        return depth

        #==================== Revursive DFS ====================#
        
        # Checks if there is a tree
        if root is None:
            return 0
        
        # Else recursively traverse the tree and adding 1 whilst choosing
        # the side that is the largest for max depth calculation
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
