# -*- coding:utf-8 -*-

from kmath.vector2 import Vector2
from kmath.vector4 import Vector4
from kmath import vector2

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

	######################################################
	#
	######################################################
	def draw(self, index, index_start, vertex_start):pass
	######################################################
	#
	######################################################
	# 布雷森漢姆直線演算法
	def draw_line(self, bgn, end, color):
		steep = abs(end.y - bgn.y) > abs(end.x - bgn.x)

		if steep:
			bgn.x, bgn.y = bgn.y, bgn.x
			end.x, end.y = end.y, end.x

		if bgn.x > end.x:
			bgn.x, end.x = end.x, bgn.x
			bgn.y, end.y = end.y, bgn.y

		deltax = end.x - bgn.x
		deltay = abs(end.y - bgn.y)
		error = deltax / 2
		y = bgn.y

		ystep = 0 + bool(bgn.y < end.y)

		for x in xrange(bgn.x, end.x):
			self.device.draw_pixel(y, x, color) if steep else self.device.draw_pixel(x, y, color)
			error = error - deltay

			if error < 0:
				y = y + ystep
				error = error + deltax

		return

	def line_clip(self, bgn, end, rect, color):
		x1, y1 = bgn.x, bgn.y
		x2, y2 = end.x, end.y
		x_min, x_max, y_min, y_max = rect.x, rect.y, rect.z, rect.w

		code1 = bgn.encode(rect)
		code2 = end.encode(rect)

		accept = False

		while True:
			if code1 == 0 and code2 == 0:
				accept = True
				break
			elif (code1 & code2) != 0:
				break
			else:
				x, y = 1, 1

				code_out = code1 if code1 else code2

				if code_out & vector2.TOP:
					x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
					y = y_max

				elif code_out & vector2.BOTTOM:
					x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
					y = y_min

				elif code_out & vector2.RIGHT:
					y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
					x = x_max

				elif code_out & vector2.LEFT:
					y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
					x = x_min

				if code_out == code1:
					x1 = x
					y1 = y
					code1 = Vector2(x1, y1).encode(rect)
				else:
					x2 = x
					y2 = y
					code2 = Vector2(x2, y2).encode(rect)


		if accept:
			self.draw_rect(rect, color)
			self.draw_line(Vector2(x1, y1), Vector2(x2, y2), color)

		return

	######################################################
	#
	######################################################
	def draw_rect(self, rect, color):
		x_min, x_max, y_min, y_max = rect.x, rect.y, rect.w, rect.z

		self.draw_line(Vector2(x_min, y_max), Vector2(x_max, y_max), color) # lt-rt
		self.draw_line(Vector2(x_min, y_min), Vector2(x_max, y_min), color) # lb-rb
		self.draw_line(Vector2(x_min, y_max), Vector2(x_min, y_min), color) # lt-lb
		self.draw_line(Vector2(x_max, y_max), Vector2(x_max, y_min), color) # rt-rb

		return
	######################################################
	#
	######################################################
	# 平底三角形 p2 p3共线
	def _draw_triangle_flat_bottom(self, p1, p2, p3, color):
		for y in xrange(p1.y, p2.y):
			xs = int((y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x + 0.5)
			xe = int((y - p1.y) * (p3.x - p1.x) / (p3.y - p1.y) + p1.x + 0.5)
			self.draw_line(Vector2(xs, y), Vector2(xe, y), color)

		return

	# 平顶三角形 p1 p2共线
	def _draw_triangle_flat_top(self, p1, p2, p3, color):
		for y in xrange(p1.y, p3.y):
			xs = int((y - p1.y) * (p3.x - p1.x) / (p3.y - p1.y) + p1.x + 0.5)
			xe = int((y - p2.y) * (p3.x - p2.x) / (p3.y - p2.y) + p2.x + 0.5)
			self.draw_line(Vector2(xs, y), Vector2(xe, y), color)

		return

	def draw_triangle(self, p1, p2, p3, color):
		if p1.y == p2.y:
			if p3.y <= p1.y: # 平底
				self._draw_triangle_flat_bottom(p3, p1, p2, color)
			else: # 平顶
				self._draw_triangle_flat_top(p1, p2, p3, color)
		elif p1.y == p3.y:
			if p2.y <= p1.y: # 平底
				self._draw_triangle_flat_bottom(p2, p1, p3, color)
			else: # 平顶
				self._draw_triangle_flat_top(p1, p3, p2, color)
		elif p2.y == p3.y:
			if p1.y <= p2.y: # 平底
				self._draw_triangle_flat_bottom(p1, p2, p3, color)
			else: # 平顶
				self._draw_triangle_flat_top(p2, p3, p1, color)
		else:
			xtop = ytop = xmid = ymid = xbom = ybom = 0

			if p1.y < p2.y < p3.y:
				xtop, ytop = p1.x, p1.y
				xmid, ymid = p2.x, p2.y
				xbom, ybom = p3.x, p3.y
			elif p1.y < p3.y < p2.y:
				xtop, ytop = p1.x, p1.y
				xmid, ymid = p3.x, p3.y
				xbom, ybom = p2.x, p2.y
			elif p2.y < p1.y < p3.y:
				xtop, ytop = p2.x, p2.y
				xmid, ymid = p1.x, p1.y
				xbom, ybom = p3.x, p3.y
			elif p2.y < p3.y < p1.y:
				xtop, ytop = p2.x, p2.y
				xmid, ymid = p3.x, p3.y
				xbom, ybom = p1.x, p1.y
			elif p3.y < p1.y < p2.y:
				xtop, ytop = p3.x, p3.y
				xmid, ymid = p1.x, p1.y
				xbom, ybom = p2.x, p2.y 
			elif p3.x < p2.y < p1.y:
				xtop, ytop = p3.x, p2.y
				xmid, ymid = p2.x, p2.y
				xbom, ybom = p1.x, p1.y

			xl = int((ymid - ytop) * (xbom - xtop) / (ybom - ytop) + xtop + 0.5)
			if xl <= xmid: # 左三角形
				self._draw_triangle_flat_bottom(Vector2(xtop, ytop), Vector2(xl, ymid), Vector2(xmid, ymid), color)
				self._draw_triangle_flat_top(Vector2(xl, ymid), Vector2(xmid, ymid), Vector2(xbom, ybom), color)
			else: # 右三角形
				self._draw_triangle_flat_bottom(Vector2(xtop, ytop), Vector2(xmid, ymid), Vector2(xl, ymid), color)
				self._draw_triangle_flat_top(Vector2(xmid, ymid), Vector2(xl, ymid), Vector2(xbom, ybom), color)

		return


	######################################################
	#
	######################################################
