# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
For this we declare a member variable or global variable so we can get the height whilst doing the recursion
The idea is similar to other stuff we do DFS to get the height and add them together to see the path
We then return the height to use for the next traversals
With our global variable we can then check the distance and retain the max across the recursions
'''
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.dist = 0

    # This function returns the height of the subtree we are looking at
    def dfs(node):
        if not node:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        self.dist = max(self.dist, left + right)
        return max(left, right) + 1
        
    dfs(root)
    return self.dist
