import time
class Input():
	def __init__(self, start_time):
		self.play = False
		self.glob_y = 0
		self.glob_x = 0
		self.glob_space_x = self.glob_x
		self.pedals = False
		self.start_time = start_time

		self.is_mouse = False

		self.dtype = None
		self.is_move = False
		self.obj = None
		self.start_pos = None
		self.end_pos = None

		self.pedal_x = 4
		self.pedaling = False

		self.pedaling_x = 2

		self.is_efect = False

		self.is_SampleR = False



	def mouse(self, pg, obj=None, dtype=None):
		if not self.is_move:
			self.obj = obj
			if dtype:
				self.dtype = dtype
			else:
				self.dtype = type(self.obj).__name__
			self.start_pos = pg.mouse.get_pos()
			self.is_move = not self.is_move
			self.is_mouse = True
			if self.dtype == "SampleR":
				self.end_pos = pg.mouse.get_pos()
				self.is_mouse = False
				self.is_SampleR = True
		else:
			if self.dtype == "Sample":
				self.end_pos = pg.mouse.get_pos()
				self.obj.xx, self.obj.yy = self.end_pos[0]-self.start_pos[0], self.end_pos[1]-self.start_pos[1]
				self.is_mouse = False
			elif self.dtype == "Efect":
				self.end_pos = pg.mouse.get_pos()
				self.obj.x, self.obj.y = self.end_pos[0], self.end_pos[1]-25
				self.obj.move = True
				self.is_mouse = False

	def del_mouse(self, HEIGHT=None, data=None, pg=None, efects_append=None, efects=None, is_R=False):
		if self.dtype == "Sample":
			self.obj.x = self.obj.x+self.obj.xx/44.1
			self.obj.y -= round(HEIGHT/3+10)
			self.obj.y += round(self.obj.yy/100)*100
			self.obj.y = max(self.obj.y, 0)
			self.obj.y += round(HEIGHT/3+10)
			self.obj.xx, self.obj.yy = 0, 0
			self.is_mouse = False
			self.is_move = False
			self.obj = None
			self.start_pos = None
			self.end_pos = None
		elif self.dtype == "SampleR" and is_R:
			self.is_mouse = False
			self.is_move = False
			self.obj = None
			self.start_pos = None
			self.end_pos = None
			self.is_SampleR = False
			self.dtype = None
		elif self.dtype == "Efect":
			for i in range(len(data)):
				if round((self.glob_x+data[i].x)*44.1)+10 < pg.mouse.get_pos()[0] < round((self.glob_x+data[i].x)*44.1)+len(data[i].img)+10:
					if data[i].y < pg.mouse.get_pos()[1] < data[i].y+100:
						start_time = time.time()
						efects_append(data[i].id, self.obj)
						data[i].pedaling(efects=efects)
						print(time.time()-start_time)
						data[i].update_img()
						print(time.time()-start_time)
						data[i].update_play(self.pedaling_x)
						print(time.time()-start_time)
						data[i].update_spectrogram()
						print(time.time()-start_time)
						break
			self.obj.data = []
			self.obj.move = False
			self.is_mouse = False
			self.is_move = False
			self.obj = None
			self.start_pos = None
			self.end_pos = None
	def space(self, update, controls, data):
		self.glob_space_x = self.glob_x
		if not self.play:
			global pedal_x
			self.pedaling_x = 2**(5-self.pedal_x)
			update(controls.pedaling)
		self.play = not self.play
		if self.play:
			for i in range(len(data)):
				data[i].update_spectrogram()
			self.start_time = time.time()
		else:
			for i in range(len(data)):
				data[i].stop()

	def x1(self):
		self.pedal_x = 5

	def x2(self):
		self.pedal_x = 4

	def x4(self):
		self.pedal_x = 3

	def x8(self):
		self.pedal_x = 2

	def x16(self):
		self.pedal_x = 1


	def pedal(self, mouse, pedaling_update):
		self.pedaling = mouse
		pedaling_update(mouse)

	def update(self, pg):
		self.is_mouse = pg.mouse.get_pressed()[0]