#Authors
#Oori Schubert
#Wesley Gilpin

from Movie import *
from MovieList import *

class Node:
    def __init__(self, movie):
        self.movie = movie
        self.left = None
        self.right = None
        self.index = 0
    def __str__(self):
        return str(self.movie)

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
    
    def insert(self, movie) -> None:
        if self.__root is None:
            self.__root = Node(movie)
            self.__size += 1
        else:
            self.__insert(self.__root, movie)

    def __insert(self, node, movie):
        if movie.getID() < node.movie.getID():
            if node.left is None:
                newNode = Node(movie)
                newNode.index = 2*node.index + 1
                node.left = newNode
                self.__size += 1
            else:
                self.__insert(node.left, movie)
        elif movie.getID() > node.movie.getID():
            if node.right is None:
                newNode = Node(movie)
                newNode.index = 2*node.index + 2
                node.right = newNode
                self.__size += 1
            else:
                self.__insert(node.right, movie)
    
    def search(self, movieID):
        if self.getSize() is 0: return None
        return self.__search(self.__root, movieID)
    
    def __search(self, node, movieID):
        if node is None: 
            return None
        elif  movieID < node.movie.getID():
            #print("left")
            temp = self.__search(node.left, movieID)
        elif movieID > node.movie.getID():
            #print("right")
            temp = self.__search(node.right, movieID)
        else: 
            temp = node.movie
        return temp

    def displayInOrder(self) -> None:
        print("Display in order %s items by ID"%(self.getSize()))
        self.__displayInOrder(self.__root)
    
    def __displayInOrder(self, node) -> None:
        if node is not None:
            self.__displayInOrder(node.left)
            print(node)
            self.__displayInOrder(node.right)
    
    def show(self) -> None:
        print("The BSTree looks like: ")
        self.__show(self.__root, 0)
    
    def __show(self, node, level) -> None:
        if node != None:
            self.__show(node.right, level + 1)
            print("%s%s(%s)"%("      " * level,node.movie.getID(),node.index))
            self.__show(node.left, level + 1)

    def extractListInOrder(self, keyword):
        print("Begin sublist extraction for word:%s using in-order traversal"%(keyword))
        newList = MovieList()
        self.__extractListInOrder(self.__root, keyword, newList)
        return newList
    
    def __extractListInOrder(self, node, keyword, newList):
        if node is not None:
            self.__extractListInOrder(node.right, keyword, newList)
            splitTitle = node.movie.getTitle().lower().split(" ")
            for word in splitTitle:
                if keyword == word:
                    newList.insert(node.movie)
                    break
            self.__extractListInOrder(node.left, keyword, newList)
