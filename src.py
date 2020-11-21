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
        BinaryTree.searchState = None
        BinaryTree.getterState = None
        BinaryTree.foundResult = False
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
    # here are our traversal methods
    def bookTraverse(self):
        """
        bookTraverse is like reading a book:
        top to bottom, left to right

        Used as argument to search and get methods
        """
        if BinaryTree.searchState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = True 
        if BinaryTree.getterState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = self 
            # here, BinaryTree.foundResult will be a BinaryTree instance itself
        if self.getLeftChild():
            self.leftChild.bookTraverse()
        if self.getRightChild():
            self.rightChild.bookTraverse()
    def revDepthTraverse(self):
        """
        bottom to top, left to right

        Used as argument to search and get methods
        """
        if self.getLeftChild():
            self.leftChild.revDepthTraverse()
        if self.getRightChild():
            self.rightChild.revDepthTraverse()
        if BinaryTree.searchState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = True 
        if BinaryTree.getterState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = self  
    def revWidthTraverse(self):
        """
        top to bottom, but right to left

        Used as argument to search and get methods
        """
        if BinaryTree.searchState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = True 
        if BinaryTree.getterState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = self 
        if self.getRightChild():
            self.rightChild.revWidthTraverse()
        if self.getLeftChild():
            self.leftChild.revWidthTraverse() 
    def revDepWidthTraverse(self):
        """
        bottom to top, right to left

        Used as argument to search and get methods
        """
        if self.getRightChild():
            self.rightChild.revDepWidthTraverse()
        if self.getLeftChild():
            self.leftChild.revDepWidthTraverse()
        if BinaryTree.searchState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = True 
        if BinaryTree.getterState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = self 
    def triangleTraverse(self):
        """
        traversal looks like a triangle:
        bottom, up, right, bottom, up, right

        Used as argument to search and get methods
        """

        if self.getLeftChild():
            self.getLeftChild().triangleTraverse()
        if BinaryTree.searchState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = True 
        if BinaryTree.getterState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = self 
        if self.getRightChild():
            self.getRightChild().triangleTraverse()

    def revTriangleTraverse(self):
        """
        triangle starting on bottom right:
        bottom, up, left, bottom, up, left

        Used as argument to search and get methods

        Returns:
            None
        """
        if self.getRightChild():
            self.rightChild.revTriangleTraverse() # recursive aspect
        
        if BinaryTree.searchState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = True 
            # since we're using recursion with instances of classes, things 
            # get very messy if we try to do a simple return statment
            # so instead, I used static variables that change based on 
        if BinaryTree.getterState == True and BinaryTree.searchItem == self.key:
            BinaryTree.foundResult = self 
            # here, BinaryTree.foundResult will be a BinaryTree instance itself

        if self.getLeftChild():
            self.leftChild.revTriangleTraverse() # recursive aspect

    def search(self, item, traverseMethod=bookTraverse):
        """
        search works by actually running through whichever traversal method we choose
        Then, inside those traversal methods, static variable BinaryTree.foundResult is changed
        based on whether item was found or not

        Args:
            item (type is dependent on keys in nodes of tree): item we are searching for
            traverseMethod: Traversal method to be used in search. 
            Options are: bookTraverse, revDepthTravers, revWidthTraverse, RevDepWidthTraverse, triangleTraverse, revTriangleTraverse.
            If you have a rough idea of where your item might be located, 
            changing traversal method can cut down on search time. Defaults to bookTraverse.

        Returns:
            BinaryTree.foundResult: True or False bool
        """
        BinaryTree.foundResult = False # reset each time we run
        BinaryTree.searchState = True
        BinaryTree.getterState = False
        BinaryTree.searchItem = item
        traverseMethod()
        return BinaryTree.foundResult
    
    def get(self, item, traverseMethod=bookTraverse):
        """
        Get works by actually running through whichever traversal method we choose
        Then, inside those traversal methods, static variable BinaryTree.foundResult is changed
        based on whether item was found or not

        Args:
            item (type is dependent on keys in nodes of tree): item we are searching for
            traverseMethod: Traversal method to be used in search. 
            Options are: bookTraverse, revDepthTravers, revWidthTraverse, RevDepWidthTraverse, triangleTraverse, revTriangleTraverse.
            If you have a rough idea of where your item might be located, 
            changing traversal method can cut down on search time. Defaults to bookTraverse.

        Returns:
            BinaryTree.foundResult: True or False bool
        """
        BinaryTree.foundResult = False
        BinaryTree.searchState = False
        BinaryTree.getterState = True
        BinaryTree.searchItem = item
        traverseMethod()
        return BinaryTree.foundResult
        
    def __repr__(self):
        return f'[key:{self.key}, leftChild: {self.leftChild}, rightChild: {self.rightChild}]'

if __name__ == '__main__':
    # testing
    bt = BinaryTree('Root')
    bt.insertLeft('left branch')
    bt.insertRight('right branch')
    bt.leftChild.insertLeft('l.l')
    bt.leftChild.leftChild.insertLeft('l.l.l')
    bt.leftChild.leftChild.insertRight('l.l.r')
    bt.leftChild.insertRight('l.r')
    bt.rightChild.insertLeft('r.l')
    bt.rightChild.leftChild.insertLeft('r.l.l')
    bt.rightChild.insertRight('r.r')
    bt.rightChild.rightChild.insertRight('r.r.r')
    print('\nbook traversing')
    bt.bookTraverse()
    print('\nreverse depth traversing')
    bt.revDepthTraverse()
    print('\nreverse width traversing')
    bt.revWidthTraverse()
    print('\nreverse depth and width traversing')
    bt.revDepWidthTraverse()
    print('\ntriangle traversing')
    bt.triangleTraverse()
    print('\nreverse triangle traversing')
    print(bt.search(item='l.l.l', traverseMethod=bt.bookTraverse)) # True
    print(bt.search(item='l.l.l', traverseMethod=bt.revDepthTraverse))
    print(bt.search(item='l.l.l', traverseMethod=bt.revWidthTraverse))
    print(bt.search(item='l.l.l', traverseMethod=bt.revDepWidthTraverse))
    print(bt.search(item='l.l.l', traverseMethod=bt.triangleTraverse))
    print(bt.search(item='l.l.l', traverseMethod=bt.revTriangleTraverse)) # True
    print(bt.search(item='sadlkjfsdalkfjh', traverseMethod=bt.revTriangleTraverse)) # False
    print(bt.get(item='l.l', traverseMethod=bt.revTriangleTraverse)) # returns tree

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
    # What happens here is our parser comes to * at the root of our tree, and
    # left (3) and right (2+5) both exist, so we get:
    # *(3, ___). Three has no children, so it is returned as the first argument
    # then we come to the node +, which operates on 2 and 5
    # which have no children, so they are retuned as arguments, so we have:
    # *(3, +(2, 5)) = 3*(2+5) = 21
    print(evalTree(pt))
