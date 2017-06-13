# -*- coding:utf-8 -*-

import math

from matrix import Matrix

class Vector4:
	def __init__(self, x=0, y=0, z=0, w=0):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

		return

	def length(self):
		sq = self.x * self.x + self.y * self.y + self.z * self.z
		return math.sqrt(sq)

	def normalize(self):
		l = length()
		if l != 0.0:
			inv = 1 / l
			x *= inv
			y *= inv
			z *= inv

		return self

	def dot(self, v):
		return self.x * v.x + self.y * v.y + self.z * v.z

	def cross(self, v):
		m1 = self.y * v.z - self.z * v.y
		m2 = self.z * v.x - self.x * v.z
		m3 = self.x * v.y - self.y * v.x
		return Vector4(m1, m2, m3, 0.0)

	def __eq__(self, v):
		if type(v) != Vector4:return False

		return  abs(self.x - v.x) <= 0.000001 and \
				abs(self.y - v.y) <= 0.000001 and \
				abs(self.z - v.z) <= 0.000001 and \
				abs(self.w - v.w) <= 0.000001

	def __mul__(self, v):
		if type(v) == Vector4:
			return Vector4(self.x * v.x, self.y * v.y, self.z * v.z, self.w * v.w)
		elif type(v) == float or type(v) == int:
			return Vector4(self.x * v, self.y * v, self.z * v, self.w)
		elif type(v) == Matrix:
			return Vector4(
					self.x * v.m11 + self.y * v.m21 + self.z * v.m31 + self.w * v.m41,
					self.x * v.m12 + self.y * v.m22 + self.z * v.m32 + self.w * v.m42,
					self.x * v.m13 + self.y * v.m23 + self.z * v.m33 + self.w * v.m43,
					self.x * v.m14 + self.y * v.m24 + self.z * v.m34 + self.w * v.m44,
					)

	def __add__(self, v):return Vector4(self.x + v.x, self.y + v.y, self.z + v.z, 0)

	def __sub__(self, v):return Vector4(self.x - v.x, self.y - v.y, self.z - v.z, 0)

	def __neg__(self):return Vector4(-self.x, -self.y, -self.z, -self.w)
