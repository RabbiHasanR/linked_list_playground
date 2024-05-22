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