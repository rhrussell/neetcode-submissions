# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]
        self.dfs(root, result)
        return result[0]

    def dfs(self, head: Optional[TreeNode], result):
        if head is None:
            return 0

        left_height = self.dfs(head.left, result)
        right_height = self.dfs(head.right, result)

        result[0] = max(result[0], left_height + right_height)

        return 1 + max(left_height, right_height)