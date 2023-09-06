import time
from pedalboard import *
import numpy as np
import pygame as pg
from scipy import signal


class Sample():
	def __init__(self, song, spectrogram, controls, efects, pedal_x, name, efect_id, pedal=[], x=0, y=0,img=None):
		t = time.time()
		self.data = song
		self.data_pedal = self.data[0]
		self.spectrogram = spectrogram
		self.controls = controls
		self.name = name
		self.id = efect_id
		self.pedal = pedal
		self.pedaling(efects=efects)
		self.x, self.y = x, y
		self.xx, self.yy = 0, 0
		self.img = img
		self.img_pedal = None
		self.update_img()
		self.isplay = False
		self.isplay_pedal = False
		self.s = None
		self.s_pedal = None
		#self.update_play(pedal_x)
		#print(np.min(self.data), np.max(self.data))
		#print(time.time()-t)

	def update(self, pg, sc, WIDTH, HEIGHT):
		if round((time.time()-self.controls.start_time-self.controls.glob_space_x-self.x)*44.1) > 0 and not self.isplay and self.controls.play:
			self.play()
			#print("play")
		if self.controls.glob_y - self.y + round(HEIGHT/3+10) <= 0:
			if self.controls.play:
				for q in range(round((time.time()-self.controls.start_time-self.controls.glob_x-self.x)*44.1), round(WIDTH+round((time.time()-self.controls.start_time-self.controls.glob_x-self.x)*44.1)-20)):
					try:
						if q >= 0:
							het = self.get_img()[q]
							pg.draw.rect(sc, (255, 0, 0), pg.Rect(q-(time.time()-self.controls.start_time-self.controls.glob_x-self.x)*44.1+10+self.xx, self.y+(50-(het*100)/2)-self.controls.glob_y+self.yy, 1, het*100))
					except IndexError:
						if q >= 0:
							pass
			else:
				for q in range(round((-self.controls.glob_x-self.x)*44.1), round(WIDTH+round((-self.controls.glob_x-self.x)*44.1)-20)):
					try:
						if q >= 0:
							het = self.get_img()[q]
							pg.draw.rect(sc, (255, 0, 0), pg.Rect(q-(-self.controls.glob_x-self.x)*44.1+10+self.xx, self.y+(50-(het*100)/2)-self.controls.glob_y+self.yy, 1, het*100))
					except IndexError:
						if q >= 0:
							pass

	def get_data(self):
		return self.data

	def get_name(self):
		return self.name

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_img(self):
		if self.isplay_pedal:
			return self.img_pedal
		return self.img

	def pedaling(self, pedal=[], efects=None):
		pedalb = Pedalboard()
		if len(pedal) != 0:
			self.pedal = []
			for i in range(len(pedal)):
				pedalb.append(pedal[i].efect(*pedal[i].defolt_args))
			self.pedal = pedal
		else:
			self.pedal = efects[self.id]
			for i in range(len(self.pedal)):
				pedalb.append(self.pedal[i].efect(*self.pedal[i].defolt_args))
		self.data_pedal = pedalb(self.data, 44100)

	def update_spectrogram(self):
		if self.isplay_pedal:
			self.spectrogram = signal.spectrogram(self.data_pedal[0], len(self.data_pedal[0]))[2]
		else:
			self.spectrogram = signal.spectrogram(self.data[0], len(self.data[0]))[2]
	def update_img(self):
		img = np.array([])
		for i in range(0, len(self.data_pedal[0]), 1000):
			try:
				if i == 0:
					img = np.append(img, 1)
				else:
					delta_wave = np.mean(np.abs(self.data_pedal[0][i:i+1000]))
					img = np.append(img, delta_wave)
			except IndexError:
				img = np.append(img, 1)
		img[-1] = 1
		self.img_pedal = img

		img = np.array([])
		for i in range(0, len(self.data[0]), 1000):
			try:
				if i == 0:
					img = np.append(img, 1)
				else:
					delta_wave = np.mean(np.abs(self.data[0][i:i+1000]))
					img = np.append(img, delta_wave)
			except IndexError:
				img = np.append(img, 1)
		img[-1] = 1
		self.img = img
	def update_play(self, pedal_x):
		t = time.time()
		self.s_pedal = pg.mixer.Sound(np.array(self.data_pedal[0][round((-self.controls.glob_x-self.x)*44100):-1]*(44100/pedal_x), dtype=np.int32))
		self.s = pg.mixer.Sound(np.array(self.data[0][round((-self.controls.glob_x-self.x)*44100):-1]*(44100/pedal_x), dtype=np.int32))
		#print(time.time()-t)
	def play(self, start=0, colvo=0, update=False):
		global pedal_x
		if not self.s or update:
			if self.isplay_pedal:
				self.s_pedal = pg.mixer.Sound(np.array([self.data_pedalt[0][round(-self.controls.glob_x*44100):-1]*(44100/pedal_x), self.data_pedalt[1][round(self.controls.glob_x*44100):-1]*(44100/pedal_x)], dtype=np.int32))
			else:
				self.s = pg.mixer.Sound(np.array([self.data[0][round(-self.controls.glob_x*44100):-1]*(44100/pedal_x), self.data[1][round(self.controls.glob_x*44100):-1]*(44100/pedal_x)], dtype=np.int32))
		t = time.time()
		if self.isplay_pedal:
			self.s_pedal.play()
		else:
			self.s.play()
		#print(time.time()-t)
		self.isplay = True

	def stop(self):
		self.s.stop()
		self.s_pedal.stop()
		self.isplay = False