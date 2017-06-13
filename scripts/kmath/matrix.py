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
		mat = Matrix()
		mat.set_zero()

		height = math.cos(fov*0.5) / math.sin(fov*0.5)
		mat.set_v(0, 0, height / aspect)
		mat.set_v(1, 1, height)
		mat.set_v(2, 2, far / (far - near))
		mat.set_v(2, 3, 1)
		mat.set_v(3, 2, near * far / (near - far))
		return mat

	@staticmethod
	def transpose(mat):
		return Matrix(
				mat.m11, mat.m21, mat.m31, mat.m41,
				mat.m12, mat.m22, mat.m32, mat.m42,
				mat.m13, mat.m23, mat.m33, mat.m43,
				mat.m14, mat.m24, mat.m34, mat.m44
				)

	@staticmethod
	def det(mat):
		ret = \
			mat.m11*mat.m22*mat.m33*mat.m44 - mat.m11*mat.m22*mat.m34*mat.m43 -\
			mat.m11*mat.m23*mat.m32*mat.m44 + mat.m11*mat.m23*mat.m34*mat.m42 +\
			mat.m11*mat.m24*mat.m32*mat.m43 - mat.m11*mat.m24*mat.m33*mat.m42 -\
			mat.m12*mat.m21*mat.m33*mat.m44 + mat.m12*mat.m21*mat.m34*mat.m43 +\
			mat.m12*mat.m23*mat.m31*mat.m44 - mat.m12*mat.m23*mat.m34*mat.m41 -\
			mat.m12*mat.m24*mat.m31*mat.m43 + mat.m12*mat.m24*mat.m33*mat.m41 +\
			mat.m13*mat.m21*mat.m32*mat.m44 - mat.m13*mat.m21*mat.m34*mat.m42 -\
			mat.m13*mat.m22*mat.m31*mat.m44 + mat.m13*mat.m22*mat.m34*mat.m41 +\
			mat.m13*mat.m24*mat.m31*mat.m42 - mat.m13*mat.m24*mat.m32*mat.m41 -\
			mat.m14*mat.m21*mat.m32*mat.m43 + mat.m14*mat.m21*mat.m33*mat.m42 +\
			mat.m14*mat.m22*mat.m31*mat.m43 - mat.m14*mat.m22*mat.m33*mat.m41 -\
			mat.m14*mat.m23*mat.m31*mat.m42 + mat.m14*mat.m23*mat.m32*mat.m41

		return ret

	@staticmethod
	def adj_elem(a1, a2, a3, b1, b2, b3, c1, c2, c3):return a1*(b2*c3 - c2*b3) - a2*(b1*c3 - c1*b3) + a3*(b1*c2 - c1*b2)

	@staticmethod
	def adj(mat):
		a1 = Matrix.adj_elem(mat.m22, mat.m23, mat.m24, mat.m32, mat.m33, mat.m34, mat.m42, mat.m43, mat.m44)
		a2 = Matrix.adj_elem(mat.m21, mat.m23, mat.m24, mat.m31, mat.m33, mat.m34, mat.m41, mat.m43, mat.m44)
		a3 = Matrix.adj_elem(mat.m21, mat.m22, mat.m24, mat.m31, mat.m32, mat.m34, mat.m41, mat.m42, mat.m44)
		a4 = Matrix.adj_elem(mat.m21, mat.m22, mat.m23, mat.m31, mat.m32, mat.m33, mat.m41, mat.m42, mat.m43)
		b1 = Matrix.adj_elem(mat.m12, mat.m13, mat.m14, mat.m32, mat.m33, mat.m34, mat.m42, mat.m43, mat.m44)
		b2 = Matrix.adj_elem(mat.m11, mat.m13, mat.m14, mat.m31, mat.m33, mat.m34, mat.m41, mat.m43, mat.m44)
		b3 = Matrix.adj_elem(mat.m11, mat.m12, mat.m14, mat.m31, mat.m32, mat.m34, mat.m41, mat.m42, mat.m44)
		b4 = Matrix.adj_elem(mat.m11, mat.m12, mat.m13, mat.m31, mat.m32, mat.m33, mat.m41, mat.m42, mat.m43)
		c1 = Matrix.adj_elem(mat.m12, mat.m13, mat.m14, mat.m22, mat.m23, mat.m24, mat.m42, mat.m43, mat.m44)
		c2 = Matrix.adj_elem(mat.m11, mat.m13, mat.m14, mat.m21, mat.m23, mat.m24, mat.m41, mat.m43, mat.m44)
		c3 = Matrix.adj_elem(mat.m11, mat.m12, mat.m14, mat.m21, mat.m22, mat.m24, mat.m41, mat.m42, mat.m44)
		c4 = Matrix.adj_elem(mat.m11, mat.m12, mat.m13, mat.m21, mat.m22, mat.m23, mat.m41, mat.m42, mat.m43)
		d1 = Matrix.adj_elem(mat.m12, mat.m13, mat.m14, mat.m22, mat.m23, mat.m24, mat.m32, mat.m33, mat.m34)
		d2 = Matrix.adj_elem(mat.m11, mat.m13, mat.m14, mat.m21, mat.m23, mat.m24, mat.m31, mat.m33, mat.m34)
		d3 = Matrix.adj_elem(mat.m11, mat.m12, mat.m14, mat.m21, mat.m22, mat.m24, mat.m31, mat.m32, mat.m34)
		d4 = Matrix.adj_elem(mat.m11, mat.m12, mat.m13, mat.m21, mat.m22, mat.m23, mat.m31, mat.m32, mat.m33)

		result = Matrix(
			a1, -a2, a3, -a4,
			-b1, b2, -b3, b4,
			c1, -c2, c3, -c4,
			-d1, d2, -d3, d4
		)
		return Matrix.transpose(result)

	@staticmethod
	def inverse(mat):
		det = abs(Matrix.det(mat))
		adj = Matrix.adj(mat)
		inv = Matrix()
		for i in xrange(4):
			for j in xrange(4):
				inv.set_v(i, j, adj.get_v(i, j) / det)

		return inv

	def __str__(self):
		return "%f, %f, %f, %f\n%f, %f, %f, %f\n%f, %f, %f, %f\n%f, %f, %f, %f\n" % (
			self.m11, self.m12, self.m13, self.m14,
			self.m21, self.m22, self.m23, self.m24,
			self.m31, self.m32, self.m33, self.m34,
			self.m41, self.m42, self.m43, self.m44)
