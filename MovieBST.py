#Authors
#Oori Schubert
#Wesley Gilpin

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