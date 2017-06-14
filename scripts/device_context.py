# -*- coding:utf-8 -*-

from kmath.vector2 import Vector2
from kmath.vector4 import Vector4
from kmath import vector2
from kmath.matrix import Matrix
from kmath import kmath

from shader import Shader

from color import Color

from vertex import VectexOut

FM_WIREFRAME = 0 # 线框
FM_SOLIDE	 = 1 # 填充

FM_HO = (
	FM_WIREFRAME,
	FM_SOLIDE,
)

class DeviceContext:
	def __init__(self, device):
		self.device = device
		self.renderMode = FM_WIREFRAME

		self.vertex_buffer = []
		self.index_buffer = []

		self.shader = Shader()

		self.camera_pos = Vector4()

		return

	######################################################
	#
	######################################################
	def set_render_mode(self, mode):
		if mode not in FM_HO:return

		self.renderMode = mode

		return

	def set_vertex_buffer(self, vertex_buffer):
		self.vertex_buffer = vertex_buffer
		return

	def set_index_buffer(self, index_buffer):
		self.index_buffer = index_buffer
		return

	def set_camera_pos(self, pos):
		self.camera_pos = pos
		return

	def set_shader(self, shader):
		self.shader = shader
		return

	######################################################
	#
	######################################################
	def transform2proj(self, vertex):
		out = self.shader.vs(vertex)

		out.oneDivZ = 1 / out.pos_proj.w

		out.color *= out.oneDivZ

		out.normal *= out.oneDivZ

		out.tex *= out.oneDivZ

		return out

	def clip(self, v):
		if v.pos_proj.x >= -v.pos_proj.w and v.pos_proj.x <= v.pos_proj.w and\
			v.pos_proj.y >= -v.pos_proj.w and v.pos_proj.y <= v.pos_proj.w and\
			v.pos_proj.z >= 0 and v.pos_proj.z <= v.pos_proj.w:
			return True

		return False

	def cvv(self, v):
		v.pos_proj.x /= v.pos_proj.w
		v.pos_proj.y /= v.pos_proj.w
		v.pos_proj.z /= v.pos_proj.w
		v.pos_proj.w = 1

		return v

	def transform2screen(self, mat, v):
		v.pos_proj = v.pos_proj * mat

		return v

	def back_face_culling(self, p1, p2, p3):
		if self.renderMode == FM_WIREFRAME:
			return True

		vec1 = p2.pos - p1.pos
		vec2 = p3.pos - p2.pos

		normal = vec1.cross(vec2)

		viewDir = p1.pos - self.camera_pos

		if normal.dot(viewDir) < 0:
			return True

		return False

	def draw(self, index, index_start, vertex_start):
		screen_mat = Matrix.screen_transform(self.device.width, self.device.height)

		for i in xrange(index_start, index / 3):
			p1 = self.vertex_buffer[vertex_start + self.index_buffer[3 * i]];
			p2 = self.vertex_buffer[vertex_start + self.index_buffer[3 * i + 1]];
			p3 = self.vertex_buffer[vertex_start + self.index_buffer[3 * i + 2]];

			if not self.back_face_culling(p1, p2, p3):
				continue

			v1 = self.transform2proj(p1)
			v2 = self.transform2proj(p2)
			v3 = self.transform2proj(p3)

			if not self.clip(v1) or not self.clip(v2) or not self.clip(v3):
				continue

			v1 = self.cvv(v1)
			v2 = self.cvv(v2)
			v3 = self.cvv(v3)

			v1 = self.transform2screen(screen_mat, v1)
			v2 = self.transform2screen(screen_mat, v2)
			v3 = self.transform2screen(screen_mat, v3)

			self.draw_triangle_out(v1, v2, v3)

		return
	######################################################
	#
	######################################################
	def draw_line(self, bgn, end):
		x1, x2 = int(bgn.x), int(end.x)
		y1, y2 = int(bgn.y), int(end.y)

		dx = int(x2 - x1)
		dy = int(y2 - y1)
		stepx = 1
		stepy = 1

		if dx >= 0:
			stepx = 1
		else:
			stepx = -1
			dx = abs(dx)

		if dy >= 0:
			stepy = 1
		else:
			stepy = -1
			dy = abs(dy)

		deltax = 2 * dx
		deltay = 2 * dy

		if dx > dy:
			error = deltay - dx
			for i in xrange(dx):
				if x1 >=0 and x1 < self.device.width and y1 >= 0 and y1 < self.device.height:
					self.device.draw_pixel(x1, y1, Color.black())

				if error >= 0:
					error -= deltax
					y1 += stepy


				error += deltay
				x1 += stepx

		else:
			error = deltax - dy
			for i in xrange(dy):
				if x1 >= 0 and x1 < self.device.width and y1 >= 0 and y1 < self.device.height:
					self.device.draw_pixel(x1, y1, Color.black())

				if error >= 0:
					error -= deltay
					x1 += stepx

				error += deltax
				y1 += stepy
		
		return

	def scanline_fill(self, left, right, yIndex):
		dx = right.pos_proj.x - left.pos_proj.x

		for x in xrange(int(left.pos_proj.x), int(right.pos_proj.x)):
			xIndex = int(x + 0.5)

			if xIndex >= 0 and xIndex < self.device.width:
				lerpFactor = (x - left.pos_proj.x) / dx if dx else 0

				oneDivZ = kmath.lerp(left.oneDivZ, right.oneDivZ, lerpFactor)

				if oneDivZ >= self.device.get_z(xIndex, yIndex):
					self.device.set_z(xIndex, yIndex, oneDivZ)

					w = 1 / oneDivZ

					out = VectexOut.lerp(left, right, lerpFactor)
					out.pos_proj.y = yIndex
					out.tex *= w
					out.normal *= w
					out.color *= w

					self.device.draw_pixel(xIndex, yIndex, self.shader.ps(out))
	######################################################
	#
	######################################################
	# 平底三角形 p2 p3共线
	def _draw_triangle_flat_bottom(self, v1, v2, v3):
		dy = 0

		for y in xrange(int(v1.pos_proj.y), int(v2.pos_proj.y)):
			yIndex = int(y + 0.5)
			if yIndex >= 0 and yIndex < self.device.height:
				t = dy / (v2.pos_proj.y - v1.pos_proj.y)

				new1 = VectexOut.lerp(v1, v2, t)
				new2 = VectexOut.lerp(v1, v3, t)
				dy += 1.0

				if new1.pos_proj.x < new2.pos_proj.x:self.scanline_fill(new1, new2, yIndex)
				else:self.scanline_fill(new2, new1, yIndex)

		return

	# 平顶三角形 p1 p2共线
	def _draw_triangle_flat_top(self, v1, v2, v3):
		dy = 0

		for y in xrange(int(v1.pos_proj.y), int(v3.pos_proj.y)):
			yIndex = int(y + 0.5)
			if yIndex >= 0 and yIndex < self.device.height:
				t = dy / (v3.pos_proj.y - v1.pos_proj.y)

				new1 = VectexOut.lerp(v1, v3, t)
				new2 = VectexOut.lerp(v2, v3, t)
				dy += 1.0

				if new1.pos_proj.x < new2.pos_proj.x:self.scanline_fill(new1, new2, yIndex)
				else:self.self.scanline_fill(new2, new1, yIndex)

		return

	def draw_triangle(self, v1, v2, v3):
		if v1.pos_proj.y == v2.pos_proj.y:
			if v3.pos_proj.y <= v1.pos_proj.y: # 平底
				self._draw_triangle_flat_bottom(v3, v1, v2)
			else: # 平顶
				self._draw_triangle_flat_top(v1, v2, v3)
		elif v1.pos_proj.y == v3.pos_proj.y:
			if v2.pos_proj.y <= v1.pos_proj.y: # 平底
				self._draw_triangle_flat_bottom(v2, v1, v3)
			else: # 平顶
				self._draw_triangle_flat_top(v1, v3, v2)
		elif v2.pos_proj.y == v3.pos_proj.y:
			if v1.pos_proj.y <= v2.pos_proj.y: # 平底
				self._draw_triangle_flat_bottom(v1, v2, v3)
			else: # 平顶
				self._draw_triangle_flat_top(v2, v3, v1)
		else:
			vertices = [v1, v2, v3]
			vertices = sorted(vertices, cmp=lambda x, y:cmp(x.pos_proj.y, y.pos_proj.y))

			top = vertices[0]
			mid = vertices[1]
			bot = vertices[2]

			mid_x = (mid.pos_proj.y - top.pos_proj.y) * (bot.pos_proj.x - top.pos_proj.x) / (bot.pos_proj.y - top.pos_proj.y) + top.pos_proj.x
			dy = mid.pos_proj.y - top.pos_proj.y
			t = dy / (bot.pos_proj.y - top.pos_proj.y)

			mid_neo = VectexOut.lerp(top, bot, t)
			mid_neo.pos_proj.x = mid_x
			mid_neo.pos_proj.y = mid.pos_proj.y

			_draw_triangle_flat_top(mid, mid_neo, bot)
			_draw_triangle_flat_bottom(top, mid, mid_neo)
		return

	def draw_triangle_out(self, v1, v2, v3):
		if self.renderMode == FM_WIREFRAME:
			self.draw_line(Vector2(v1.pos_proj.x, v1.pos_proj.y), Vector2(v2.pos_proj.x, v2.pos_proj.y))
			self.draw_line(Vector2(v1.pos_proj.x, v1.pos_proj.y), Vector2(v3.pos_proj.x, v3.pos_proj.y))
			self.draw_line(Vector2(v2.pos_proj.x, v2.pos_proj.y), Vector2(v3.pos_proj.x, v3.pos_proj.y))
		elif self.renderMode == FM_SOLIDE:
			self.draw_triangle(v1, v2, v3)


	######################################################
	#
	######################################################
