# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def _maxPathSum(node):
            if node == None:
                return float('-inf'), float('-inf')         
            
            lmsum, lmdsum = _maxPathSum(node.left)
            rmsum, rmdsum = _maxPathSum(node.right)
            mdsum = max(lmdsum + node.val, rmdsum + node.val, node.val)
            msum = max(lmsum, rmsum, mdsum, lmdsum + node.val + rmdsum)
            
            return msum, mdsum
            
        msum, _ = _maxPathSum(root)
        return msum