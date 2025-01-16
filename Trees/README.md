Note: This section will have code based on leetcode's systems and as such does not work locally. To simulate similar ideas we would define our own tree structure :)

# 100. Same Tree

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

- Traverse both trees and compare the nodes each time to see if they equal
- Return false early if one of the pairs is not equal or true if the entire trees were traveresed

# 102. Binary Tree Level Order Traversal

Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

- Go through all the nodes in the level adding it to a new array
- When going through those nodes add its left and right nodes to the queue to continue adding the levels

# 104. Maximum Depth of Binary Tree

Link: https://leetcode.com/problems/same-tree/

- You can do a BFS solution with a queue that adds new nodes for you to remove
- A DFS solution would be something similar but with a stack instead -> honestly not intuitive to me
- Finally a recursive DFS solution that aims to just solve the subproblem on which subtree is bigger and add 1 progressively till the end

# 105. Construct Binary Tree from Preorder and Inorder Traversal

Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

- The idea is that we need to use both preorder and inorder traversal to determine the left and right subtrees of a root node
- We recursively add new root nodes and then determine its left and right subtrees
- Note 1: Preorder Traversal means that the root node is first followed by all the nodes from the left subtree of root and then followed by all the nodes from the right subtree
- Note 2: Inorder Traversal means that its all the left subtree nodes then the root node and then all the right subtree nodes
- Hence we can use these ideas to determine whats the root node and what the left / right subtrees are

# 110. Balanced Binary Tree

Link: https://leetcode.com/problems/balanced-binary-tree/description/

- The more basic solution which is `n^2` time is to do a DFS at each node comparing the heights at each time
- The more efficient solution which is `n` time is to do a **BOTTOM-UP** solution
- The idea is that we just calculate the most lowest leafs of the tree and record their height slowly building up
- The solution uses in this case 2 variables to track that to determine if its a balanced at each step and the height to reuse

# 124. Binary Tree Maximum Path Sum

Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

- We calculate the subtrees path and then add on the max to the root node
- Since we cannot split we have to check which path is the max or that neither is and the node is not worth adding

# 208. Implement Trie (Prefix Tree)

Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/

- To implement a trie its like a tree that has multiple branches and then each has its own children
- We have a variable to mark where a word ends to ensure checking that a word is actually added into the trie

# 226. Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/

- BFS or DFS solution
- You have to be at the respective nodes and swap them to their new positons
- Do so till the entire tree is traversed

# 235. Lowest Common Ancestor of a Binary Search Tree

Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

- We know its a binary tree so there are properties we need to remember such that the left side of a node value is smaller than it and the right side is larger than it
- This simplifies it to us checking for cases where its either both on the left side or right side
- The other case being they are split left and right side
- Time complexity is `log n` where `n` is the height of the tree

# 543. Diameter of Binary Tree

Link: https://leetcode.com/problems/diameter-of-binary-tree/description/

- We have a global variable / member variable of the class
- We do DFS but on both sides to get the max path of each on that node
- Update and recurse accordingly

# 572. Subtree of Another Tree

Link: https://leetcode.com/problems/subtree-of-another-tree/description/

- The idea is that we can first find a matching node to the root of the subtree
- And after that we can compare the trees side by side
- Using a DFS and recursion is super helpful here
