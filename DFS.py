class Node:
definit (self, key):
self.left None
self.right = None
self.val = key
#A function to do inorder tree traversal
def printInorder(root):
if root:
#First recur on left child
printInorder(root.left)
#then print the data of node
print(root.val),
# now recur on right child
printlnorder(root.right)
# Driver code
root = Node(1)
root.left Node(2)
root.right Node(3)
root.left.left = Node(4)
root.left.rightNode(5)
root.right.leftNode(6)
root.right.rightNode(7)
root.left. left.left = Node(8)
root.left.right.left = Node(9)
foot.right.left.left = Node(10)
root.right.right.right = Node(11)
print ("\nInorder traversal of binary tree is")
printlnorder(root)
