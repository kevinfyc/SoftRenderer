# -*- coding:utf-8 -*-

from kmath import kmath

HH = 0xff << 24
HL = 0xff << 16
LH = 0xff << 8
LL = 0xff << 24
INV255 = 1.0 / 255.0

class Color:
	def __init__(self, r, g, b, a):
		if r > 1:r = 1
		if g > 1:g = 1
		if b > 1:b = 1
		if a > 1:a = 1

		self.r = r
		self.g = g
		self.b = b
		self.a = a

		return

	def to_list(self):return [self.r*255, self.g*255, self.b*255]

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
		return (int(v.r * 255) << 16) + (int(v.g * 255) << 8) + int(v.b*255) + (int(v.a * 255) << 24)
	
	@staticmethod
	def red():return Color(1, 0, 0, 1)

	@staticmethod
	def gray():return Color(0.2, 0.2, 0.2, 1)

	@staticmethod
	def black():return Color(0, 0, 0, 1)

	@staticmethod
	def lerp(c1, c2, t):return Color(
		kmath.lerp(c1.r, c2.r, t),
		kmath.lerp(c1.g, c2.g, t),
		kmath.lerp(c1.b, c2.b, t),
		kmath.lerp(c1.a, c2.a, t),	
		)

	def __mul__(self, v):
		if isinstance(v, Color):return Color(self.r * v.r, self.g * v.g, self.b * v.b, self.a * v.a)
		elif type(v) == float or type(v) == int:return Color(self.r * v, self.g * v, self.b * v, self.a * v)

	def __str__(self):
		return "(%f, %f, %f, %f)" % (self.r, self.g, self.b, self.a, )


