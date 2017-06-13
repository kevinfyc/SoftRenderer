# -*- coding:utf-8 -*-

import sys
import time

import pygame

import device, device_context

from color import Color

from shape.cube import Cube

g_cube = Cube()

#dev = device.Device(800, 600)
#dev.clear_buffer(Color.gray())
#dev.draw_pixel(100, 100, Color.black())
#
## for test
#from kmath import vector2, vector4, matrix
#dev_con = device_context.DeviceContext(dev)
#
#dev_con.line_clip(vector2.Vector2(200, 20), vector2.Vector2(300, 300), vector4.Vector4(100, 400, 100, 400), Color.black())
#
##dev_con._draw_triangle_flat_bottom(vector2.Vector2(300, 100), vector2.Vector2(200, 200), vector2.Vector2(400, 200), Color.black())
##dev_con._draw_triangle_flat_top(vector2.Vector2(200, 200), vector2.Vector2(400, 200), vector2.Vector2(300, 300), Color.black())
#
#dev_con.draw_triangle(vector2.Vector2(200, 100), vector2.Vector2(100, 200), vector2.Vector2(300, 300), Color.black())
#
#mat1 = matrix.Matrix(1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4)
#mat2 = matrix.Matrix(11, 22, 33, 44, 11, 22, 33, 44, 11, 22, 33, 44, 11, 22, 33, 44)
#mat = mat1 * mat2
#print mat
#
## end test

tt = 0
nt = 0
while True:
	tt = time.time()
	g_cube.tick(nt)
	g_cube.draw()

	nt = time.time() - tt

	s = 1 / 60.0
	if nt < s:
		time.sleep(s - nt)

	print "fps is %f" % (1 / nt, )
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
