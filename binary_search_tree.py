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
    

    def inorder_traversal_stack(self):
        res = []
        stack = []
        current = self.root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            

            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res
    
    def postorder_traversal_two_stack(self):
        res = []
        stack1 = [self.root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)

                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
        

        while stack2:
            node = stack2.pop()
            res.append(node.val)
        
        return res



    def inorder_traversal_recursion(self):
        res = []

        def traversal(node):
            if node:
                traversal(node.left)
                res.append(node.val)
                traversal(node.right)
        
        traversal(self.root)
        return res
    
    def preorder_traversal_recursion(self):
        res = []

        def traversal(node):
            if node:
                res.append(node.val)
                traversal(node.left)
                traversal(node.right)
        traversal(self.root)

        return res
    
    def postorder_traversal_recursion(self):
        res = []

        def traversal(node):
            if node:
                traversal(node.left)
                traversal(node.right)
                res.append(node.val)
        traversal(self.root)
        return res
    


    

tree = Tree()

# tree.insert(10)
# tree.insert(5)
# tree.insert(15)
# tree.insert(3)
# tree.insert(7)
# tree.insert(18)

tree.insert(17)
tree.insert(7)
tree.insert(23)
tree.insert(1)
tree.insert(12)
tree.insert(19)

# tree.insert(1)
# tree.insert(2)
# tree.insert(3)
# tree.insert(4)
# tree.insert(5)
# tree.insert(6)

print('preorder traversal stack:',tree.preorder_traversal_stack())
print('inorder traversal stack:', tree.inorder_traversal_stack())
print('postorder traversal two stack:', tree.postorder_traversal_two_stack())


print('preordertraversal using recursion:', tree.preorder_traversal_recursion())
print('inorder traversal using recursion:', tree.inorder_traversal_recursion())
print('postorder traversal using recursion:', tree.postorder_traversal_recursion())


