class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def delete(node):  # find the node and its parent node to be removed
    delNodeParent = node
    delNode = node.right
    while delNode.left:
        delNodeParent = delNode
        delNode = delNode.left  # replace the data value
    node.data = delNode.data
    if delNode.right:  # if the right child exists, connect the parent
        if delNodeParent.data > delNode.data:
            delNodeParent.left = delNode.right
        else:
            delNodeParent.right = delNode.right
    else:  # if the node has no right child, remove the node
        if delNode.data < delNodeParent.data:
            delNodeParent.left = None
        else:
            delNodeParent.right = None


class BinaryTree:
    def __init__(self):
        self.root = None  # starting with an empty root node

    def insert(self, data):
        if self.root is None:  # if the tree is empty, insert a data of a new root node
            self.root = Node(data)
        else:  # if not call the _insert function to add the node to the tree
            self.add(data, self.root)

    def add(self, data, cur_node):  # function to recursively add a new node to the tree
        if data < cur_node.data:  # add the node to the left node subtree
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self.add(data, cur_node.left)
        elif data > cur_node.data:  # add the node to the right node subtree
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.add(data, cur_node.right)
        else:  # if the data is in the tree, print this message
            print("Value already present in tree")

    def display(self, cur_node):  # display method to print the binary tree in string
        lines, _, _, _ = self.show(cur_node)
        for line in lines:
            print(line)

    def show(self, cur_node):
        if cur_node.right is None and cur_node.left is None:  # if the current node is a leaf node, return a single line
            line = '%s' % cur_node.data  # concatenation of strings together
            width = len(line)  # the width is the length of the line
            height = 1
            middle = width // 2
            return [line], width, height, middle  # return array of line, width, height, and middle of width length

        if cur_node.right is None:
            lines, n, p, x = self.show(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if cur_node.left is None:
            lines, n, p, x = self.show(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.show(cur_node.left)
        right, m, q, y = self.show(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def remove(self, target):
        if self.root is None:  # if root node is None return False
            return False
        elif self.root.data == target:  # check if the root node is the target
            if self.root.left is None and self.root.right is None:  # if root node has no child, the root is None
                self.root = None
            elif self.root.left and self.root.right is None:  # If root node has only left child, set root to left child
                self.root = self.root.left
            elif self.root.left is None and self.root.right:  # if root has only right child, set root to right child
                self.root = self.root.right
            elif self.root.left and self.root.right:  # if root node has both child, call _remove function
                delete(self.root)
            return True

        parent = None
        node = self.root
        while node and node.data != target:
            parent = node
            if target < node.data:
                node = node.left
            else:
                node = node.right
        if node is None or node.data != target:  # if the data is not the target, return False
            return False
        elif node.left is None and node.right is None:  # if the target node has no child
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        elif node.left and node.right is None: # if the target node has only left child
            if target < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        elif node.left is None and node.right:  # if the target node has only right child
            if target < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        else:  # if the target node has both child call _remove function and return True
            delete(node)
            return True


bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)

bst.display(bst.root)

bst.remove(6)
bst.remove(4)
bst.remove(100)

bst.display(bst.root)
