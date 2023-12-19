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

# 124. Binary Tree Maximum Path Sum

Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

- We calculate the subtrees path and then add on the max to the root node
- Since we cannot split we have to check which path is the max or that neither is and the node is not worth adding

# 226. Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/

- BFS or DFS solution
- You have to be at the respective nodes and swap them to their new positons
- Do so till the entire tree is traversed
