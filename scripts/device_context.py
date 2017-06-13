# -*- coding:utf-8 -*-

from kmath.vector2 import Vector2
from kmath import vector2

FM_WIREFRAME = 0 # 线框
FM_SOLIDE	 = 1 # 填充

class DeviceContext:
	def __init__(self, device):
		self.device = device
		self.renderMode = FM_WIREFRAME

		return

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

	def draw_rect(self, rect, color):
		x_min, x_max, y_min, y_max = rect.x, rect.y, rect.w, rect.z

		self.draw_line(Vector2(x_min, y_max), Vector2(x_max, y_max), color) # lt-rt
		self.draw_line(Vector2(x_min, y_min), Vector2(x_max, y_min), color) # lb-rb
		self.draw_line(Vector2(x_min, y_max), Vector2(x_min, y_min), color) # lt-lb
		self.draw_line(Vector2(x_max, y_max), Vector2(x_max, y_min), color) # rt-rb

		return
