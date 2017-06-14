# -*- coding:utf-8 -*-

import math

class Matrix:
	def __init__(self,
			m11=0, m12=0, m13=0, m14=0,
			m21=0, m22=0, m23=0, m24=0,
			m31=0, m32=0, m33=0, m34=0,
			m41=0, m42=0, m43=0, m44=0):

		self.m = [ [m11, m12, m13, m14], [m21, m22, m23, m24], [m31, m32, m33, m34], [m41, m42, m43, m44], ]


		return

	@property
	def m11(self):return self.get_v(0, 0)
	@property
	def m12(self):return self.get_v(0, 1)
	@property
	def m13(self):return self.get_v(0, 2)
	@property
	def m14(self):return self.get_v(0, 3)


	@property
	def m21(self):return self.get_v(1, 0)
	@property
	def m22(self):return self.get_v(1, 1)
	@property
	def m23(self):return self.get_v(1, 2)
	@property
	def m24(self):return self.get_v(1, 3)


	@property
	def m31(self):return self.get_v(2, 0)
	@property
	def m32(self):return self.get_v(2, 1)
	@property
	def m33(self):return self.get_v(2, 2)
	@property
	def m34(self):return self.get_v(2, 3)


	@property
	def m41(self):return self.get_v(3, 0)
	@property
	def m42(self):return self.get_v(3, 1)
	@property
	def m43(self):return self.get_v(3, 2)
	@property
	def m44(self):return self.get_v(3, 3)

	def get_v(self, i, k):return self.m[i][k]
	def set_v(self, i, k, v):self.m[i][k] = v

	def __eq__(self, v):
		if not isinstance(v, Matrix):return False

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
		mat = Matrix(
				self.m11 * v.m11 + self.m12 * v.m21 + self.m13 * v.m31 + self.m14 * v.m41,
				self.m11 * v.m12 + self.m12 * v.m22 + self.m13 * v.m33 + self.m14 * v.m42,
				self.m11 * v.m13 + self.m12 * v.m23 + self.m13 * v.m33 + self.m14 * v.m43,
				self.m11 * v.m14 + self.m12 * v.m24 + self.m13 * v.m34 + self.m14 * v.m44,

				self.m21 * v.m11 + self.m22 * v.m21 + self.m23 * v.m31 + self.m24 * v.m41,
				self.m21 * v.m12 + self.m22 * v.m22 + self.m23 * v.m33 + self.m24 * v.m42,
				self.m21 * v.m13 + self.m22 * v.m23 + self.m23 * v.m33 + self.m24 * v.m43,
				self.m21 * v.m14 + self.m22 * v.m24 + self.m23 * v.m34 + self.m24 * v.m44,
				
				self.m31 * v.m11 + self.m32 * v.m21 + self.m33 * v.m31 + self.m34 * v.m41,
				self.m31 * v.m12 + self.m32 * v.m22 + self.m33 * v.m33 + self.m34 * v.m42,
				self.m31 * v.m13 + self.m32 * v.m23 + self.m33 * v.m33 + self.m34 * v.m43,
				self.m31 * v.m14 + self.m32 * v.m24 + self.m33 * v.m34 + self.m34 * v.m44,
				
				self.m41 * v.m11 + self.m42 * v.m21 + self.m43 * v.m31 + self.m44 * v.m41,
				self.m41 * v.m12 + self.m42 * v.m22 + self.m43 * v.m33 + self.m44 * v.m42,
				self.m41 * v.m13 + self.m42 * v.m23 + self.m43 * v.m33 + self.m44 * v.m43,
				self.m41 * v.m14 + self.m42 * v.m24 + self.m43 * v.m34 + self.m44 * v.m44,
				)
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

	# view 矩阵
	@staticmethod
	def matrix_look_at_lh(eyePos, lookAt, up):
		zaxis = lookAt - eyePos
		zaxis.normalize()

		xaxis = up.cross(zaxis).normalize()

		yaxis = zaxis.cross(xaxis)

		return Matrix(
				xaxis.x, yaxis.x, zaxis.x, 0,
				xaxis.y, yaxis.y, zaxis.y, 0,
				xaxis.z, yaxis.z, zaxis.z, 0,
				-xaxis.dot(eyePos), -yaxis.dot(eyePos), -zaxis.dot(eyePos), 1
				)

	@staticmethod
	def perspective_fov_lh(fov, aspect, near, far):
		height = math.cos(fov*0.5) / math.sin(fov*0.5)

		mat = Matrix(
				height / aspect, 0, 0, 0,
				0, height, 0, 0,
				0, 0, far / (far - near), 1,
				0, 0,  near * far / float(near - far), 0
				)
		return mat

	def transpose(self):
		return Matrix(
				self.m11, self.m21, self.m31, self.m41,
				self.m12, self.m22, self.m32, self.m42,
				self.m13, self.m23, self.m33, self.m43,
				self.m14, self.m24, self.m34, self.m44
				)

	def det(self):
		ret = 0

		ret += self.m[0][0] * (self.m[1][1] * self.m[2][2] - self.m[1][2] * self.m[2][1])
		ret -= self.m[0][1] * (self.m[1][0] * self.m[2][2] - self.m[1][2] * self.m[2][0])
		ret += self.m[0][2] * (self.m[1][0] * self.m[2][1] - self.m[1][1] * self.m[2][0])

		return ret

	def inverse(self):
		matrix = Matrix(
				self.m11, self.m12, self.m13, self.m14,
                self.m21, self.m22, self.m23, self.m24,
                self.m31, self.m32, self.m33, self.m34,
                self.m41, self.m42, self.m43, self.m44
				)

		determinant = matrix.det()

		if determinant == 0:
			return False

		rcp = 1 / determinant
		self.m[0][0] = matrix.m[1][1] * matrix.m[2][2] - matrix.m[1][2] * matrix.m[2][1]
		self.m[0][1] = matrix.m[0][2] * matrix.m[2][1] - matrix.m[0][1] * matrix.m[2][2]
		self.m[0][2] = matrix.m[0][1] * matrix.m[1][2] - matrix.m[0][2] * matrix.m[1][1]
		self.m[1][0] = matrix.m[1][2] * matrix.m[2][0] - matrix.m[1][0] * matrix.m[2][2]
		self.m[1][1] = matrix.m[0][0] * matrix.m[2][2] - matrix.m[0][2] * matrix.m[2][0]
		self.m[1][2] = matrix.m[0][2] * matrix.m[1][0] - matrix.m[0][0] * matrix.m[1][2]
		self.m[2][0] = matrix.m[1][0] * matrix.m[2][1] - matrix.m[1][1] * matrix.m[2][0]
		self.m[2][1] = matrix.m[0][1] * matrix.m[2][0] - matrix.m[0][0] * matrix.m[2][1]
		self.m[2][2] = matrix.m[0][0] * matrix.m[1][1] - matrix.m[0][1] * matrix.m[1][0]

		self.m[0][0] *= rcp
		self.m[0][1] *= rcp
		self.m[0][2] *= rcp

		self.m[1][0] *= rcp
		self.m[1][1] *= rcp
		self.m[1][2] *= rcp

		self.m[2][0] *= rcp
		self.m[2][1] *= rcp
		self.m[2][2] *= rcp

		self.m[3][0] = -(matrix.m[3][0] * self.m[0][0] + matrix.m[3][1] * self.m[1][0] + matrix.m[3][2] * self.m[2][0])
		self.m[3][1] = -(matrix.m[3][0] * self.m[0][1] + matrix.m[3][1] * self.m[1][1] + matrix.m[3][2] * self.m[2][1])
		self.m[3][2] = -(matrix.m[3][0] * self.m[0][2] + matrix.m[3][1] * self.m[1][2] + matrix.m[3][2] * self.m[2][2])

		if determinant == 0:
			self.identity()

		return True

	@staticmethod
	def screen_transform(width, height):
		return Matrix(
				width * 0.5, 0, 0, 0,
				0, height * 0.5, 0, 0,
				0, 0, 1, 0,
				width * 0.5, height * 0.5, 0, 1
				)

	def __str__(self):
		return "%f, %f, %f, %f\n%f, %f, %f, %f\n%f, %f, %f, %f\n%f, %f, %f, %f\n" % (
			self.m11, self.m12, self.m13, self.m14,
			self.m21, self.m22, self.m23, self.m24,
			self.m31, self.m32, self.m33, self.m34,
			self.m41, self.m42, self.m43, self.m44)
