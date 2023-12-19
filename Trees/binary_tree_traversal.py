# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Checks if the tree is there
        if root is None:
            return []
        
        res = [] # stores all the arrays 
        queue = [root] # Start off our queue with the root

        # Loops till we traverse the entire tree
        while queue:
            temp = [] # Temp will hold the new array of nodes to traverse through
            new_level = [] # this variable will hold all the nodes in the current level to be appended to
            
            for node in queue:
                # If the node exists append the left first and then the right nodes
                # And then add the value to the level array
                if node:
                    temp.append(node.left)
                    temp.append(node.right)
                
                    new_level.append(node.val)
            
            # If its not empty append it
            # When it is empty we know that the tree has been traversed
            if new_level:
                res.append(new_level)
            queue = temp

        return res