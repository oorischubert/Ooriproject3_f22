#Authors
#Oori Schubert
#Wesley Gilpin

from Movie import *
import random


class MovieList:
    def __init__(self,database=None):
        self.__movies = []
        self.__size = 0
        if database is not None:
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
        self.__movies.append(movie)
        self.__size += 1
    
    def binarySearch(self, movieID):
        low = 0
        high = self.__size - 1
        while low <= high:
            mid = (low + high) // 2
            if self.__movies[mid].getID() == movieID:
                return self.__movies[mid]
            elif self.__movies[mid].getID() < movieID:
                low = mid + 1
            else:
                high = mid - 1
        return False
    
    def shuffle(self) -> None:
        for i in range(self.__size):
            j = random.randint(0,self.__size-1)
            temp = self.__movies[i]
            self.__movies[i] = self.__movies[j]
            self.__movies[j] = temp

    def save(self,database) -> None:
        file = open(database, "w")
        for i in range(self.__size):
            file.write(str(self.__movies[i].getID()) + ";" + str(self.__movies[i].getYear()) + ";" + self.__movies[i].getTitle() + ";\n")
        file.close()

    def display(self) -> None:
        for i in range(self.__size):
            print(self.__movies[i])
