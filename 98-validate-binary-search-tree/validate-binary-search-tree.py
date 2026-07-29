# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, minimum, maximum) -> bool:
        if not node:
            return True
        
        if not (node.val > minimum and node.val < maximum):
            return False
        
        return self.dfs(node.left, minimum, node.val) and self.dfs(node.right, node.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))

        