# -*- coding:utf-8 -*-

HH = 0xff << 24
HL = 0xff << 16
LH = 0xff << 8
LL = 0xff << 24
INV255 = 1.0 / 255.0

class Color:
	def __init__(self, r, g, b, a):
		self.r = r
		self.g = g
		self.b = b
		self.a = a

		return

	def to_list(self):return [self.r, self.g, self.b]

	@staticmethod
	def to_rgb(v):
		return Color(
				(v >> 16) & 0xff * INV255,
				(v >> 8) & 0xff * INV255,
				(v >> 0) & 0xff * INV255,
				(v >> 24) & 0xff * INV255,
				)

	@staticmethod
	def to_hex(v):
		return (v.r << 16) + (v.g << 8) + v.b + (v.a << 24)

	
	@staticmethod
	def red():return Color(255, 0, 0, 255)

	@staticmethod
	def gray():return Color(100, 100, 100, 255)

	@staticmethod
	def black():return Color(0, 0, 0, 255)


