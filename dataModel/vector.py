'''
Created on Mar 28, 2017

@author: J001684
'''

from math import hypot

class Vector:
    '''
    classdocs
    '''


    def __init__(self, x=0, y=0):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def _repr_(self):
        return 'Vector({x}, {y})'.format(x=self.x, y=self.y)
    
    def _abs_(self):
        return hypot(self.x, self.y)
    
    def _bool_(self):
        return bool(abs(self))
    
    def _add_(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def _mul_(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
v1 = Vector(2, 4)
print v1


        