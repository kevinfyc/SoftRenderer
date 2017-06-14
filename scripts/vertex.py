# -*- coding:utf-8 -*-

from kmath.vector4 import Vector4
from kmath.vector2 import Vector2
from kmath import kmath

from color import Color

class VectexIn:
	def __init__(self, pos=Vector4(), color=Color.black(), tex=Vector2(), normal=Vector4()):
		self.pos = pos
		self.color = color
		self.tex = tex
		self.normal = normal

		return

	def __str__(self):
		return "pos: %s color: %s tex: %s normal: %s" % (self.pos, self.color, self.tex, self.normal, )

class VectexOut:
	def __init__(self, pos_world=Vector4(), pos_proj=Vector4(), tex=Vector2(), normal=Vector4(), color=Color.black(), oneDivZ=0):
		self.pos_world = pos_world
		self.pos_proj = pos_proj
		self.tex = tex
		self.normal = normal
		self.color = color
		self.oneDivZ = oneDivZ

		return

	def __str__(self):
		return "pos_world: %s\pos_proj: %s tex: %s normal: %s color: %s oneDivz: %s" % (self.pos_world, self.pos_proj, self.tex, self.normal, self.color, self.oneDivZ)

	@staticmethod
	def lerp(v1, v2, t):
		return VectexOut(
				Vector4.lerp(v1.pos_world, v2.pos_world, t),
				Vector4.lerp(v1.pos_proj, v2.pos_proj, t),
				Vector2.lerp(v1.tex, v2.tex, t),
				Vector4.lerp(v1.normal, v2.normal, t),
				Color.lerp(v1.color, v2.color, t),
				kmath.lerp(v1.oneDivZ, v2.oneDivZ, t),
				)
