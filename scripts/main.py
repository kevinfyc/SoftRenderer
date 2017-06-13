# -*- coding:utf-8 -*-

import sys

import pygame

import device, device_context

from color import Color

dev = device.Device(800, 600)
dev.draw_pixel(100, 100, Color.black())

# for test
from kmath import vector2
dev_con = device_context.DeviceContext(dev)
dev_con.draw_line(vector2.Vector2(100, 100), vector2.Vector2(300, 500), Color.black())
# end test

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
