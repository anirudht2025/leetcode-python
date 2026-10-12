class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def depth(node):
            nonlocal diameter

            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            diameter = max(diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root)
        return diameter
