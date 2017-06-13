# -*- coding:utf-8 -*-

from kmath.vector4 import Vector4
from kmath.vector2 import Vector2

from color import Color

class Vectex:
	def __init__(self, pos=Vector4(), color=Color.black(), tex=Vector2(), normal=Vector4()):
		self.pos = pos
		self.color = color
		self.tex = tex
		self.normal = normal
