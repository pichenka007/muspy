import random
print(random.randint(1, 10))

from Data.While.event import *

from pedalboard.io import AudioFile
from pedalboard import *

from scipy import signal

import pygame as pg
pg.mixer.init()
pg.font.init()

import math
import time
import numpy as np
#import matplotlib
#matplotlib.use("TKAgg")

# *** переменые *** #

old_time = time.time()
delta_time = 1 # time.time() to 60 fps

DEBUG = True

FPS = 60

WIDTH, HEIGHT = 500, 500

sc = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)

old_WIDTH, old_HEIGHT = sc.get_size()

clock = pg.time.Clock()
pg.display.set_caption("wave")

# *** global переменые *** #

#pedal_x = 1 # x1 x2 x4 x8 x16 коофицеент снижения помех
data = [] # data>>[class>>[сэмпл>>[[звук], имя, [эфекты], [данные дорожки], img]]]
efects = []



# *** class *** #

from Data.Class.Sample import *
from Data.Class.Input import *
from Data.Class.Draw import *
from Data.Class.Menu import *

draw = Draw()
menu = Menu(WIDTH, HEIGHT, pg)
controls = Input(time.time())

# *** funcs *** #


def pedaling_update(pedal=False):
	for i in range(len(data)):
		data[i].isplay_pedal = pedal


def update(pedal=False):
	for i in range(len(data)):
		if pedal:
			data[i].isplay_pedal = True
			data[i].update_play(controls.pedaling_x)
			data[i].update(pg, sc, WIDTH, HEIGHT)
		else:
			data[i].isplay_pedal = False
			data[i].update_play(controls.pedaling_x)
			data[i].update(pg, sc, WIDTH, HEIGHT)


def all_update(pedal=False):
	for i in range(len(data)):
		if pedal:
			data[i].pedaling()
			data[i].isplay_pedal = True
			data[i].update_img()
			data[i].update_play(controls.pedaling_x)
			data[i].update(pg, sc, WIDTH, HEIGHT)
		else:
			data[i].pedaling()
			data[i].isplay_pedal = False
			data[i].update_img()
			data[i].update_play(controls.pedaling_x)
			data[i].update(pg, sc, WIDTH, HEIGHT)


def make(t, math):
	data = []
	for i in range(t):
		data.append(math.sin(i/(1+pg.mouse.get_pos()[0]/100))*44100)
	return data


def add_data(file, name=None, x=0, y=0, pedal=None):
	x = x
	y = round(HEIGHT/3+10)+y*100
	with AudioFile(file) as f:
		delta_file = [f.read(f.frames), f.frames, f.samplerate]
	if not name:
		name = file.split(r"\q"[0][-1])
	if not pedal:
		efects.append([])
	else:
		efects.append(pedal)

	f, t, spectrogram = signal.spectrogram(delta_file[0][0], delta_file[2])

	data.append(Sample(delta_file[0], spectrogram, controls, efects, controls.pedaling_x, name, len(data), pedal, x, y))


def efects_append(efect_id, q):
	efects[efect_id].append(q)

from Data.Defs.defs import *

# *** UserCode *** #



add_data("Phonk Tutorial.wav", "fonk", 0, 0)
#add_data("манделавания.wav", "megalovania", 0, 0)
#add_data("dr.lisvi.wav", "dr", 0, 0)
#add_data("the.wav", "it's me", 0, 0)
#add_data("just Music.mp3", "just", 0, 0)
#for i in range(5):
#	add_data("Honk1.mp3",i, i, 1)
#add_data("Honk1.mp3", "honk", 0.05, 0, [Reverb(room_size=1)])
#add_data("Honk1.mp3", "honk", 0.1, 0, [Reverb(room_size=1)])

#efects.append(0)
#efects[0].append(0)


import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
#plt = matplotlib.pyplot
print("start")
#print(len(data[0].data[0]))
print()
print("stop")
#print(len(Sxx), len(Sxx[0]))
#for x in range(0, len(Sxx), 100):
#	for y in range(len(Sxx[x])):
#		pg.draw.rect(sc, (round(Sxx[x][y]*255), 255, 0), pg.Rect(x, y, 1, 1))
pg.display.flip()
#t, f, Sxx = signal.spectrogram(data[0].data[0][0:44100])
#plt.pcolormesh(f, t, Sxx)
#, shading="gouraud"
plt.show()
import time
#time.sleep(10)
#deltaa = []
#print(44100*10//60)
#print(44100*10//60//60)
#for i in range(44100*10):
#	deltaa.append(max(math.sin(i/5), math.cos(i**0.4), math.tan(i*2)))
#2**(1/12)
#with AudioFile("Sound/"+"sin"+".wav", "w", 44100) as f:
#	#gh = Pedalboard()
#	#gh.append(Reverb(1))
#	f.write(np.array(deltaa))

#deltaa = [deltaa, deltaa]

#data.append(Sample(deltaa, "name", [Reverb(1)], 0, 0))

#data[0].pedaling();# data[0].isplay_pedal = True; data[0].update_img()

#add_data("the.wav", "it's me", 0.05, 1)






# *** Pedaling *** #


#for i in range(len(data)):
#	pedal.append(data[i][2](data[i][0]))
#	with AudioFile("Sound/"+str(i)+".wav") as f:
#		f.write(pedal[i])
#	pedal[i] = pg.mixer.Sound("Sound/"+str(i)+".wav")

