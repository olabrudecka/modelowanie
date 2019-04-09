from cs50 import get_float
from math import *
from enum import *
#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
#3 Test your solutions



def checkFigure(fig):
        fig[0] = fig[0].lower()
        return fig

def checkValues(fig):
    if fig[1] <= 0:
        print('Wrong number')
        return False
    elif len(fig) > 2:
        if fig[1] <= 0:
            print('Wrong number')
            return False
    return True


def countField(fig):
    field = 0
    if fig[0] == 'circle':
        field = pi * (fig[1] ** 2)
    elif fig[0] == 'rectangle':
        field = fig[1] * fig[2]
    elif fig[0] == 'triangle':
        field = (fig[1] * fig[2]) / 2
    elif fig[0] == 'rhombus':
        field = (fig[1] * fig[2]) / 2
    return field



def compareFields(fig1,fig2):
        fig = checkFigure(fig1)
        fig = checkFigure(fig2)
        field1 = countField(fig1)
        field2 = countField(fig2)
        print(field2)
        if field1 !=0 and field2 != 0:
            if field1 > field2 and checkValues(fig1) == True and checkValues(fig2) == True:
                print('First figure ' + fig1[0] + ' has larger field')
            elif field1 < field2 and checkValues(fig1) == True and checkValues(fig2) == True:
                print('Second figure ' + fig2[0] + ' has larger field')
            elif field1 == field2 and checkValues(fig1) == True and checkValues(fig2) == True:
                print('Fields of both figures are equal')
        else:
            print('Wrong figure')


compareFields(['Circle', 1],['Triangle', 2, 10])




























# class figures():
#
#     def __init__(self, fig1, fig2):
#         self.fig = 0
#         self.field = 0
#
#     def getFigure(self):
#         a = 0
#         while a == 0:
#             fig = input('Write "c" for circle, "r" for rectangle, "t" for triangle or "rh" for rhombus: ')
#             if (fig == 'c') or (fig == 'r') or (fig == 't') or (fig == 'rh'):
#                 a = 1
#             else:
#                 print('Wrong type')
#         return fig
#
#     def countField(self):
#         fig = self.fig
#         field = self.field
#         if fig == 'Circle':
#             radius = get_float('Give radius: ')
#             field = pi * (radius ** 2)
#         elif fig == 'Rectangle':
#             x = get_float('Give first parameter: ')
#             y = get_float('Give second parameter: ')
#             field = x * y
#         elif fig == 'Triangle':
#             x = get_float('Give base: ')
#             y = get_float('Give height: ')
#             field = (x * y) / 2
#         elif fig == 'Rhombus':
#             x = get_float('Give first diagonal: ')
#             y = get_float('Give second diagonal: ')
#             field = (x * y) / 2
#         self.field = field
