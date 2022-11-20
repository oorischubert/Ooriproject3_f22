#Authors
#Oori Schubert
#Wesley Gilpin

from Movie import *
from MovieList import *
from Queue import *
from tkinter import *

class Node:
    def __init__(self, movie):
        self.movie = movie
        self.left = None
        self.right = None
        self.index = 0
    def __str__(self):
        return str(self.movie)

class MovieBST:
    def __init__(self,database = None):
        self.__root = None
        self.__size = 0
        if database is not None:
            file = open(database, "r")
            for line in file:
                line = line.strip()
                line = line.split(";")
                movie = Movie(int(line[0]), int(line[1]), line[2]) #split string
                self.insert(movie)
            file.close()
    
    def getSize(self) -> int:
        """Returns size of tree"""
        return self.__size
    
    def insert(self, movie) -> None:
        """Inserts a movie object"""
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
        """Returns a movie object"""
        if self.getSize() == 0: return None
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
        """Displays the BSTree"""
        print("The BSTree looks like: ")
        self.__show(self.__root, 0)
    
    def __show(self, node, level) -> None:
        if node != None:
            self.__show(node.right, level + 1)
            print("%s%s(%s)"%("      " * level,node.movie.getID(),node.index))
            self.__show(node.left, level + 1)

    def extractListInOrder(self, keyword) -> MovieList:
        """Returns a MovieList Class"""
        print("Begin sublist extraction for word:%s using in-order traversal"%(keyword))
        newList = MovieList()
        self.__extractListInOrder(self.__root, keyword, newList)
        return newList
    
    def __extractListInOrder(self, node, keyword, newList) -> None:
        if node is not None:
            self.__extractListInOrder(node.left, keyword, newList)
            self.__extractListInOrder(node.right, keyword, newList)
            splitTitle = node.movie.getTitle().lower().split(" ")
            for word in splitTitle:
                if keyword == word:
                    newList.insert(node.movie)
                    break
    
    def getMaxIndex(self) -> int:
        """Returns max index of the tree"""
        index = self.__getMaxIndex(self.__root)
        return index
    
    def __getMaxIndex(self, node, index=0) -> int:
        if index < node.index:
            index = node.index
        if node.right is not None:
            index = self.__getMaxIndex(node.right, index)
        if node.left is not None:
            index = self.__getMaxIndex(node.left, index)
        return index
    
    def getMaxLevel(self) -> int:
        """Returns max level of the tree"""
        level = self.__getMaxLevel(self.__root)
        return level
    
    def __getMaxLevel(self, node, level=-1) -> int:
        if node is not None:
            level += 1
            rightLevel = self.__getMaxLevel(node.right, level)
            leftLevel = self.__getMaxLevel(node.left, level)
            if rightLevel > leftLevel: level = rightLevel
            else: level = leftLevel
        return level
        
    def displayLevelOrder(self) -> list:
        """Returns a list of movies in index order"""
        listdb = self.__displayLevelOrder(self.__root)
        return listdb
    
    def __displayLevelOrder(self, node) -> list:
        listdb = [None] * (self.getMaxIndex() + 1) #create empty list
        if node is not None:
            queue = Queue()
            queue.enqueue(node)
            while not queue.isEmpty():
                temp = queue.dequeue()
                print(temp)
                listdb[temp.index] = temp.movie  # type: ignore
                if temp.left is not None: # type: ignore
                    queue.enqueue(temp.left) # type: ignore
                if temp.right is not None: # type: ignore
                    queue.enqueue(temp.right) # type: ignore
        return listdb
    
    @staticmethod
    def plotBST(listDB) -> None:
        root = Tk()
        root.title("BSTree")
        sWidth = 1000 #canvas width
        sHeight = 1000 #canvas height
        canvas = Canvas(root, width=sWidth, height=sHeight, bg="white")
        canvas.pack()
        circleRad = 5
        level = 0
        while 2**level < len(listDB): #get max level
            level += 1
        maxItems = 2**level - 1
        xList = [None] * maxItems #create empty list
        for i in range(len(listDB)):
            if listDB[i] is not None:
                xList[i] = listDB[i]
        for i in range(level):
            itemPlace = 0
            for j in range(2**i-1,2*(2**i-1)+1):
                x = (sWidth/2)/(2**i) + sWidth/(2**i) * itemPlace
                itemPlace += 1 #increment itemPlace
                y = 20 + i*40 #increment level coordinate
                if xList[j] is not None:
                    canvas.create_oval(x-circleRad, y-circleRad, x+circleRad, y+circleRad, fill="blue")
                else:
                    canvas.create_oval(x-circleRad, y-circleRad, x+circleRad, y+circleRad, fill="grey")
                if i is not level-1: #if not last level
                        if xList[2*j+1] is not None:
                            canvas.create_line(x, y, x-(sWidth/2)/(2**(i+1)), y+40, fill="blue")
                        else: 
                            canvas.create_line(x, y, x-(sWidth/2)/(2**(i+1)), y+40, fill="grey")
                        if xList[2*j+2] is not None:
                            canvas.create_line(x, y, x+(sWidth/2)/(2**(i+1)), y+40, fill="blue")
                        else:
                            canvas.create_line(x, y, x+(sWidth/2)/(2**(i+1)), y+40, fill="grey")         
        root.mainloop() #activate!