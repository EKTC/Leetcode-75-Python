# ===== Solution 1 ====== #
# Both solutions are very similar where we first find the node that matches to the root of the subtree
# Once we find that we start comparing the nodes to see if they are equal till we dont find a matching pair or exhaust the subtree / tree
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

    def subtree_check(s, t):
        # If both have valid nodes we can check if they are equal and also their left and right subtrees
        # Will return True if they are equal exactly
        if s and t:
            return s.val == t.val and subtree_check(s.left, t.left) and subtree_check(s.right, t.right)
        
        # Our return is `s is t` as it compares the trees even if they are None 
        # Hence its a similar comparison to `s == t` but they cant compare None / Null
        return s is t

    # Checks if we even have a tree to explore
    if not s:
        return False
    # We put this here to check each iteration
    elif subtree_check(s, t):
        return True
    
    # This helps explore the tree recursively trying to find the node with a same value as the subtree root
    # Note: We have an `or` condition for our recursion as the nodes could be None / Null so we can just ignore it :D
    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# ===== Solution 2 ====== #
# This solution just has a more readable function of DFS to show how we are traversing the tree
# The conditions are the same as they help us check the trees recursively
def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def check_subtree(s, t):
        if s and t:
            return s.val == t.val and check_subtree(s.left, t.left) and check_subtree(s.right, t.right)
        return s is t
            
    def dfs(s, t):
        if not s:
            return False
        elif check_subtree(s, t):
            return True
        
        return dfs(s.left, t) or dfs(s.right, t)

    return dfs(s, t)