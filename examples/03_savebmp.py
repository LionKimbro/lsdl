import lsdl
from lsdl import UP, DOWN, LEFT, RIGHT, ESC, F1

lsdl.init()

w = lsdl.window("Key Events", 400, 200)
rr = lsdl.renderer(w)
e = lsdl.event()  # reusable event object

lsdl.color(rr, 0,0,0)
lsdl.clear(rr)
lsdl.color(rr, 255,0,0)
lsdl.fillbox(rr, 50,50, 20,20)

# Create the surface for the window you want to save, when you want to
# save it.
lsdl.save_bmp(lsdl.surface(w), rr, "saved.bmp")

# If you present the drawing, and THEN save, a blank screen will be
# saved, because present performs a FLIP, leaving a blank screen in
# the drawing area (which is then saved.)
lsdl.present(rr)

lsdl.wdestroy(w)

