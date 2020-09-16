class Queue(object):
    def __init__(self):
        self.item=[]
    def enqueue(self,item):
        self.item.insert(0,item)
    def dequeue(self):
        if not self.isempty():
          return self.item.pop()

    def isempty(self):
        return len(self.item)==0

    def peak(self):
        if not self.isempty():
            return self.item[-1].value
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.item)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def LevelTransverse(self,start):
        if start is None:
            return

        qp=Queue()
        qp.enqueue(start)
        transverse=""
        while len(Queue)>0:
            transverse+=str(Queue.peak())+"-"
            Node=Queue.dequeue()

            if Node.left:
                Queue.enqueue(Node.left)
            if Node.right:
                Queue.enqueue(Node.right)

        return transverse





    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
   
        
# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:#

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.LevelTransverse("levelorder"))