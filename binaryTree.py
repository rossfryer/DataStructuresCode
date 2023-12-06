class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

# Create a binary tree and insert the values
values = [2, 5, 12, 3, 8, 4, 9, 56]
tree = BinaryTree(values[0])
for value in values[1:]:
    tree.insert(value)

# Perform preorder, inorder, and postorder traversals to display the tree elements
print("Preorder Traversal:")
tree.preorder_traversal(tree.root)
print("\nInorder Traversal:")
tree.inorder_traversal(tree.root)
print("\nPostorder Traversal:")
tree.postorder_traversal(tree.root)
