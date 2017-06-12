# -*- coding:utf-8 -*-

import sys

import pygame

import color

class Device:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		pygame.init()

		self.screen = pygame.display.set_caption('soft renderer')
		self.screen = pygame.display.set_mode([width, height])
		self.screen.fill(color.Color.gray().to_list())

		return

	def draw_pixel(self, x, y, color):
		pygame.draw.rect(self.screen, color.to_list(), [x, y, 1, 1], 1)
		pygame.display.flip()

		return

