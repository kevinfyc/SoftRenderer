# -*- coding:utf-8 -*-

FM_WIREFRAME = 0 # 线框
FM_SOLIDE	 = 1 # 填充

class DeviceContext:
	def __init__(self, device):
		self.device = device
		self.renderMode = FM_WIREFRAME

		return

