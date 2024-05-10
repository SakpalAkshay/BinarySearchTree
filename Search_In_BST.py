class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if root.val == val:
                return True
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return False
