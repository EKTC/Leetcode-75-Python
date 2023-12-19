# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if p and q are both empty
        if p is None and q is None:
            return True
        # Check if either p or q is empty and thus return
        elif p is None or q is None:
            return False
        # Check two things
        # 1) If the values are the same continue the node checking
        # 2) If they are not equal that means that its failed and we can return false
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False