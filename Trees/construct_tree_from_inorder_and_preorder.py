# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ======= Solution 1 =========== #
# To dive into this 
# Preorder Traversal means that the root node is first followed by all the nodes from the left subtree of root and then followed by all the nodes from the right subtree
# Inorder Traversal means that its all the left subtree nodes then the root node and then all the right subtree nodes
# Thus first we can find the root node as the preorder has the root node as the first node
# And then we can grab the midpoint in the inorder list
# Since we have the midpoint for inorder that means anything before the root node is part of the left subtree
# And anything after is part of the right subtree
#
# Since the midpoint in inorder determines the number of nodes for the left / right subtrees
# We can then determine in the preorder array what nodes belong to the left / right subtrees as well 
# We do this based on the index bounds we setup
# And then that allows to recurse deeper with our new preorder / inorder lists to keep adding nodes
# 
# Doing an example:
# preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# ==== First iteration ===
# We take the preorder array and get the first node 
# Our tree is now 
#      3
#    /  \
#  None None
#
# We the can grab our midpoint which is going to be 1 here => We see that theres only one node on the left tree as well
# Now we wnat to assign the left / right subtrees for follow up recursions
# On our left subtree we can check our preorder and grab all the nodes based on the index
# Hence our preorder is [9]
# and our inorder is just the left of the root so its also just [9]
# For the right we can repeat and then it leaves [20, 15, 7] and [15, 20, 7] respectively
# And continue till we place all the nodes
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root

# ======= Solution 2 =========== #
# This solution is similar in idea
# Instead of using bounds for our preorder since we know that the root is first we can pop and add it 
# And then match the inorder list
# It means we dont have to keep upkeep on the preorder arrays as we will just deal with each node eventually
# As they all will be rootnodes
# Allows for a bit of a cleaner solution
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
    if not preorder or not inorder:
        return None
    
    
    mid = inorder.index(preorder[0])
    root = TreeNode(preorder.pop(0))
    
    root.left = self.buildTree(preorder, inorder[:mid])
    root.right = self.buildTree(preorder, inorder[mid + 1:])

    return root