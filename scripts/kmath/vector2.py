# -*- coding:utf-8 -*-

from vector4 import Vector4

INSIDE = 0  #0000
LEFT = 1    #0001
RIGHT = 2   #0010
BOTTOM = 4  #0100
TOP = 8     #1000

class Vector2:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

		return


	def encode(self, rect):
		x_min, x_max, y_min, y_max = rect.x, rect.y, rect.z, rect.w

		c = INSIDE
		if self.x < x_min:c = c | LEFT
		elif self.x > x_max:c = c | RIGHT

		if self.y < y_min:c = c | BOTTOM
		elif self.y > y_max:c = c | TOP

		return c

