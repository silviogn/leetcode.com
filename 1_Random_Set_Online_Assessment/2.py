'''Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        values = {}
        if root is not None:
            self.insert_and_navigate(root, 0, values)
        return [max(value) for value in values.values()]

    def insert_and_navigate(self, node, level, values):
        if level not in values.keys():
            values[level] = [node.val]
        else:
            values[level].append(node.val)

        if node.left is not None:
            self.insert_and_navigate(node.left, level + 1, values)

        if node.right is not None:
            self.insert_and_navigate(node.right, level + 1, values)

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
