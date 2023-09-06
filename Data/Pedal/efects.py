from pedalboard import *
res = []

"""
!efect ->
sound_efect = pedal(sound)

!defolt_args ->
pedal = Pedalboard()
pedal.append(Reverb(defolt_args))

!color ->
color

!name ->
name
"""

class Efect():
	def __init__(self, efect, defolt_args, color, name):
		self.efect = efect
		self.defolt_args = defolt_args
		self.color = color
		self.name = name
		self.x = 0
		self.y = 0

		self.data = []
		self.move = False
	def draw(self, draw, sc, pg, ww, text):
		self.x, self.y = pg.mouse.get_pos()
		xx, yy, ww, hh = self.x-ww/2, self.y-25, ww, 50
		draw.rect(sc, pg, xx, yy, ww, hh, self.color, 25)
		sc.blit(text, (xx+ww/2-text.get_size()[0]/2, yy))




#              efect  defolt_args         color               name
res.append(Efect(Reverb, [0.3], (255/1.1, 255/1.5, 255/1.5), "Reverb"))

res.append(Efect(Reverb, [0.6], (255/1.5, 255/1.1, 255/1.5), "Reverb"))
res.append(Efect(Reverb, [1], (255/1.5, 255/1.5, 255/1.1), "Reverb"))
res.append(Efect(PitchShift, [10], (255/1.5, 255/1.5, 255/1.1), "PitchShift+"))
res.append(Efect(PitchShift, [-10], (255/1.5, 255/1.5, 255/1.1), "PitchShift-"))
res.append(Efect(Delay, [1], (255/1.5, 255/1.5, 255/1.1), "Delay"))






if __name__ == "__main__":
	print("откройте этот файл чтобы добавить свои эфекты или vst плагины")
	#print(dir(PitchShift))
	input("нажмите enter чтобы закрыть")
