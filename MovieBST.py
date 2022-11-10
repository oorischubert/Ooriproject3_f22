### To complete

#Here the code makes use of the randomized list of ID “Movies.txt” obtained with the previous app and create a Binary Search Tree (BST) (the random list will guarantee that the BST is fairly balanced).
#What you need to implement in MovieBST.py:
#1. The class Node (as seen in class) followed by the class MovieBST (in the same file).
#2. A constructor that reads the file and insert all items in the BST.
#3. The insert method. Note: the Tree is sorted by ID number. This method should be recursive.
#4. The getSize method
#5. The search method that accepts an ID number and return the corresponding movie.
#This method can be iterative or recursive.
#6. Requirement: variables such as “the number of items” should be private. Auxiliary methods used in recursion must also be private.
#create a BST, display “in-order” the list, show the tree structure (90 degree angle) using both ID and index level numbers.


#1. The method displayInOrder and its “private” recursive auxiliary routine. All the
#movies in the BST will be listed when the latter is traversed in order.
#2. The method show and and its “private” recursive auxiliary routine, that displays the 90 degree shifted tree structure with the ID number and index number in parenthesis. Make sure, you get the same output...
#Remark: In addition to the traditional references ’left’, ’right’, your Node class should contain an ’index’ attribute that indicates the level-order position of the node in the Tree structure (lecture 18). Rule: The index of root is 0, if a current node has index “index”, the index of its left child is “2*index+1” and right child is “2*index+2”. The index numbers of a given node can easily be set up during insertion

from Movie import *
class Node:
    def __init__(self, movie):
        self.__movie = movie
        self.__left = None
        self.__right = None
    def __str__(self):
        return str(self.__movie)

class MovieBST:
    def __init__(self,database):
        self.__root = None
        self.__size = 0
        file = open(database, "r")
        for line in file:
            line = line.strip()
            line = line.split(";")
            movie = Movie(int(line[0]), int(line[1]), line[2])
            self.insert(movie)
        file.close()
    
    def getSize(self) -> int:
        return self.__size
    
    def insert(self, movie):
        if self.__root == None:
            self.__root = Node(movie)
            self.__size += 1
        else:
            self.__insert(self.__root, movie)
    
    def __insert(self, node, movie) -> Node:
        if node == None:
            node = Node(movie)
            self.__size += 1
        else:
            if movie.getID() < node.__movie.getID():
                node.__left = self.__insert(node.__left, movie)
            else:
                node.__right = self.__insert(node.__right, movie)
        return node
    
    def search(self, movieID):
        return self.__search(self.__root, movieID)
    
    def __search(self, node, movieID):
        if node == None:
            return False
        elif int(node.__movie.getID()) == movieID:
            return node.__movie
        elif node.__movie.getID() < movieID:
            return self.__search(node.__right, movieID)
        else:
            return self.__search(node.__left, movieID)

    def displayInOrder(self):
        self.__displayInOrder(self.__root)
    
    def __displayInOrder(self, node):
        if node != None:
            print(node)
            self.__displayInOrder(node.__left)
            self.__displayInOrder(node.__right)
    
    def show(self):
        self.__show(self.__root, 0)
    
    def __show(self, node, level):
        if node != None:
            self.__show(node.__right, level + 1)
            print("   " * level, node)
            self.__show(node.__left, level + 1)