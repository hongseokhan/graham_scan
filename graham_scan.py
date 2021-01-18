import os
import random
import math
from point2d import Point2D

class Convexhull(Point2D):
    def __init__(self):
        super().__init__()
        self.__coordinate_list = []

    @property
    def coordinate_list(self):
        return self.__coordinate_list

    @coordinate_list.setter
    def coordinate_list(self, coordinate_list):
        self.__coordinate_list = coordinate_list

    def create_points(self,num):
        for x in range(0,401):
            for y in range(0,401):
                point = (x,y)
                self.__coordinate_list.append(point)
        self.__coordinate_list = random.sample(self.__coordinate_list,num)
        path = ".\\"
        dirs =  os.listdir(path)
        f = open("test.txt",'w')
        f.write('points'+'\n')
        for coordinate in self.__coordinate_list:
            f.writelines(str(coordinate[0])+'\t'+str(coordinate[1])+'\n')
        f.write('end'+'\n')
        f.close()
        return self.__coordinate_list
    
    def get_sorted_by_angle_group_between_points(self,num):
        angle_list = []
        sorted_point_list = []
        self.__coordinate_list.sort(key=lambda x: x[1])
        ref_start_point = self.__coordinate_list[0]
        sorted_point_list.append(ref_start_point)
        self.__coordinate_list.remove(ref_start_point)
        for i in range(len(self.__coordinate_list)):
            dx = self.__coordinate_list[i][1]-ref_start_point[0]
            dy = self.__coordinate_list[i][0]-ref_start_point[1]
            angle = math.degrees((math.atan(dx/dy)))
            if dx < 0.0:
                angle += 180.0
                angle_list.append(angle)
            elif dy < 0.0: 
                angle += 360.0
                angle_list.append(angle)
        group = list(zip(angle_list, self.__coordinate_list))
        group.sort(key=lambda  x: x[0])
        self.__coordinate_list =[self.__coordinate_list for angle_list,self.__coordinate_list in group]
        self.__coordinate_list.insert(0,ref_start_point)
        return self.__coordinate_list

    def cross_product_direction(self,a,b,c):
        """ cross_product_value > 0 (CW)
            cross_product_value < 0 (ccw)
            cross_product_value = 0 (Co-linear)
        """
        return (b[1] -a[1])*(c[0]-a[0]) - (b[0] -a[0])*(c[1]-a[1])

    def graham_scan(self):
        stack = [] 
        stack.append(self.__coordinate_list[0])
        stack.append(self.__coordinate_list[0])

        for i in (len(self.__coordinate_list)):
            

        return self.__coordinate_list

