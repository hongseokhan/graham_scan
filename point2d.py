class Point2D:
    def __init__(self):
        self.__x = 0.0
        self.__y = 0.0   

    @property
    def xcoord(self):
        return self.__x
    
    @xcoord.setter
    def xcoord(self,x):
        self.__x = x

    @property
    def ycoord(self):
        return self.__y
    
    @ycoord.setter
    def ycoord(self,y):
        self.__y = y