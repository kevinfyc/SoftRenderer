# -*- coding:utf-8 -*-

from kmath.vector4 import Vector4
from kmath.vector2 import Vector2

from color import Color

from vertex import VectexIn

class MeshData:
	def __init__(self):
		self.vertices = []
		self.indices = []

class GeometryCreator:
	# 指定宽(X方向)、高(Y方向)、深(Z方向)
	def create_cube(self, width, height, depth):
		mesh = MeshData()

		halfW = width * 0.5
		halfH = height * 0.5
		halfD = height * 0.5

		# front
		v0 = VectexIn()
		v0.pos = Vector4(-halfW, -halfH, -halfD,1.0)
		v0.normal = Vector4(0.0, 0.0, -1.0)
		v0.color = Color(1.0, 0.0, 0.0, 1.0)
		v0.tex = Vector2(0.0, 1.0)
		v1 = VectexIn()
		v1.pos = Vector4(-halfW, halfH, -halfD,1.0)
		v1.normal = Vector4(0.0, 0.0, -1.0)
		v1.color = Color(0.0, 0.0, 0.0, 1.0)
		v1.tex = Vector2(0.0, 0.0)
		v2 = VectexIn()
		v2.pos = Vector4(halfW, halfH, -halfD, 1.0)
		v2.normal = Vector4(0.0, 0.0, -1.0)
		v2.color = Color(1.0, 0.0, 0.0, 1.0)
		v2.tex = Vector2(1.0, 0.0)
		v3 = VectexIn()
		v3.pos = Vector4(halfW, -halfH, -halfD, 1.0)
		v3.normal = Vector4(0.0, 0.0, -1.0)
		v3.color = Color(0.0, 1.0, 0.0, 1.0)
		v3.tex = Vector2(1.0, 1.0)
		
		# left
		v4 = VectexIn()
		v4.pos = Vector4(-halfW, -halfH, halfD, 1.0)
		v4.normal = Vector4(-1.0, 0.0, 0.0)
		v4.color = Color(0.0, 0.0, 1.0, 1.0)
		v4.tex = Vector2(0.0, 1.0)
		v5 = VectexIn()
		v5.pos = Vector4(-halfW, halfH, halfD, 1.0)
		v5.normal = Vector4(-1.0, 0.0, 0.0)
		v5.color = Color(1.0, 1.0, 0.0, 1.0)
		v5.tex = Vector2(0.0, 0.0)
		v6 = VectexIn()
		v6.pos = Vector4(-halfW, halfH, -halfD, 1.0)
		v6.normal = Vector4(-1.0, 0.0, 0.0)
		v6.color = Color(0.0, 0.0, 0.0, 1.0)
		v6.tex = Vector2(1.0, 0.0)
		v7 = VectexIn()
		v7.pos = Vector4(-halfW, -halfH, -halfD, 1.0)
		v7.normal = Vector4(-1.0, 0.0, 0.0)
		v7.color = Color(1.0, 1.0, 1.0, 1.0)
		v7.tex = Vector2(1.0, 1.0)
		
		# back
		v8 = VectexIn()
		v8.pos = Vector4(halfW, -halfH, halfD, 1.0)
		v8.normal = Vector4(0.0, 0.0, 1.0)
		v8.color = Color(1.0, 0.0, 1.0, 1.0)
		v8.tex = Vector2(0.0, 1.0)
		v9 = VectexIn()
		v9.pos = Vector4(halfW, halfH, halfD, 1.0)
		v9.normal = Vector4(0.0, 0.0, 1.0)
		v9.color = Color(0.0, 1.0, 1.0, 1.0)
		v9.tex = Vector2(0.0, 0.0)
		v10 = VectexIn()
		v10.pos = Vector4(-halfW, halfH, halfD, 1.0)
		v10.normal = Vector4(0.0, 0.0, 1.0)
		v10.color = Color(1.0, 1.0, 0.0, 1.0)
		v10.tex = Vector2(1.0, 0.0)
		v11 = VectexIn()
		v11.pos = Vector4(-halfW, -halfH, halfD, 1.0)
		v11.normal = Vector4(0.0, 0.0, 1.0)
		v11.color = Color(0.0, 0.0, 1.0, 1.0)
		v11.tex = Vector2(1.0, 1.0)
		
		# right
		v12 = VectexIn()
		v12.pos = Vector4(halfW, -halfH, -halfD, 1.0)
		v12.normal = Vector4(1.0, 0.0, 0.0)
		v12.color = Color(0.0, 1.0, 0.0, 1.0)
		v12.tex = Vector2(0.0, 1.0)
		v13 = VectexIn()
		v13.pos = Vector4(halfW, halfH, -halfD, 1.0)
		v13.normal = Vector4(1.0, 0.0, 0.0)
		v13.color = Color(1.0, 0.0, 0.0, 1.0)
		v13.tex = Vector2(0.0, 0.0)
		v14 = VectexIn()
		v14.pos = Vector4(halfW, halfH, halfD, 1.0)
		v14.normal = Vector4(1.0, 0.0, 0.0)
		v14.color = Color(0.0, 1.0, 1.0, 1.0)
		v14.tex = Vector2(1.0, 0.0)
		v15 = VectexIn()
		v15.pos = Vector4(halfW, -halfH, halfD, 1.0)
		v15.normal = Vector4(1.0, 0.0, 0.0)
		v15.color = Color(1.0, 0.0, 1.0, 1.0)
		v15.tex = Vector2(1.0, 1.0)
		
		# top
		v16 = VectexIn()
		v16.pos = Vector4(-halfW, halfH, -halfD, 1.0)
		v16.normal = Vector4(0.0, 1.0, 0.0)
		v16.color = Color(0.0, 0.0, 0.0, 1.0)
		v16.tex = Vector2(0.0, 1.0)
		v17 = VectexIn()
		v17.pos = Vector4(-halfW, halfH, halfD, 1.0)
		v17.normal = Vector4(0.0, 1.0, 0.0)
		v17.color = Color(1.0, 1.0, 0.0, 1.0)
		v17.tex = Vector2(0.0, 0.0)
		v18 = VectexIn()
		v18.pos = Vector4(halfW, halfH, halfD, 1.0)
		v18.normal = Vector4(0.0, 1.0, 0.0)
		v18.color = Color(0.0, 1.0, 1.0, 1.0)
		v18.tex = Vector2(1.0, 0.0)
		v19 = VectexIn()
		v19.pos = Vector4(halfW, halfH, -halfD, 1.0)
		v19.normal = Vector4(0.0, 1.0, 0.0)
		v19.color = Color(1.0, 0.0, 0.0, 1.0)
		v19.tex = Vector2(1.0, 1.0)
		
		# bottom
		v20 = VectexIn()
		v20.pos = Vector4(-halfW, -halfH, halfD, 1.0)
		v20.normal = Vector4(0.0, -1.0, 0.0)
		v20.color = Color(0.0, 0.0, 1.0, 1.0)
		v20.tex = Vector2(0.0, 1.0)
		v21 = VectexIn()
		v21.pos = Vector4(-halfW, -halfH, -halfD, 1.0)
		v21.normal = Vector4(0.0, -1.0, 0.0)
		v21.color = Color(1.0, 1.0, 1.0, 1.0)
		v21.tex = Vector2(0.0, 0.0)
		v22 = VectexIn()
		v22.pos = Vector4(halfW, -halfH, -halfD, 1.0)
		v22.normal = Vector4(0.0, -1.0, 0.0)
		v22.color = Color(0.0, 1.0, 0.0, 1.0)
		v22.tex = Vector2(1.0, 0.0)
		v23 = VectexIn()
		v23.pos = Vector4(halfW, -halfH, halfD, 1.0)
		v23.normal = Vector4(0.0, -1.0, 0.0)
		v23.color = Color(1.0, 0.0, 1.0, 1.0)
		v23.tex = Vector2(1.0, 1.0)

		mesh.vertices = [
				v0,  v1,  v2,  v3,
				v4,  v5,  v6,  v7,
				v8,  v9,  v10, v11,
				v12, v13, v14, v15,
				v16, v17, v18, v19,
				v20, v21, v22, v23,
				]

		# index
		mesh.indices = [
				 0,  1,  2,  0,  2,  3,
				 4,  5,  6,  4,  6,  7,
				 8,  9, 10,  8, 10, 11,
				12, 13, 14, 12, 14, 15,
				16, 17, 18, 16, 18, 19,
				20, 21, 22, 20, 22, 23,
				]

		return mesh


g_geometry_creator = GeometryCreator()

