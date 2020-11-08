# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def flatten(self, root):
        if root is None or (root.right is None and root.left is None):
            return

        if root.left is not None:
            self.flatten(root.left)

            treempNode = root.right
            root.right = root.left
            root.left = None

            curr = root.right
            while curr.right is not None:
                curr = curr.right

            curr.right = treempNode

        self.flatten(root.right)

if __name__ == '__main__':
    t = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    Solution().flatten(t)
