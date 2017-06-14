# -*- coding:utf-8 -*-

import sys

import config

if config.USE_PYGAME:
	import pygame
	from pygame import gfxdraw
else:
	import Tkinter

from color import Color

class Device:
	def __init__(self, width, height):
		self.width = width
		self.height = height

		if config.USE_PYGAME:
			pygame.init()

			self.screen = pygame.display.set_caption('soft renderer')
			self.screen = pygame.display.set_mode([width, height])
			self.screen.fill(Color.red().to_list())
		else:
			self.window = Tkinter.Tk()
			self.window.title("soft renderer")
			self.cvs = Tkinter.Canvas(self.window, width=width, height=height)
			self.cvs.pack()

		self.frame_buffer = [0, ] * self.width * self.height
		self.z_buffer = [[0,] * self.height ] * self.width

		self.c = 0

		return

	def get_z(self, x, y):
		if x >= 0 and x < self.width and y >= 0 and y < self.height:return self.z_buffer[x][y]

		return 1

	def set_z(self, x, y, z):
		if x >= 0 and x < self.width and y >= 0 and y < self.height:self.z_buffer[x][y] = z

		return

	def draw_pixel(self, x, y, color):
		hex_color = Color.to_hex(color)
		cur_color = self.frame_buffer[self.width*y + x]

		if hex_color == cur_color:return

		self.frame_buffer[self.width*y + x] = Color.to_hex(color)

		if config.USE_PYGAME:
			gfxdraw.pixel(self.screen, x, y, color.to_list())
		else:
			self.cvs.create_line(x, y, x, y+1, fill="#ff0000")

		return

	def begin_draw(self):pass

	def end_draw(self):
		if config.USE_PYGAME:
			pygame.display.flip()

		return

	def clear_buffer(self, color):
		for x in xrange(self.width):
			for y in xrange(self.height):
				self.draw_pixel(x, y, color)
				self.z_buffer[x][y] = 0

