# -*- coding:utf-8 -*-

from vector4 import Vector4
import kmath

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

	def __mul__(self, v):
		if type(v) == int or type(v) == float:return Vector2(self.x * v, self.y * v)
		elif isinstance(v, Vector2):return Vector2(self.x * v.x, self.y * v.y)

	def __str__(self):
		return "(%f %f)" % (self.x, self.y, )

	@staticmethod
	def lerp(v1, v2, t):return Vector2(
			kmath.lerp(v1.x, v2.x, t),
			kmath.lerp(v1.y, v2.y, t)
			)

	def encode(self, rect):
		x_min, x_max, y_min, y_max = rect.x, rect.y, rect.z, rect.w

		c = INSIDE
		if self.x < x_min:c = c | LEFT
		elif self.x > x_max:c = c | RIGHT

		if self.y < y_min:c = c | BOTTOM
		elif self.y > y_max:c = c | TOP

		return c

