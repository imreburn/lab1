# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
# remember row and column index
# data structure to store : dictionary two-dimensional array
# for certain node, save the value at appropriate 
        from collections import defaultdict
    
        d = defaultdict(list)
        
        def _vtraversal(node, col, row, d):
            if node == None:
                return None
            else:
                _vtraversal(node.left, col-1, row+1, d)
                d[col] += [(row, node.val)]
                _vtraversal(node.right, col+1, row+1, d)

        _vtraversal(root, 0, 0, d)
        res = []
        for i in sorted([*d.keys()]):
            res.append([val for (_, val) in sorted(d[i])])
        return res
        