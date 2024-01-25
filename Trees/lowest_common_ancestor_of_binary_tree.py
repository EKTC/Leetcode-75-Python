# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# ======== Solution 1 ======== #
# The idea is that we check the current node value
# And traverse based on some main conditions
# 1) If both `p` and `q` are larger than the node value that means its all on the right side of the node
# 2) If both `p` and `q` are smaller than the node value that means its all on the left side of the node
# 3) If one is smaller while the other is larger that means that they are split across the sides of the node which means the LCA is that current node so we just return
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    temp_node = root 

    while temp_node:
        if temp_node.val > p.val and temp_node.val > q.val:
            temp_node = temp_node.left
        elif temp_node.val < p.val and temp_node.val < q.val:
            temp_node = temp_node.right
        else:
            return temp_node