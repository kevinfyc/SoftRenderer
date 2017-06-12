# -*- coding:utf-8 -*-

import sys

import pygame

import device

from color import Color

dev = device.Device(800, 600)
dev.draw_pixel(100, 100, Color.black())

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
