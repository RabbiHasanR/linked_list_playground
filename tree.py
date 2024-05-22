class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None


    def insert(self, val):
        new_node = Node(val)

        if self.root is None:
            self.root = new_node
            return
        
        stack = [self.root]

        while stack:
            current = stack.pop()

            if val < current.val:
                if current.left is None:
                    current.left = new_node
                else:
                    stack.append(current.left)
            else:
                if current.right is None:
                    current.right = new_node
                else:
                    stack.append(current.right)

    def preorder_traversal_stack(self):

        res = []
        stack = [self.root]

        while stack:
            current = stack.pop()
            if current:
                res.append(current.val)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
        return res
    



tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

print(tree.preorder_traversal_stack())
