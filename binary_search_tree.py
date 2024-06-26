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

    def delete_node(self, key):


        def delete(root, key):
            if root is None:
                return root
            
            if key > root.val:
                root.right = delete(root.right, key)
            elif key < root.val:
                root.left = delete(root.left, key)
            
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                

                # find the min from right subtree

                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = delete(root.right, root.val)

            return root

        return delete(self.root, key)
    
    
    # def rootToLeaf(self):
    #     path = []
    #     index = 0

    #     def printRootToLeaf(node, path, index):
    #         if node is None:
    #             return
            
    #         if index == len(path):
    #             path.append(node.val)
    #         else:
    #             print('index:', index, len(path))
    #             path[index] = node.val
            
    #         if node.left is None and node.right is None:
    #             print('path:', path)
                
            
    #         printRootToLeaf(node.left, path, index + 1)
    #         printRootToLeaf(node.right, path, index + 1)
        
    #     printRootToLeaf(self.root, path, index)
    
    
    def find_paths_using_preorder(self):
        
        def rootToLeaf(node, current_path, all_paths):
            if not node:
                return
            
            current_path.append(node.val)
            
            if not node.left and not node.right:
                all_paths.append(list(current_path))
            else:
                rootToLeaf(node.left, current_path, all_paths)
                rootToLeaf(node.right, current_path, all_paths)
            
            current_path.pop()
        
        find_paths = []
        rootToLeaf(self.root, [], find_paths)
        
        return find_paths
    
    # find max depth
    
    def max_depth_recursion(self):
        
        def max_depth(node):
            if node is None:
                return 0
            else:
                left_depth = max_depth(node.left)
                right_depth = max_depth(node.right)
            
            return max(left_depth, right_depth) + 1
        
        return max_depth(self.root)
    
    
    
        
        
    


    

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


root = tree.delete_node(7)

print('after delete preorder traversal stack:',tree.preorder_traversal_stack())


print('print all root to path')

# tree.rootToLeaf()

print(tree.find_paths_using_preorder())

print('Max depth:', tree.max_depth_recursion())


