import lsdl
from lsdl import UP, DOWN, LEFT, RIGHT, ESC

lsdl.init()

w = lsdl.window("Key Events", 400, 200)
rr = lsdl.renderer(w)
e = lsdl.event()  # reusable event object

x, y, dx, dy = 50, 50, 0, 0
running = True

while running:
    if lsdl.poll(e):
        if e.type == lsdl.eQUIT: running = False
        elif e.type == lsdl.eKEYDOWN:
            key = lsdl.kcode(e)
            x += {LEFT: -10, RIGHT: +10}.get(key, 0)
            y += {UP: -10, DOWN: +10}.get(key, 0)
            if key == ESC: running = False
    lsdl.color(rr, 0,0,0)
    lsdl.clear(rr)
    lsdl.color(rr, 255,0,0)
    lsdl.fillbox(rr, x,y, 20,20)
    lsdl.present(rr)

lsdl.wdestroy(w)
