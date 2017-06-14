# -*- coding:utf-8 -*-

from kmath.matrix import Matrix

from vertex import VectexIn, VectexOut

class Shader:
	def vs(self, v):pass
	def ps(self, v):pass

class CubeShader:
	def __init__(self):
		self.wvp = Matrix()
		self.wvp.identity()

		self.world = Matrix()
		self.world.identity()
		
		self.worldInvTranspose = Matrix()
		self.worldInvTranspose.identity()
		
		self.texture = None

		return

	def set_wvp(self, mat):
		self.wvp = mat
		return

	def set_texture(self, texture):
		self.texture = texture
		return

	def set_world(self, world):
		self.world = world
		return

	def set_world_inv_transpose(self, mat):
		self.worldInvTranspose = mat
		return

	def vs(self, v):
		out = VectexOut()
		out.pos_proj = v.pos * self.wvp

		out.pos_world = v.pos * self.world

		out.color = v.color
		out.tex = v.tex

		return out

	def ps(self, v):
		return v.color

