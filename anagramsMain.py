'''
NAME: Jonathan Argumedo
PROFESSOR NAME: Diego Aguirre 
TA NAME: Anindita Nath  
CLASS: CS 2302 Data Structures
DATE: November 4, 2018 
UPDATDE BY: (Your name goes here)
'''


from treesAVL import avlTree
from treesAVL import Node
from treesRed import redBlackTree

#global tree (can be AVL or Red Black in this specific problem)
global tree
'''
'countAnagram' is a method that returns the total number of anagrams of a word that 
are found in a tree that has 354,984 English Words.
'''
def countAnagram(word, treeOfWords,  listOfWords, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        currentNode = treeOfWords.search(str)
        if currentNode is not None:
            listOfWords.append(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                countAnagram(before + after, treeOfWords,  listOfWords, prefix + cur)
    return len(listOfWords)#the number of anagrams found in the file are in a list
                        #return the len of list and you'll have the anagrams total

'''
'populateAVLtree' is a mehtod that takes a file name and a tree parameter and 
populates the tree with the words from the textFile (Uses AVL Tree)
'''
def populateAVLtree(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        current_line = line.split()
        if isinstance(tree, avlTree):
            tree.insert(Node(current_line[0]))
        else:
            tree.insert(current_line[0])
    file.close()

'''
'populateRedTree' is a method that takes a file name and a tree parameter
and populates the tree with words from the textFile (Uses Red  Black Tree)
'''        
def populateRedTree(fileName, tree):
    file = open(fileName, "r")
    for line in file:
        temp = line.split()
        tree.insert(temp[0])
    file.close()
'''
'print_anagram' is amethod that generates all permutations of a word
each output is verified by traversing a tree, this tree is populated
with over 354,984 English Words. If a match is found then that word is an 
anagram
'''
def print_anagram(word, treeOfWords, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        currentNode = treeOfWords.search(str)
        if currentNode is not None:
            print(currentNode.key)
    else:
        for i in range(len(word)):
            cur = word [i: i + 1]
            before = word[0:i]
            after = word[i +1:]
            if cur not in before:
                print_anagram(before + after, treeOfWords, prefix + cur)
                
'''
'findMaxAnagrams' finds the maximum anagrams found in a file
it takes a tree and a fileName as parameters
'''
def findMaxAnagrams(fileOfWords, tree):
    finalMaxAnagrams = 0
    wordFound = ""
    
    with open(fileOfWords, "r") as file:
        for line in file:
            #call the countAnagrams function that returns the anagrams of each word
            #we call it with every word found in the file that is passed as parameter
            #and the global tree that contains the 354, 984 words
            listOfWords = []
            currentMaxAnagrams = countAnagram(line.split()[0], tree, listOfWords)
            
            if currentMaxAnagrams > finalMaxAnagrams:#if the value returned is greater than the FinalMax then that means a new max has been found
                finalMaxAnagrams = currentMaxAnagrams
                wordFound = line.split()[0]
        print("The word with the most anagrams is '%s' and it has [%d] anagrams." % (wordFound, finalMaxAnagrams))
        print("\nThe anagrams of the word '%s' are..." % (wordFound))
        print_anagram(wordFound, tree)
        
def main():
    while True:
        print("********************************************************************************")
        option = input("Enter the tree you would like to use:\n\n1)AVL Tree\n2)Red Black Tree\n\nEnter response: ")
        if option == '1' or option == "one":#check if the user selected AVL Tree
            try:
                tree = avlTree() #create an empty tree
                print("Populating AVL Tree...")
                populateAVLtree("words.txt", tree) #populate AVL Tree
               
                userWord = input("\nEnter the word you want to search: ")
                count = [] #list used in  method (countAnagrams)
                print("\n\nThe word '%s' has [%d] anagrams." % (userWord, countAnagram(userWord, tree, count)))
                print("\nThe anagrams fro the word '%s' are..." % (userWord))
                print_anagram(userWord, tree) #check if the word has anagrams
                
            except FileNotFoundError:
                print("\n\nOops! File not found!")
                break
            
        #check if the option is an Red Black Tree
        elif option == '2' or option == "two":
            try:
                tree = redBlackTree() #create an empty tree
                print("Populating Red Black Tree...")
                populateRedTree("words.txt", tree)

                userWord = input("\nEnter the word you want to search: ")
                count = [] #list used in  method (countAnagrams)
                print("\n\nThe word '%s' has [%d] anagrams." % (userWord, countAnagram(userWord, tree, count)))
                print("\nThe anagrams fro the word '%s' are..." % (userWord))
                print_anagram(userWord, tree) #check if the word has anagrams
                
            except FileNotFoundError:
                print("\n\nOops! File not found!")
                break
            
        print("\n\n\nFinding the max of anagams of file 'maxAnagrams'...")
        try:
            findMaxAnagrams("maxAnagrams.txt", tree)
            break
        except FileNotFoundError:
            print("\n\nOops! File not found!")
            break
                     
main()   
