from Data.Pedal.efects import *
import time
import math
import numpy as np


class Menu():
	def __init__(self, W, H, pg):
		self.proc_x = (W-20)/100
		self.proc_y = (H/3)/100
		self.qw = []

		self.efects = res
		self.y_efects = 0
		self.ry_efects = 0
		xx, yy, ww, hh, rr = self.proc_x*100+10-80-min(200, self.proc_y*100*1.3), self.proc_y*15+10, min(200, self.proc_y*100*1.3), self.proc_y*70//50*50, 25
		self.xy_efects = [xx, yy, ww, hh]
		self.mouse = False

		for i in range(100):
			self.qw.append([0, 0])
		self.font_ComicSansMS = pg.font.Font("fonts/ComicSansMS.ttf", 18)
		self.font_ComicSansMS_30 = pg.font.Font("fonts/ComicSansMS.ttf", 30)
	def update(self, WIDTH, HEIGHT, sc, pg, draw, controls, pedaling_update, data, pedal_x, efects_append, efects, st):
		self.proc_x = (WIDTH-20)/100
		self.proc_y = (HEIGHT/3-20)/100
		x, y = pg.mouse.get_pos()
		# *** add song *** #

		xx, yy, ww, hh, rr = 30, 30, round(self.proc_y*100)-40, round(self.proc_y*100)-40, 20
		if yy < x < hh+yy and yy < y < hh+yy:
			draw.rect(sc, pg, xx, yy, ww, hh, (255/1.5, 255/1.5, 255/1.5), rr)
		else:
			draw.rect(sc, pg, xx, yy, ww, hh, (255/2, 255/2, 255/2), rr)

		draw.rect(sc, pg, xx+ww/2-10, yy+yy/2, 20, hh-30, (255, 255, 255), 10)
		draw.rect(sc, pg, xx+15, yy+hh/2-10, hh-30, 20, (255, 255, 255), 10)

		#add = self.font_ComicSansMS_30.render("add", True, (255, 255, 255))
		#sc.blit(add, (yy+hh/2-25, yy+hh/1.5))

		# *** pedal_x *** #

		xx, yy, ww, hh, rr = round(self.proc_x*100+10), round(self.proc_y*100+15), round(self.proc_x*5), 10, 4

		if xx-50*1-10 < x < xx-50*1+hh+10 and yy-10 < y < yy+hh+10:
			draw.rect(sc, pg, xx-50*1, yy, hh, hh, (255/4, 255/4, 255/4), rr)
			if pg.mouse.get_pressed()[0] and not controls.is_mouse:
				controls.x16()
		else:
			draw.rect(sc, pg, xx-50*1, yy, hh, hh, (255, 255, 255), rr)
		x16 = self.font_ComicSansMS.render("x16", True, (255, 255, 255))
		sc.blit(x16, (xx-50*1+15, yy-9))

		if xx-50*2-10 < x < xx-50*2+hh+10 and yy-10 < y < yy+hh+10:
			draw.rect(sc, pg, xx-50*2, yy, hh, hh, (255/4, 255/4, 255/4), rr)
			if pg.mouse.get_pressed()[0]:
				controls.x8()
		else:
			draw.rect(sc, pg, xx-50*2, yy, hh, hh, (255, 255, 255), rr)
		x8 = self.font_ComicSansMS.render("x8", True, (255, 255, 255))
		sc.blit(x8, (xx-50*2+15, yy-9))

		if xx-50*3-10 < x < xx-50*3+hh+10 and yy-10 < y < yy+hh+10:
			draw.rect(sc, pg, xx-50*3, yy, hh, hh, (255/4, 255/4, 255/4), rr)
			if pg.mouse.get_pressed()[0]:
				controls.x4()
		else:
			draw.rect(sc, pg, xx-50*3, yy, hh, hh, (255, 255, 255), rr)
		x4 = self.font_ComicSansMS.render("x4", True, (255, 255, 255))
		sc.blit(x4, (xx-50*3+15, yy-9))

		if xx-50*4-10 < x < xx-50*4+hh+10 and yy-10 < y < yy+hh+10:
			draw.rect(sc, pg, xx-50*4, yy, hh, hh, (255/4, 255/4, 255/4), rr)
			if pg.mouse.get_pressed()[0]:
				controls.x2()
		else:
			draw.rect(sc, pg, xx-50*4, yy, hh, hh, (255, 255, 255), rr)
		x2 = self.font_ComicSansMS.render("x2", True, (255, 255, 255))
		sc.blit(x2, (xx-50*4+15, yy-9))

		if xx-50*5-10 < x < xx-50*5+hh+10 and yy-10 < y < yy+hh+10:
			draw.rect(sc, pg, xx-50*5, yy, hh, hh, (255/4, 255/4, 255/4), rr)
			if pg.mouse.get_pressed()[0]:
				controls.x1()
		else:
			draw.rect(sc, pg, xx-50*5, yy, hh, hh, (255, 255, 255), rr)
		x1 = self.font_ComicSansMS.render("x1", True, (255, 255, 255))
		sc.blit(x1, (xx-50*5+15, yy-9))

		draw.rect(sc, pg, xx-50*controls.pedal_x+1, yy+1, hh-2, hh-2, (255/10, 255/10, 255/10), rr-1)

		# *** pedaling *** #

		xx, yy, ww, hh, rr = 10+2, round(self.proc_y*100+10)+2, 16, 16, 4

		if controls.pedaling:
			if xx < x < xx+ww and yy < y < yy+hh:
				draw.rect(sc, pg, xx, yy, ww, hh, (0, 255/1.2, 0), rr)
				if pg.mouse.get_pressed()[2]:
					controls.pedal(False, pedaling_update)
			else:
				draw.rect(sc, pg, xx, yy, ww, hh, (0, 255, 0), rr)
		else:
			if xx < x < xx+ww and yy < y < yy+hh:
				draw.rect(sc, pg, xx, yy, ww, hh, (255/1.2, 0, 0), rr)
				if pg.mouse.get_pressed()[0]:
					controls.pedal(True, pedaling_update)
			else:
				draw.rect(sc, pg, xx, yy, ww, hh, (255, 0, 0), rr)

		pedaling = self.font_ComicSansMS.render("pedaling", True, (255, 255, 255))
		sc.blit(pedaling, (xx+20, yy-7))

		# *** ecvalayzer *** #

		xx, yy, ww, hh, rr = round(self.proc_y*100), 30,  (self.proc_x*100-80-min(200, self.proc_y*100*1.3)-round(self.proc_y*100))//10*10, self.proc_y*100-40, 0

		notes = round(ww)

		draw.rect(sc, pg, xx, yy, ww, hh, (255, 255, 255), rr)

		if controls.play:
			for i in range(notes):
				d = []
				for q in range(len(data)):
					if 0 < round((time.time()-controls.start_time-controls.glob_space_x-data[q].x)*44.1) < len(data[q].img):
						d.append(data[q])
			try:
				spec = self.delta_spec
			except AttributeError:
				spec = []
				for i in range(129):
					spec.append(0)
			for i in range(len(d)):
				start_d = round((time.time()-controls.start_time-d[i].x-controls.glob_x)*44100)
				step = len(d[i].img)*1000/len(d[i].spectrogram[0])
				ti = round(start_d/step)
				pt = time.time()
				for n in range(129):
					try:
						spec[n] = min((spec[n]+d[i].spectrogram[n][ti])/2, 1)
						spec[n] = (max(spec[n-1]+spec[n], 0))/2
					except IndexError: spec[n] = (max(spec[n-1]+spec[n], 0))/2
				for n in range(129):
					try:
						spec[128-n] = (spec[128-n+1]+spec[128-n])/2
					except IndexError: pass
			for i in range(len(spec)):
				pg.draw.rect(sc, (255, 0, 0), pg.Rect(xx+round(i*ww/129), yy, round(ww/129), round(min(spec[i]*10**9.5, hh))))
			self.delta_spec = spec
		# *** efects *** #

		xx, yy, ww, hh, rr = self.proc_x*100+10-80-min(200, self.proc_y*100*1.3), self.proc_y*15+10, min(200, self.proc_y*100*1.3), self.proc_y*70//50*50, 25
		self.xy_efects = [xx, yy, ww, hh]
		draw.rect(sc, pg, xx, yy, ww, hh, (255/4, 255/4, 255/4), rr)

		for i in range(len(self.efects)):
			if -1 < i+self.y_efects//50 < hh//50:
				text = self.font_ComicSansMS_30.render(self.efects[i].name, True, (255, 255, 255))
				draw.rect(sc, pg, xx, yy+(i+self.y_efects//50)*50, ww, 50, self.efects[i].color, 25)
				sc.blit(text, (xx+ww/2-text.get_size()[0]/2, yy+(i+self.y_efects//50)*50))
				if xx < x+10 < xx+ww and yy+(i+self.y_efects//50)*50 < y < yy+(i+self.y_efects//50)*50+50:
					if pg.mouse.get_pressed()[0] and not controls.is_move:
						controls.mouse(pg, self.efects[i])
				if not pg.mouse.get_pressed()[0] and self.efects[i].move:
					controls.del_mouse(HEIGHT, data, pg, efects_append, efects)
				if self.efects[i].move:
					if len(self.efects[i].data) != 50:
						for egg in range(50):
							self.efects[i].data.append([x-ww/2, y-25])
					for q in reversed(range(len(self.efects[i].data))):
						draw.rect(sc, pg, self.efects[i].data[q][0], self.efects[i].data[q][1], ww, 50, (self.efects[i].color[0]/(q/10+1), self.efects[i].color[1]/(q/10+1), self.efects[i].color[2]/(q/10+1)), 25)
						if q == 0:
							self.efects[i].data[q][0] = x-ww/2
							self.efects[i].data[q][1] = y-25
						else:
							self.efects[i].data[q][0] += (self.efects[i].data[q-1][0]-self.efects[i].data[q][0])/2
							self.efects[i].data[q][1] += (self.efects[i].data[q-1][1]-self.efects[i].data[q][1])/2
					self.efects[i].draw(draw, sc, pg, ww, text)

		# *** Sample efects *** #

		if controls.is_SampleR:
			xx, yy, ww, hh, rr = controls.end_pos[0], controls.end_pos[1]-self.proc_y*70//50*25, 200, self.proc_y*70//50*50, 25
			draw.rect(sc, pg, xx, yy, ww, hh, (255, 255, 255), rr)
			if not pg.mouse.get_pressed()[0] and self.mouse:
				self.mouse = False
			try:
				for i in range(len(efects[controls.obj.id])):
					if -1 < i+self.ry_efects//50 < hh//50:
						text = self.font_ComicSansMS_30.render(efects[controls.obj.id][i].name, True, (255, 255, 255))
						draw.rect(sc, pg, xx, yy+(i+self.ry_efects//50)*50, ww, 50, efects[controls.obj.id][i].color, 25)
						sc.blit(text, (xx+ww/2-text.get_size()[0]/2, yy+(i+self.ry_efects//50)*50))
						if pg.mouse.get_pressed()[0]:
							if xx < x < xx+ww and yy+(i+self.ry_efects//50)*50 < y < yy+(i+self.ry_efects//50)*50+50 and not self.mouse:
								del efects[controls.obj.id][round(yy-y)//50]
								self.mouse = True
							if xx < x < xx+ww and yy < y < yy+hh:
								pass
							else:
								controls.obj.pedaling(efects=efects)
								controls.obj.update_img()
								controls.obj.update_play(controls.pedaling_x)
								controls.del_mouse(is_R=True)
								break
			except IndexError:
				pass
			try:
				if len(efects[controls.obj.id]) == 0:
					controls.obj.pedaling(efects=efects)
					controls.obj.update_img()
					controls.obj.update_play(controls.pedaling_x)
					controls.del_mouse(is_R=True)
			except AttributeError:
				pass

		# *** mouse *** #

		for i in range(len(self.qw)):
			if i == 0:
				self.qw[i][0] += (pg.mouse.get_pos()[0]-self.qw[i][0])
				self.qw[i][1] += (pg.mouse.get_pos()[1]-self.qw[i][1])
			else:
				self.qw[i][0] += (self.qw[i-1][0]-self.qw[i][0])/1.5
				self.qw[i][1] += (self.qw[i-1][1]-self.qw[i][1])/1.25
			pg.draw.circle(sc, (255, 0, 0), self.qw[i], (len(self.qw)-i)*(5/len(self.qw)))