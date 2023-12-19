# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res # allows us to use it as a global variable
            # If its a null value
            if not node:
                return 0
            
            # Grab the max of each path recursively
            left = dfs(node.left)
            right = dfs(node.right)

            # Then check if its worth adding the path or not for the value
            left_path = max(left, 0)
            right_path = max(right, 0)

            # Check if the current node and its split is greater than the current max
            # This is done as there are some cases where its true!
            res = max(res, node.val + left_path + right_path)

            # Makes the subtree the greatest value possible with the splits
            return node.val + max(left_path, right_path)
        
        dfs(root)
        return res