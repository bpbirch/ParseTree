#%%
import operator
#%%

class BinaryTree:
    # BinaryTree is composed of nodes and references to other nodes
    def __init__(self, rootObj):
        self.key = rootObj # the root object / key of a binarytree can be any kind of object
        self.leftChild = None # reference to a left node
        self.rightChild = None # reference to a right node
        self.parent = None
    def getLeftChild(self):
        return self.leftChild 
    def getRightChild(self):
        return self.rightChild
    def getParent(self): # adding parent functionality to avoid using stacks in parseTree function
        return self.parent
    def setRootVal(self, obj):
        self.key = obj 
    def getRootVal(self):
        return self.key
    def insertLeft(self, obj): # insert a new node whose key is obj
        if self.leftChild == None:
            self.leftChild = BinaryTree(obj)
            self.leftChild.parent = self # adding parent references
        else:
            newLeft = BinaryTree(obj)
            newLeft.left = self.leftChild 
            self.leftChild.parent = newLeft # must assign two new parent references
            newLeft.parent = self
            self.leftChild = newLeft
            # here we're inserting a new Binary Tree as a child,
            # and the root value of that new tree is obj
    def insertRight(self, obj): # insert a new node whose key is obj
        if self.rightChild == None:
            self.rightChild = BinaryTree(obj)
            self.rightChild.parent = self
        else:
            newRight = BinaryTree(obj)
            newRight.right = self.rightChild
            self.rightChild = newRight

    def __repr__(self):
        return f'[key:{self.key}, leftChild: {self.leftChild}, rightChild: {self.rightChild}]'

if __name__ == '__main__':
    bt = BinaryTree('hello')
    bt.insertLeft(99)
    lc = bt.getLeftChild()
    lc.insertLeft(13) # this is a reference, so inserts into bc tree
    lcc = lc.getLeftChild()
    print(lcc.parent)
    print(lc.parent) # this will be the entire binary tree, since parent of lc is the root node


#%% parse tree
# a parse tree is a structure that allows us to represent mathematical expressions
# as hierarchical node/reference relations
# This is very similar to Miller & Ranum's parseTree, but I utilized parent functionality
# in my BinaryTree class, so I didn't have to utilize stacks here
# we'll write this as a function that returns an instance of a class
def parseTree(expression):
    expList = [item for item in expression if item != ' '] # ignore whitespace
    tree = BinaryTree('')
    currentTree = tree
    for item in expList:
        if item == '(':
            currentTree.insertLeft('') # make a new node whose rootVal is '', as leftChild
            currentTree = currentTree.getLeftChild()
        elif item not in '+-*/)':
            currentTree.setRootVal(eval(item)) # if item is a number, make it rootVal, then go to parent
            currentTree = currentTree.getParent()
        elif item in '+-*/':
            currentTree.setRootVal(item)
            currentTree.insertRight('') # insert a new node as right child
            currentTree = currentTree.getRightChild()
        elif item == ')':
            currentTree = currentTree.getParent()
        else:
            raise ValueError(f'Unknown token: {item}')
    return tree
        
if __name__ == '__main__':
    pt = parseTree('(3+(4*7))')
    print(pt) # this is giving the correct tree

#%%
def evalTree(pTree):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = pTree.getLeftChild()
    right = pTree.getRightChild()
    # the following is our recursive basecase, in which we do not have any child values
    # because in our tree, leaf nodes are always integers / operands
    if left and right:
        op = ops[pTree.getRootVal()]
        return op(evalTree(left), evalTree(right)) # so this is where we recursively delve deeper into our tree
    else:
        return pTree.getRootVal() # returns our operands 

if __name__ == '__main__':
    pt = parseTree('(3*(2+5))') # should return 21
    # so evalTree will recursively create a stack (because that's what recursion is)
    # and will go until it finds 3, 2, and 5. Then + operates on 2 and 5, then * operates on 7
    print(evalTree(pt))
