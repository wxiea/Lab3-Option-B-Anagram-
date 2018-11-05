class avlTree:
    #simple constructor to create an empty tree (value is None)
    def __init__(self):
        self.root = None

    '''
    'rotateLeft' method performs a left roatation at node and returns the 
    new root of the subtree that is generated.
    '''
    def rotateLeft(self, node):
        #pointer to the right child of the left child.
        right_leftChild = node.right.left
        
        #the right child moves up to the node's position.
        if node.parent is not None:
            node.parent.updateChild(node, node.right)
        #make root  
        else:
            self.root = node.right
            self.root.parent = None #since we just have a root the parent is None

        #The node becomes the left child of the old right child(That is now the parent.)
        node.right.assignChild('left', node)
        #make right_leftChild the right child of node.
        node.assignChild('right', right_leftChild)
        
        return node.parent

    '''
    'rotateRight' method performs a right rotation at a node and returns
    the root of a the new subtree that is generated 
    '''
    def rotateRight(self, node):
        # pointer to the left child of the right child.
        left_rightChild = node.left.right
        
        # left child moves up to the node's position.
        if node.parent is not None:
            node.parent.updateChild(node, node.left)
        #make root
        else:
            self.root = node.left
            self.root.parent = None
        # node becomes the right child of left child (That is now parent.)
        node.left.assignChild('right', node)

        # make left_rightChild the left child of node.
        node.assignChild('left', left_rightChild)
        return node.parent
    
    '''
    'rebalance' method simpy updates the current nodes height and 
    rebalances the subtrees only if the balance factor is -2 or 2
    '''
    def rebalance(self, node):
        # update the height of current node.
        node.calculateHeight()        
        if node.getBalance() == -2: #if an inbalance exist then 
            if node.right.getBalance() == 1:# check if right subtree is too big.
                #do a right rotation
                self.rotateRight(node.right)
            # left rotation will make the subtree balance
            return self.rotateLeft(node)
                        
        elif node.getBalance() == 2:
            if node.left.getBalance() == -1:# check if the left subtree is too big.
                # do a left rotation
                self.rotateLeft(node.left)
            # right rotation will make the subtree balanced.
            return self.rotateRight(node)
            
        #if no inbalance is found then return the node
        return node
    
    '''
    'insert' method simple checks if the tree is empty, if so then creates the
    root of the tree. After that then the method uses a simple binary search
    inseriton method (checks if node.key is less than or greater than current node)
    then a rebalance is made in the subtree and the rest of the tree since the
    subtree has been modified.
    '''
    def insert(self, node):
        #if the tree is empty, then the root is the new Node
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            # binary search tree insert.
            temp = self.root
            while temp is not None:
                if node.key < temp.key: #if value is less than temp then inser left
                    if temp.left is None: #check if left subtree is None
                        temp.left = node
                        node.parent = temp
                        temp = None
                    else:
                        temp = temp.left #go to the next left child
                        
                else: #if the node has a greater value then insert to the right
                    if temp.right is None: #check if the right node is None
                        temp.right = node
                        node.parent = temp
                        temp = None
                    else:
                        temp = temp.right #go to the next right child
                
            #Rebalance the new node's parent up until the root is reached
            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent
    
    '''
    'remove' method checks for many cases (if the node has 1 or 2 or 0 child, also if the node is leaf)
    it rebalances the subtree after a deletions is made.
    '''
    def remove(self, node):
        if node is None: #if the current node is None then just simply return False
            return False
        #get parent of current node
        parent = node.parent
    
        if node.left is not None and node.right is not None:#check if node has 2 childs
            successor = node.right # get the successor
            while successor.left != None:
                successor = successor.left
                
            node.key = successor.key #copy word
            self.remove(successor) #remove successor
                
            return True #since everyhting has been balanced we return
        
        elif node is self.root: #check if node has 1 or 0 child
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right
                
            if self.root is not None:
                self.root.parent = None
            return True
        
        elif node.left is not None: #node with only left child
            parent.updateChild(node, node.left)
            
        else: #node is leaf or has only right child
            parent.updateChild(node, node.right)
        node = parent
        while node is not None:
            self.rebalance(node)            
            node = node.parent
        return True

    '''
    'search' method searches for a certain word(key) in the tree that matches
    the word(key) that is being passed as a parameter.
    '''
    def search(self, key):
        temp = self.root
        while temp is not None:
            if temp.key.lower() == key.lower(): #compare the word with the current node word
                return temp
            elif key > temp.key: 
                temp = temp.right
            else: temp = temp.left
        return None

'''
'Node' class is used by the avlTree class, each nodes holds a key(english word)
'''
class Node:
    #default constructor
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0 
        
    '''
    'getBalance' is a method that generates the nodes balance factor
    this balance factor is calculated by height(leftSubtree) - height(rightTree)
    '''
    # defined as height(left subtree) - height(right subtree)
    def getBalance(self):
        heightOfLeft = -1 #if the left subtree is None then the heigth is -1
        if self.left is not None:
            heightOfLeft = self.left.height
            
        heightOfRight = -1 #if the right subtree is None then the height is -1
        if self.right is not None:
            heightOfRight = self.right.height
            
        return heightOfLeft - heightOfRight

    '''
    'calculateHeight' calculates the height of the subtree after it
    has been modified.
    '''
    def calculateHeight(self):
        heightOfLeft = -1 #if the left subtree is None then the heigth is -1 
        if self.left is not None:
            heightOfLeft = self.left.height
            
        heightOfRight = -1 #if the right subtree is None then the height is -1
        if self.right is not None:
            heightOfRight = self.right.height
        
        self.height = max(heightOfLeft, heightOfRight) + 1 #return the maximum height
    
    '''
    'updateChild' method simply updates the current child and replaces it with
    the new child passed as a parameter
    '''
    def updateChild(self, currentChild, newChild):
        if self.left is currentChild:
            return self.assignChild("left", newChild)
        elif self.right is currentChild:
            return self.assignChild("right", newChild)
        
        return False #if the cases fail then new child could not be linked with the current node

    '''
    'assignChild' method assigns either side (left or right) of the tree with a new child
    '''
    def assignChild(self, selectChild, child):
        # selectChild is properly assigned.
        if selectChild != "left" and selectChild != "right":
            return False
        # Assign the left or right new member.
        if selectChild == "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self
        self.calculateHeight() #since the subtree has been modified we must update the height
        return True
