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


def countField(fig):
    if fig == 'Circle':
        radius = get_float('Give radius: ')
        field = pi * (radius ** 2)
    elif fig == 'Rectangle':
        x = get_float('Give first parameter: ')
        y = get_float('Give second parameter: ')
        field = x * y
    elif fig == 'Triangle':
        x = get_float('Give base: ')
        y = get_float('Give height: ')
        field = (x * y) / 2
    elif fig == 'Rhombus':
        x = get_float('Give first diagonal: ')
        y = get_float('Give second diagonal: ')
        field = (x * y) / 2

    print('Field', field)
    return field

def getFigure():
    a = 0
    while a == 0:
        fig = input('Write Circle, Rectangle, Triangle or Rhombus: ')
        if (fig == 'Circle') or (fig == 'Rectangle') or (fig == 'Triangle') or (fig == 'Rhombus'):
            a = 1
        else:
            print('Wrong type')
    return fig

def compareFields(fig1,fig2):
    if fig1['field'] > fig2['field']:
        print('First figure '+ fig1['figure'] + ' has larger field')
    elif fig1['field'] < fig2['field']:
        print('Second figure '+ fig2['figure'] + ' has larger field')
    elif fig1['field'] == fig2['field']:
        print('Fields of both figures are equal')




#countField()

fig1 = {'figure': getFigure() }
fig1['field'] = countField(fig1['figure'])
fig2 = {'figure': getFigure() }
fig2['field'] = countField(fig2['figure'])

compareFields(fig1,fig2)

































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
