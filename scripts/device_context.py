# -*- coding:utf-8 -*-

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
