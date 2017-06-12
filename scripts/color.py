# -*- coding:utf-8 -*-

class Color:
	def __init__(self, r, g, b, a):
		self.r = r
		self.g = g
		self.b = b
		self.a = a

		return

	def to_list(self):return [self.r, self.g, self.b]
	
	@staticmethod
	def red():return Color(255, 0, 0, 255)

	@staticmethod
	def gray():return Color(100, 100, 100, 255)

	@staticmethod
	def black():return Color(0, 0, 0, 255)


