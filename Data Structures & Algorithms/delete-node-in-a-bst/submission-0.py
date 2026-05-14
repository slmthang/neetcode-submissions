# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minVal(self, root):

        while (root and root.left):
            root = root.left

        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None

        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        
        if (key < root.val):
            root.left = self.deleteNode(root.left, key)

        if (key == root.val):

            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            minNode = self.minVal(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)

        
        return root