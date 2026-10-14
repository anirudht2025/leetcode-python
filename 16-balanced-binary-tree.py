class Solution:
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                return -1

            if left_height == -1 or right_height == -1:
                return -1

            return 1 + max(left_height, right_height)

        return height(root) != -1
