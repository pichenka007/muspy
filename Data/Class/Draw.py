class Draw():
	def rect(self, sc, pg, x, y, w, h, rgb=[0, 0, 0], r=0):
		pg.draw.rect(sc, rgb, pg.Rect(x+r, y, w-r-r, h))
		pg.draw.rect(sc, rgb, pg.Rect(x, y+r, w, h-r-r))

		pg.draw.circle(sc, rgb, (x+r, y+r), r)
		pg.draw.circle(sc, rgb, (x+w-r, y+r), r)
		pg.draw.circle(sc, rgb, (x+r, y+h-r), r)
		pg.draw.circle(sc, rgb, (x+w-r, y+h-r), r)