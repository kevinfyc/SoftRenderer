# -*- coding:utf-8 -*-


class Matrix:
	def __init__(self,
			m11=0, m12=0, m13=0, m14=0,
			m21=0, m22=0, m23=0, m24=0,
			m31=0, m32=0, m33=0, m34=0,
			m41=0, m42=0, m43=0, m44=0):

		self.m = [ [m11, m12, m13, m14], [m21, m22, m23, m24], [m31, m32, m33, m34], [m41, m42, m43, m44], ]


		return

	@property
	def m11(self):return self.m[0][0]
	@property
	def m12(self):return self.m[0][1]
	@property
	def m13(self):return self.m[0][2]
	@property
	def m14(self):return self.m[0][3]


	@property
	def m21(self):return self.m[1][0]
	@property
	def m22(self):return self.m[1][1]
	@property
	def m23(self):return self.m[1][2]
	@property
	def m24(self):return self.m[1][3]


	@property
	def m31(self):return self.m[2][0]
	@property
	def m32(self):return self.m[2][1]
	@property
	def m33(self):return self.m[2][2]
	@property
	def m34(self):return self.m[2][3]


	@property
	def m41(self):return self.m[3][0]
	@property
	def m42(self):return self.m[3][1]
	@property
	def m43(self):return self.m[3][2]
	@property
	def m44(self):return self.m[3][3]

	def get_v(self, i, k):return self.m[i][k]
	def set_v(self, i, k, v):self.m[i][k] = v

	def __eq__(self, v):
		if type(v) != Matrix:return False

		for i in xrange(4):
			for j in xrange(4):
				if abs(self.m[i][j] - v.m[i][j]) >= 0.000001:
					return False
		return True

	def __add__(self, v):
		return Matrix(
				self.m11 + v.m11, self.m12 + v.m12, self.m13 + v.m13, self.m14 + v.m14,
				self.m21 + v.m21, self.m22 + v.m22, self.m23 + v.m23, self.m24 + v.m24,
				self.m31 + v.m31, self.m32 + v.m32, self.m33 + v.m33, self.m34 + v.m34,
				self.m41 + v.m41, self.m42 + v.m42, self.m43 + v.m43, self.m44 + v.m44
				)

	def __sub__(self, v):
		return Matrix(
				self.m11 - v.m11, self.m12 - v.m12, self.m13 - v.m13, self.m14 - v.m14,
				self.m21 - v.m21, self.m22 - v.m22, self.m23 - v.m23, self.m24 - v.m24,
				self.m31 - v.m31, self.m32 - v.m32, self.m33 - v.m33, self.m34 - v.m34,
				self.m41 - v.m41, self.m42 - v.m42, self.m43 - v.m43, self.m44 - v.m44
				)

	def __mul__(self, v):
		mat = Matrix()

		for i in xrange(4):
			for j in xrange(4):
				mat.set_v(j, i, 
						self.m[j][0] * v.m[0][i] + 
						self.m[j][1] * v.m[1][i] + 
						self.m[j][2] * v.m[2][i] + 
						self.m[j][3] * v.m[3][i])

		return mat

	def identity(self):
		self.m11, self.m12, self.m13, self.m14 = 1, 0, 0, 0
		self.m21, self.m22, self.m23, self.m24 = 0, 1, 0, 0
		self.m31, self.m32, self.m33, self.m34 = 0, 0, 1, 0
		self.m41, self.m42, self.m43, self.m44 = 0, 0, 0, 1

		return

	def set_zero(self):
		self.m11, self.m12, self.m13, self.m14 = 0, 0, 0, 0
		self.m21, self.m22, self.m23, self.m24 = 0, 0, 0, 0
		self.m31, self.m32, self.m33, self.m34 = 0, 0, 0, 0
		self.m41, self.m42, self.m43, self.m44 = 0, 0, 0, 0

		return

	def __str__(self):
		return "%f, %f, %f, %f\n%f, %f, %f, %f\n%f, %f, %f, %f\n%f, %f, %f, %f\n" % (
			self.m11, self.m12, self.m13, self.m14,
			self.m21, self.m22, self.m23, self.m24,
			self.m31, self.m32, self.m33, self.m34,
			self.m41, self.m42, self.m43, self.m44)
