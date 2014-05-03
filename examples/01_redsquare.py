import lsdl

lsdl.init()

w = lsdl.window("Red Square", 400, 200)

rr = lsdl.renderer(w)

lsdl.color(rr, 255,0,0)
lsdl.fillbox(rr, 10,10, 50,50)
lsdl.present(rr)

e = lsdl.event()  # creates a reusable event object

while not e.type == lsdl.eQUIT: lsdl.poll(e)

lsdl.wdestroy(w)
