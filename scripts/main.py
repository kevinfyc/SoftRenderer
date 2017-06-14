# -*- coding:utf-8 -*-

import sys
import time

import pygame

import device, device_context

from color import Color

from shape.cube import Cube

g_cube = Cube()

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

	print "fps is %f dtime is %f" % (1 / nt, time.time() - tt, )
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
