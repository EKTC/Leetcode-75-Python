# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # ============= DFS solution ============== # 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # adds the first node to the stack
        stack = [root]
        while stack:
            # Pops the node and then checks if its null or not
            current = stack.pop()
            if current:

                # Here we swap the nodes to invert it 
                temp = current.right
                current.right = current.left
                current.left = temp

                # Now add the next nodes onto the stack
                stack.append(current.left)
                stack.append(current.right)
        return root
    
    # ============= BFS solution ============== # 
    def invertTreeV2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTreeV2(root.left)
        self.invertTreeV2(root.right)
        
        return root