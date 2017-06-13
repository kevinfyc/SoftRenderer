# -*- coding:utf-8 -*-

import sys

import pygame

import device, device_context

from color import Color

dev = device.Device(800, 600)
dev.draw_pixel(100, 100, Color.black())

# for test
from kmath import vector2, vector4
dev_con = device_context.DeviceContext(dev)

dev_con.line_clip(vector2.Vector2(200, 20), vector2.Vector2(300, 300), vector4.Vector4(100, 400, 100, 400), Color.black())

dev_con._draw_triangle_flat_bottom(vector2.Vector2(300, 100), vector2.Vector2(200, 200), vector2.Vector2(400, 200), Color.black())
dev_con._draw_triangle_flat_top(vector2.Vector2(200, 200), vector2.Vector2(400, 200), vector2.Vector2(300, 300), Color.black())

# end test

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
