# -*- coding:utf-8 -*-

from kmath.matrix import Matrix
import config

from color import Color

from device import Device
from device_context import DeviceContext
import device_context

from kmath.vector4 import Vector4
from kmath import kmath

from shape.geometry_creator import g_geometry_creator

from shader import CubeShader

class Cube:
	def __init__(self):
		self.world = Matrix()
		self.world.identity()

		self.worldViewProj = Matrix()
		self.worldViewProj.identity()

		self.worldInvTranspose = Matrix()
		self.worldInvTranspose.identity()

		self.device = Device(config.CLIENT_WIDTH, config.CLIENT_HEIGHT)
		self.device_context = DeviceContext(self.device)

		self.mesh = g_geometry_creator.create_cube(2, 2, 2)

		self.device_context.set_vertex_buffer(self.mesh.vertices)
		self.device_context.set_index_buffer(self.mesh.indices)

		self.shader = CubeShader()

		self.device_context.set_shader(self.shader)

		return

	def tick(self, dt):
		pos = Vector4(0, 1.54508531, -4.75528240, 1)
		target = Vector4(0, 0, 0, 1)
		up = Vector4.up()

		view = Matrix.matrix_look_at_lh(pos, target, up)
		proj = Matrix.perspective_fov_lh(kmath.HALF_SQRT, self.device.width /  (self.device.height*1.0), 1, 100)

		self.worldViewProj = self.world * view * proj;

		tmp = self.world
		tmp.inverse()
		tmp.transpose()
		self.worldInvTranspose = tmp

		self.device_context.set_camera_pos(pos)

		return

	def draw(self):
		self.device.begin_draw()

		self.device.clear_buffer(Color.gray())

		self.device_context.set_render_mode(device_context.FM_SOLIDE)

		self.shader.set_wvp(self.worldViewProj)
		self.shader.set_world(self.world)
		self.shader.set_world_inv_transpose(self.worldInvTranspose)

		self.device_context.draw(len(self.mesh.indices), 0, 0)

		self.device.end_draw()
		return

