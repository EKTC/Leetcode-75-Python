# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This solution is the more simple case being O(n^2)
# It aims to do a DFS to get the height of that subtree and then compare it to the left and right to ensure it meets the conditions
# It then repeats this for every node in the subtree hence recurses on itself with the main function
def isBalancedV1(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return 0
        return 1 + max(dfs(root.left), dfs(root.right))
    
    if not root:
        return True
    balanced = abs(dfs(root.left) - dfs(root.right)) <= 1
    return balanced and self.isBalanced(root.left) and self.isBalanced(root.right)

# The more efficient solution 
# It uses a boolean to record whether at this pt the node is balanced and the height of that subtree
def isBalancedV2(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if root is None:
            return [True, 0]
        
        left, right = dfs(root.left), dfs(root.right)
        
        # We have the condition to check whether its balanced such that we check
        # 1) Hey are the left and right subtrees being looked at balanced?
        # 2) We then check if the height of those subtrees are gonna be less than 1 to fit the condition
        balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

        # We then return this as out value to be used for other recursions 
        # Taking the max of the tree height 
        return [balanced, max(left[1], right[1]) + 1]
    
    return dfs(root)[0]