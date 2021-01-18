import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QPen, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_graphicsview import Ui_GraphicsviewWindow
from convexhull import Convexhull
from filereader import Filereader

num = 11
class GraphicsviewWindow(QMainWindow,Ui_GraphicsviewWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        conv = Convexhull()
        conv.create_points(num)
        coordinate_system = self.make_coordinate_system()
        point_group = self. make_point_item(conv)
        convex_hull_line_group = self.make_convex_hull_line_item(conv)
        coordinate_system.addItem(point_group)
        coordinate_system.addItem(convex_hull_line_group)
        self.graphicsView.setScene(coordinate_system)

    def make_coordinate_system(self):
        scene = QGraphicsScene()
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)
        #좌표평면
        side = 20
        for i in range(20):
            for j in range(20):
                r = QtCore.QRectF(QtCore.QPointF(i*side, j*side), QtCore.QSizeF(side, side))
                scene.addRect(r, blackPen)
                origin_point_radius = 3
                center =200
                scene.addEllipse(center-origin_point_radius,center-origin_point_radius,origin_point_radius*2,origin_point_radius*2,redPen,blackBrush)
        return scene

    def make_point_item(self,conv):
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)
        random_point_group = QGraphicsItemGroup()
        file = Filereader() 
        conv.coordinate_list = file.getpoint()
        for i in range(num):
            radius = 2
            x,y = conv.coordinate_list[i]
            point_item = QGraphicsEllipseItem(x-radius,y-radius,radius*2,radius*2)
            random_point_group.addToGroup(point_item)
        return random_point_group

    def make_convex_hull_line_item(self,conv):
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)
        convex_hull_item_group = QGraphicsItemGroup()
        sorted_point_list = conv.get_sorted_by_angle_group_between_points(num)
        convex_hull_list = conv.graham_scan()
        for i in range(len(convex_hull_list)-1):
            start_point = convex_hull_list[i]
            end_point = convex_hull_list[i+1]
            print(f'start_point is {start_point}')
            print(f'end_point is {end_point}')
            convex_hull_item = QGraphicsLineItem(start_point[0],start_point[1],end_point[0],end_point[1])
            convex_hull_item_group.addToGroup(convex_hull_item)
            if i == (len(convex_hull_list)-2):
                start_point = convex_hull_list[i+1]
                end_point = convex_hull_list[0]
                print(f'start_point is {start_point}')
                print(f'end_point is {end_point}')
                convex_hull_item = QGraphicsLineItem(start_point[0],start_point[1],end_point[0],end_point[1])
                convex_hull_item_group.addToGroup(convex_hull_item)
        return convex_hull_item_group
