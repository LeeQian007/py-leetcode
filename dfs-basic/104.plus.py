class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_greater_than_target(root, target):
    def dfs(node, depth):
        if node is None:
            return 0
        if node.val > target:
            return depth + 1
        left = dfs(node.left, depth + 1)
        right = dfs(node.right, depth + 1)
        return max(left, right)

    return dfs(root, 0)