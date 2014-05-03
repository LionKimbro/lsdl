

import lsdl


g = {"setup": False}

colorspec = """
0xFFFFFF 0 WHITE
0xE2E2E2 1 PALE
0xED1C24 2 RED
0xFFAEC9 3 PINK
0xF1AB07 4 ORANGE
0x7D5904 5 BROWN
0xFFF200 6 YELLOW
0x22B14C 7 GREEN
0x75FF86 8 LIGHT_GREEN
0x00A2E8 9 BLUE
0x99D9EA A LIGHT_BLUE
0x8334AE B PURPLE
0xC08CDD C LIGHT_PURPLE
0xE72EEB D UGLY
0x5C5C5C E GRAY
0x000000 F BLACK
"""

colornames = []
colorvals = []

for line in colorspec.splitlines():
    if not line: continue
    a,b,c = line.split(None, 2)
    globals()[c] = int(b,16)
    colornames.append(c)
    colorvals.append((int(a[2:4],16), int(a[4:6],16), int(a[6:8],16)))
del a, b, c
del line
del colorspec


def update():
    init()
    lsdl.target(g["rr"], None)
    lsdl.copy(g["rr"], g["t"])
    lsdl.present(g["rr"])
    lsdl.target(g["rr"], g["t"])

def autoupdate():
    init()
    if g["autoupdate"]: update()


def colori(name):
    try: return colornames.index(name.upper())
    except ValueError: return None

def rgb(i):
    if isinstance(i, str): i = colori(i)
    r,gr,b = colorvals[i] if i is not None else colorvals[0xD]
    return r,gr,b


def init():
    if not g["setup"]:
        lsdl.init()
        g["w"] = lsdl.window("mer", 480, 240)
        g["rr"] = lsdl.renderer(g["w"])
        g["evt"] = lsdl.event()
        g["t"] = lsdl.texture(g["rr"], 480, 240)
        g["autoupdate"] = True
        g["setup"] = True
        update()
        color("BLUE")

def color(i):
    init()
    r,gr,b = rgb(i)
    lsdl.color(g["rr"], r,gr,b)

def point(x,y):
    init()
    lsdl.point(g["rr"], x,y)
    autoupdate()

def line(x1,y1,x2,y2):
    init()
    lsdl.line(g["rr"], x1,y1, x2,y2)
    autoupdate()

def box(x1,y1,x2,y2):
    init()
    lsdl.fillbox(g["rr"], x1,y1, x2,y2)
    autoupdate()

def wait(ms=1000):
    init()
    lsdl.delay(ms)

