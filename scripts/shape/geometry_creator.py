# -*- coding:utf-8 -*-

from kmath.vector4 import Vector4
from kmath.vector2 import Vector2

from vertex import Vectex

class MeshData:
	def __init__(self, size_v, size_i):
		self.vertices = [Vectex(), ] * size_v
		self.indices = [0, ] * size_i

class GeometryCreator:
	# 指定宽(X方向)、高(Y方向)、深(Z方向)
	def create_cube(self, width, height, depth):
		mesh = MeshData(24, 36)

		halfW = width * 0.5
		halfH = height * 0.5
		halfD = height * 0.5

		# front
		mesh.vertices[0].pos = Vector4(-halfW, -halfH, -halfD,1.0)
		mesh.vertices[0].normal = Vector4(0.0, 0.0, -1.0)
		mesh.vertices[0].color = Vector4(1.0, 0.0, 0.0, 1.0)
		mesh.vertices[0].tex = Vector2(0.0, 1.0)
		mesh.vertices[1].pos = Vector4(-halfW, halfH, -halfD,1.0)
		mesh.vertices[1].normal = Vector4(0.0, 0.0, -1.0)
		mesh.vertices[1].color = Vector4(0.0, 0.0, 0.0, 1.0)
		mesh.vertices[1].tex = Vector2(0.0, 0.0)
		mesh.vertices[2].pos = Vector4(halfW, halfH, -halfD, 1.0)
		mesh.vertices[2].normal = Vector4(0.0, 0.0, -1.0)
		mesh.vertices[2].color = Vector4(1.0, 0.0, 0.0, 1.0)
		mesh.vertices[2].tex = Vector2(1.0, 0.0)
		mesh.vertices[3].pos = Vector4(halfW, -halfH, -halfD, 1.0)
		mesh.vertices[3].normal = Vector4(0.0, 0.0, -1.0)
		mesh.vertices[3].color = Vector4(0.0, 1.0, 0.0, 1.0)
		mesh.vertices[3].tex = Vector2(1.0, 1.0)
		
		# left
		mesh.vertices[4].pos = Vector4(-halfW, -halfH, halfD, 1.0)
		mesh.vertices[4].normal = Vector4(-1.0, 0.0, 0.0)
		mesh.vertices[4].color = Vector4(0.0, 0.0, 1.0, 1.0)
		mesh.vertices[4].tex = Vector2(0.0, 1.0)
		mesh.vertices[5].pos = Vector4(-halfW, halfH, halfD, 1.0)
		mesh.vertices[5].normal = Vector4(-1.0, 0.0, 0.0)
		mesh.vertices[5].color = Vector4(1.0, 1.0, 0.0, 1.0)
		mesh.vertices[5].tex = Vector2(0.0, 0.0)
		mesh.vertices[6].pos = Vector4(-halfW, halfH, -halfD, 1.0)
		mesh.vertices[6].normal = Vector4(-1.0, 0.0, 0.0)
		mesh.vertices[6].color = Vector4(0.0, 0.0, 0.0, 1.0)
		mesh.vertices[6].tex = Vector2(1.0, 0.0)
		mesh.vertices[7].pos = Vector4(-halfW, -halfH, -halfD, 1.0)
		mesh.vertices[7].normal = Vector4(-1.0, 0.0, 0.0)
		mesh.vertices[7].color = Vector4(1.0, 1.0, 1.0, 1.0)
		mesh.vertices[7].tex = Vector2(1.0, 1.0)
		
		# back
		mesh.vertices[8].pos = Vector4(halfW, -halfH, halfD, 1.0)
		mesh.vertices[8].normal = Vector4(0.0, 0.0, 1.0)
		mesh.vertices[8].color = Vector4(1.0, 0.0, 1.0, 1.0)
		mesh.vertices[8].tex = Vector2(0.0, 1.0)
		mesh.vertices[9].pos = Vector4(halfW, halfH, halfD, 1.0)
		mesh.vertices[9].normal = Vector4(0.0, 0.0, 1.0)
		mesh.vertices[9].color = Vector4(0.0, 1.0, 1.0, 1.0)
		mesh.vertices[9].tex = Vector2(0.0, 0.0)
		mesh.vertices[10].pos = Vector4(-halfW, halfH, halfD, 1.0)
		mesh.vertices[10].normal = Vector4(0.0, 0.0, 1.0)
		mesh.vertices[10].color = Vector4(1.0, 1.0, 0.0, 1.0)
		mesh.vertices[10].tex = Vector2(1.0, 0.0)
		mesh.vertices[11].pos = Vector4(-halfW, -halfH, halfD, 1.0)
		mesh.vertices[11].normal = Vector4(0.0, 0.0, 1.0)
		mesh.vertices[11].color = Vector4(0.0, 0.0, 1.0, 1.0)
		mesh.vertices[11].tex = Vector2(1.0, 1.0)
		
		# right
		mesh.vertices[12].pos = Vector4(halfW, -halfH, -halfD, 1.0)
		mesh.vertices[12].normal = Vector4(1.0, 0.0, 0.0)
		mesh.vertices[12].color = Vector4(0.0, 1.0, 0.0, 1.0)
		mesh.vertices[12].tex = Vector2(0.0, 1.0)
		mesh.vertices[13].pos = Vector4(halfW, halfH, -halfD, 1.0)
		mesh.vertices[13].normal = Vector4(1.0, 0.0, 0.0)
		mesh.vertices[13].color = Vector4(1.0, 0.0, 0.0, 1.0)
		mesh.vertices[13].tex = Vector2(0.0, 0.0)
		mesh.vertices[14].pos = Vector4(halfW, halfH, halfD, 1.0)
		mesh.vertices[14].normal = Vector4(1.0, 0.0, 0.0)
		mesh.vertices[14].color = Vector4(0.0, 1.0, 1.0, 1.0)
		mesh.vertices[14].tex = Vector2(1.0, 0.0)
		mesh.vertices[15].pos = Vector4(halfW, -halfH, halfD, 1.0)
		mesh.vertices[15].normal = Vector4(1.0, 0.0, 0.0)
		mesh.vertices[15].color = Vector4(1.0, 0.0, 1.0, 1.0)
		mesh.vertices[15].tex = Vector2(1.0, 1.0)
		
		# top
		mesh.vertices[16].pos = Vector4(-halfW, halfH, -halfD, 1.0)
		mesh.vertices[16].normal = Vector4(0.0, 1.0, 0.0)
		mesh.vertices[16].color = Vector4(0.0, 0.0, 0.0, 1.0)
		mesh.vertices[16].tex = Vector2(0.0, 1.0)
		mesh.vertices[17].pos = Vector4(-halfW, halfH, halfD, 1.0)
		mesh.vertices[17].normal = Vector4(0.0, 1.0, 0.0)
		mesh.vertices[17].color = Vector4(1.0, 1.0, 0.0, 1.0)
		mesh.vertices[17].tex = Vector2(0.0, 0.0)
		mesh.vertices[18].pos = Vector4(halfW, halfH, halfD, 1.0)
		mesh.vertices[18].normal = Vector4(0.0, 1.0, 0.0)
		mesh.vertices[18].color = Vector4(0.0, 1.0, 1.0, 1.0)
		mesh.vertices[18].tex = Vector2(1.0, 0.0)
		mesh.vertices[19].pos = Vector4(halfW, halfH, -halfD, 1.0)
		mesh.vertices[19].normal = Vector4(0.0, 1.0, 0.0)
		mesh.vertices[19].color = Vector4(1.0, 0.0, 0.0, 1.0)
		mesh.vertices[19].tex = Vector2(1.0, 1.0)
		
		# bottom
		mesh.vertices[20].pos = Vector4(-halfW, -halfH, halfD, 1.0)
		mesh.vertices[20].normal = Vector4(0.0, -1.0, 0.0)
		mesh.vertices[20].color = Vector4(0.0, 0.0, 1.0, 1.0)
		mesh.vertices[20].tex = Vector2(0.0, 1.0)
		mesh.vertices[21].pos = Vector4(-halfW, -halfH, -halfD, 1.0)
		mesh.vertices[21].normal = Vector4(0.0, -1.0, 0.0)
		mesh.vertices[21].color = Vector4(1.0, 1.0, 1.0, 1.0)
		mesh.vertices[21].tex = Vector2(0.0, 0.0)
		mesh.vertices[22].pos = Vector4(halfW, -halfH, -halfD, 1.0)
		mesh.vertices[22].normal = Vector4(0.0, -1.0, 0.0)
		mesh.vertices[22].color = Vector4(0.0, 1.0, 0.0, 1.0)
		mesh.vertices[22].tex = Vector2(1.0, 0.0)
		mesh.vertices[23].pos = Vector4(halfW, -halfH, halfD, 1.0)
		mesh.vertices[23].normal = Vector4(0.0, -1.0, 0.0)
		mesh.vertices[23].color = Vector4(1.0, 0.0, 1.0, 1.0)
		mesh.vertices[23].tex = Vector2(1.0, 1.0)

		# index
		mesh.indices[0] = 0
		mesh.indices[1] = 1
		mesh.indices[2] = 2
		mesh.indices[3] = 0
		mesh.indices[4] = 2
		mesh.indices[5] = 3

		mesh.indices[6] = 4
		mesh.indices[7] = 5
		mesh.indices[8] = 6
		mesh.indices[9] = 4
		mesh.indices[10] = 6
		mesh.indices[11] = 7

		mesh.indices[12] = 8
		mesh.indices[13] = 9
		mesh.indices[14] = 10
		mesh.indices[15] = 8
		mesh.indices[16] = 10
		mesh.indices[17] = 11

		mesh.indices[18] = 12
		mesh.indices[19] = 13
		mesh.indices[20] = 14
		mesh.indices[21] = 12
		mesh.indices[22] = 14
		mesh.indices[23] = 15

		mesh.indices[24] = 16
		mesh.indices[25] = 17
		mesh.indices[26] = 18
		mesh.indices[27] = 16
		mesh.indices[28] = 18
		mesh.indices[29] = 19

		mesh.indices[30] = 20
		mesh.indices[31] = 21
		mesh.indices[32] = 22
		mesh.indices[33] = 20
		mesh.indices[34] = 22
		mesh.indices[35] = 23

		return mesh


g_geometry_creator = GeometryCreator()