old = round(time.time())
while True:
	st = time.time()
	delta_time = (time.time()-old_time)*60
	old_time = time.time()

	keys = pg.key.get_pressed()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()
		if event.type == pg.KEYUP:
			if keys[pg.K_SPACE]:
				controls.space(update, controls, data)
		if event.type == pg.MOUSEWHEEL:
			if menu.xy_efects[0] < pg.mouse.get_pos()[0] < menu.xy_efects[0]+menu.xy_efects[2] and menu.xy_efects[1] < pg.mouse.get_pos()[1] < menu.xy_efects[1]+menu.xy_efects[3]:
				menu.y_efects += event.y*50
				menu.y_efects = min(menu.y_efects, 0)
			elif controls.dtype == "SampleR":
				try:
					if controls.end_pos[0] < pg.mouse.get_pos()[0] < controls.end_pos[0]+200:
						if controls.end_pos[1]-menu.proc_y*70//50*25 < pg.mouse.get_pos()[1] < controls.end_pos[1]+menu.proc_y*70//50*25:
							menu.ry_efects += event.y*50
							menu.ry_efects = min(menu.ry_efects, 0)
				except TypeError:
					pass
			else:
				if keys[pg.K_LSHIFT]:
					if keys[pg.K_LCTRL]:
						controls.glob_x += event.y*0.1
						controls.glob_x = -max(-controls.glob_x, 0)
					else:
						controls.glob_x += event.y
						controls.glob_x = -max(-controls.glob_x, 0)
				else:
					controls.glob_y -= event.y*100
					controls.glob_y = max(controls.glob_y, 0)
	if old_WIDTH != WIDTH or old_HEIGHT != HEIGHT:
		for i in range(len(data)):
			data[i].y -= round(old_HEIGHT/3+10)
			data[i].y += round(HEIGHT/3+10)
		old_WIDTH, old_HEIGHT = sc.get_size()

	WIDTH, HEIGHT = sc.get_size()
	sc.fill((100, 100, 100))

	# *** меню *** #

	pg.draw.rect(sc, (0, 0, 0), pg.Rect(40, 10, WIDTH-80, round(HEIGHT/3-20)))
	pg.draw.rect(sc, (0, 0, 0), pg.Rect(10, 40, WIDTH-20, round(HEIGHT/3-50)))
	#pg.draw.rect(sc, (0, 0, 0), pg.Rect(10, round(HEIGHT/3-40), 30, 30))

	pg.draw.circle(sc, (0, 0, 0), (40, 40), 30)
	pg.draw.circle(sc, (0, 0, 0), (WIDTH-40, 40), 30)
	#pg.draw.circle(sc, (0, 0, 0), (WIDTH-40, round(HEIGHT/3-40)), 30)

	# *** дорожка *** #

	pg.draw.rect(sc, (0, 0, 0), pg.Rect(10, round(HEIGHT/3+10), WIDTH-20, round(HEIGHT/3*2-50)))
	pg.draw.rect(sc, (0, 0, 0), pg.Rect(40, round(HEIGHT/3+10), WIDTH-80, round(HEIGHT/3*2-20)))
	#pg.draw.rect(sc, (0, 0, 0), pg.Rect(10, round(HEIGHT/3+10), 30, 30))

	pg.draw.circle(sc, (0, 0, 0), (WIDTH-40, round(HEIGHT/3+40)), 30)
	pg.draw.circle(sc, (0, 0, 0), (WIDTH-40, HEIGHT-40), 30)
	pg.draw.circle(sc, (0, 0, 0), (40, HEIGHT-40), 30)


	if pg.mouse.get_pressed()[0] and controls.is_move:
		controls.mouse(pg)
	else:
		if not pg.mouse.get_pressed()[0] and controls.is_move:
			controls.del_mouse(HEIGHT=HEIGHT, pg=pg, data=data, efects_append=efects_append, efects=efects)
	for i in range(len(data)):
		if pg.mouse.get_pressed()[0] and not controls.is_move and not controls.is_mouse:
			if round((controls.glob_x+data[i].x)*44.1) < pg.mouse.get_pos()[0]-10 < round((controls.glob_x+data[i].x)*44.1)+len(data[i].img):
				if data[i].y < pg.mouse.get_pos()[1] < data[i].y+100:
					controls.mouse(pg, data[i])
		if pg.mouse.get_pressed()[2] and not controls.is_move and not controls.is_mouse:
			if round((controls.glob_x+data[i].x)*44.1) < pg.mouse.get_pos()[0]-10 < round((controls.glob_x+data[i].x)*44.1)+len(data[i].img):
				if data[i].y < pg.mouse.get_pos()[1] < data[i].y+100:
					controls.mouse(pg, data[i], dtype="SampleR")
		data[i].update(pg, sc, WIDTH, HEIGHT)
	menu.update(WIDTH, HEIGHT, sc, pg, draw, controls, pedaling_update, data, controls.pedaling_x, efects_append, efects, st)

	controls.update(pg)

	#draw.rect(7.333333333333333+10, 7.333333333333333+10, 132.0, 132.0, (255, 255, 255), 10)


	#new = round(time.time())
	#if old != new:
	#	pg.mixer.Sound(np.array(make(44100), dtype=np.int16)).play()
	#old = round(time.time())



	pg.display.set_caption(str(round(clock.get_fps())))
	pg.display.flip()
	clock.tick(FPS)

"""
from pedalboard.io import AudioFile

with AudioFile("the.wav") as f:
	print(type(f))
	with AudioFile("out.wav", "w", f.samplerate, 2) as o:
		while f.tell() < f.frames:
			audio = f.read(500000)
			loader = audio ** 3
			o.write(loader)
"""