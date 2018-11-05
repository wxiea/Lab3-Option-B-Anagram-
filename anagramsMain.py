from treesAVL import avlTree
from treesAVL import Node

global tree
'''
'populateTree' is a mehtod that takes a file name and a tree parameter and 
populates the tree with the words from the textFile
'''
def populateTree(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        current_line = line.split()
        if isinstance(tree, avlTree):
            tree.insert(Node(current_line[0]))
        else:
            tree.insert(current_line[0])

#method provided by the PDF file
            
def print_anagrams(word, prefix=""):    
    if len(word) <= 1:        
        str = prefix + word 
        current = tree.search(str)
        if current is not None:            
            print(current.key)    
    else:        
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur            
            after = word[i + 1:] # letters after cur
 
            if cur not in before: # Check if permutations of cur have not been generated.                
                print_anagrams(before + after, prefix + cur) 
            print_anagrams(word, prefix)

tree = avlTree()
populateTree("words.txt", tree)
print_anagrams(tree, "POTS")