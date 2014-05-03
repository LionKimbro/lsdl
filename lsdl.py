"""lsdl -- Lion's PySDL2 wrapper

notation:
  w -- "window"
  s -- "surface"
  rr -- "renderer"
"""

import ctypes, sdl2

kA = sdl2.SDLK_a;  kB = sdl2.SDLK_b;  kC = sdl2.SDLK_c
kD = sdl2.SDLK_d;  kE = sdl2.SDLK_e;  kF = sdl2.SDLK_f
kG = sdl2.SDLK_g;  kH = sdl2.SDLK_h;  kI = sdl2.SDLK_i
kJ = sdl2.SDLK_j;  kK = sdl2.SDLK_k;  kL = sdl2.SDLK_l
kM = sdl2.SDLK_m;  kN = sdl2.SDLK_n;  kO = sdl2.SDLK_o
kP = sdl2.SDLK_p;  kQ = sdl2.SDLK_q;  kR = sdl2.SDLK_r
kS = sdl2.SDLK_s;  kT = sdl2.SDLK_t;  kU = sdl2.SDLK_u
kV = sdl2.SDLK_v;  kW = sdl2.SDLK_w;  kX = sdl2.SDLK_x
kY = sdl2.SDLK_y;  kZ = sdl2.SDLK_z;  SPC = sdl2.SDLK_SPACE

k0 = sdl2.SDLK_0;  k1 = sdl2.SDLK_1;  k2 = sdl2.SDLK_2;
k3 = sdl2.SDLK_3;  k4 = sdl2.SDLK_4;  k5 = sdl2.SDLK_5;
k6 = sdl2.SDLK_6;  k7 = sdl2.SDLK_7;  k8 = sdl2.SDLK_8;
k9 = sdl2.SDLK_9

KP0 = sdl2.SDLK_KP_0; KP1 = sdl2.SDLK_KP_1; KP2 = sdl2.SDLK_KP_2
KP3 = sdl2.SDLK_KP_3; KP4 = sdl2.SDLK_KP_4; KP5 = sdl2.SDLK_KP_5
KP6 = sdl2.SDLK_KP_6; KP7 = sdl2.SDLK_KP_7; KP8 = sdl2.SDLK_KP_8
KP9 = sdl2.SDLK_KP_9

KPMINUS = sdl2.SDLK_KP_MINUS; KPPLUS = sdl2.SDLK_KP_PLUS
KPRET = sdl2.SDLK_KP_ENTER;   KPPERIOD = sdl2.SDLK_KP_PERIOD

F1 = sdl2.SDLK_F1;   F2 = sdl2.SDLK_F2;   F3 = sdl2.SDLK_F3
F4 = sdl2.SDLK_F4;   F5 = sdl2.SDLK_F5;   F6 = sdl2.SDLK_F6
F7 = sdl2.SDLK_F7;   F8 = sdl2.SDLK_F8;   F9 = sdl2.SDLK_F9
F10 = sdl2.SDLK_F10; F11 = sdl2.SDLK_F11; F12 = sdl2.SDLK_F12

RET = sdl2.SDLK_RETURN;       ESC = sdl2.SDLK_ESCAPE
RSHIFT = sdl2.SDLK_RSHIFT;    LSHIFT = sdl2.SDLK_LSHIFT
LCTRL = sdl2.SDLK_LCTRL;      RCTRL = sdl2.SDLK_RCTRL
LALT = sdl2.SDLK_LALT;        RALT = sdl2.SDLK_RALT

COMMA = sdl2.SDLK_COMMA;       PERIOD = sdl2.SDLK_PERIOD
LBRACKET = sdl2.SDLK_LEFTBRACKET
RBRACKET = sdl2.SDLK_RIGHTBRACKET
SLASH = sdl2.SDLK_SLASH;       BKSLASH = sdl2.SDLK_BACKSLASH
TICK = sdl2.SDLK_QUOTE;        BKTICK = sdl2.SDLK_BACKQUOTE
MINUS = sdl2.SDLK_MINUS;       EQUAL = sdl2.SDLK_EQUALS
BKSPACE = sdl2.SDLK_BACKSPACE; TAB = sdl2.SDLK_TAB
CAPS = sdl2.SDLK_CAPSLOCK;     NUMLOCK = sdl2.SDLK_NUMLOCKCLEAR
SEMICOLON = sdl2.SDLK_SEMICOLON
LWIN = sdl2.SDLK_LGUI;         RWIN = sdl2.SDLK_RGUI
MENU = sdl2.SDLK_APPLICATION

LEFT = sdl2.SDLK_LEFT;  RIGHT = sdl2.SDLK_RIGHT
UP = sdl2.SDLK_UP;      DOWN = sdl2.SDLK_DOWN


INS = sdl2.SDLK_INSERT;  DEL = sdl2.SDLK_DELETE
HOME = sdl2.SDLK_HOME;   END = sdl2.SDLK_END
PGUP = sdl2.SDLK_PAGEUP; PGDOWN = sdl2.SDLK_PAGEDOWN

#DIV = sdl2.SDLK_DIVIDE;  MUL = sdl2.SDLK_MULTIPLY

PRINTSCREEN = sdl2.SDLK_PRINTSCREEN
SCROLLLOCK = sdl2.SDLK_SCROLLLOCK
BREAK = sdl2.SDLK_PAUSE


eQUIT = sdl2.SDL_QUIT
eKEYDOWN = sdl2.SDL_KEYDOWN
eKEYUP = sdl2.SDL_KEYUP


kmap = {BKTICK: "`~", k1: "1!", k2: "2@", k3: "3#", k4: "4$", k5: "5%",
        k6: "6^", k7: "7&", k8: "8*", k9: "9(", k0: "0)", MINUS: "-_",
        EQUAL: "=+", kQ: "qQ", kW: "wW", kE: "eE", kR: "rR", kT: "tT",
        kY: "yY", kU: "uU", kI: "iI", kO: "oO", kP: "pP", LBRACKET: "[{",
        RBRACKET: "]}", BKSLASH: "\\|", kA: "aA", kS: "sS", kD: "dD", kF: "fF",
        kG: "gG", kH: "hH", kJ: "jJ", kK: "kK", kL: "lL", SEMICOLON: ";:",
        TICK: "'"+'"', kZ: "zZ", kX: "xX", kC: "cC", kV: "vV", kB: "bB",
        kN: "nN", kM: "mM", COMMA: ",<", PERIOD: ".>", SLASH: "/?", SPC: "  "}


def enc(s): return s.encode("ascii", "replace")

def search(s, pfix="SDL"):
    L, s, pfix = [], s.lower(), pfix.lower()
    for x in dir(sdl2):
        x_orig, x = x, x.lower()
        if s in x and x.startswith(pfix): L.append(x_orig)
    return L

def codestr(k):
    for n in globals():
        if globals()[n] == k: return n

def sdlcodestr(k):
    L = []
    for n in dir(sdl2):
        if getattr(sdl2, n) == k: L.append(n)
    return L


def init(): sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

def quit(): sdl2.SDL_Quit()

def delay(ms): sdl2.SDL_Delay(ms)


def window(ttl, w, h):
    return sdl2.SDL_CreateWindow(enc(ttl),
                                 sdl2.SDL_WINDOWPOS_UNDEFINED,
                                 sdl2.SDL_WINDOWPOS_UNDEFINED,
                                 w, h, sdl2.SDL_WINDOW_SHOWN)

def fullscreen(ttl):
    return sdl2.SDL_CreateWindow(enc(ttl),
                                 sdl2.SDL_WINDOWPOS_UNDEFINED,
                                 sdl2.SDL_WINDOWPOS_UNDEFINED,
                                 0, 0,
                                 sdl2.SDL_WINDOWPOS_FULLSCREEN_DESKTOP)

def fullscreen_pseudosize(rr, w, h):
    sdl2.SDL_SetHint(sdl2.SDL_HINT_RENDER_SCALE_QUALITY)
    sdl2.SDL_RenderSetLogicalSize(rr, w, h)

def wdestroy(w): sdl2.SDL_DestroyWindow(w)

def wupdate(w): sdl2.SDL_UpdateWindowSurface(w)


def surface(w): return sdl2.SDL_GetWindowSurface(w)


def event(): return sdl2.SDL_Event()

def poll(evt): return sdl2.SDL_PollEvent(ctypes.byref(evt))

def kcode(evt): return evt.key.keysym.sym

# expand with: https://wiki.libsdl.org/SDL_Keymod
#   (LCTRL, RCTRL, LALT, RALT)
key_to_keymod = {RSHIFT: sdl2.KMOD_RSHIFT,
                 LSHIFT: sdl2.KMOD_LSHIFT,
                 LCTRL: sdl2.KMOD_LCTRL,
                 RCTRL: sdl2.KMOD_RCTRL,
                 LALT: sdl2.KMOD_LALT,
                 RALT: sdl2.KMOD_RALT}

def pressed(key): return sdl2.SDL_GetModState() & key_to_keymod.get(key, 0)

# deprecated
def pump():
    e = event()
    while poll(e): pass


def renderer(w):
    return sdl2.SDL_CreateRenderer(w, -1, sdl2.SDL_RENDERER_ACCELERATED)

def color(rr, r,g,b,a=255): sdl2.SDL_SetRenderDrawColor(rr, r,g,b,a)

def point(rr, x, y): sdl2.SDL_RenderDrawPoint(rr, x, y)

def line(rr, x1, y1, x2, y2): sdl2.SDL_RenderDrawLine(rr, x1,y1, x2,y2)

# disambiguate rect & box
def box(rr, x,y, w,h): sdl2.SDL_RenderDrawRect(rr, rect(x,y, w,h))

def fillbox(rr, x,y, w,h): sdl2.SDL_RenderFillRect(rr, rect(x,y, w,h))

def clear(rr): sdl2.SDL_RenderClear(rr)

# NOTE: This is basically a flip!
def present(rr): sdl2.SDL_RenderPresent(rr)


def ticks(): return sdl2.SDL_GetTicks()


def sfree(s): sdl2.SDL_FreeSurface(s)


def rect(x=0,y=0,w=0,h=0): return sdl2.SDL_Rect(x,y,w,h)


def texture(rr, w, h):
    return sdl2.SDL_CreateTexture(rr, sdl2.SDL_PIXELFORMAT_ARGB8888,
                                  sdl2.SDL_TEXTUREACCESS_TARGET,
                                  w, h)

def s2t(rr, s): return sdl2.SDL_CreateTextureFromSurface(rr, s)

def tdestroy(t): sdl2.SDL_DestroyTexture(t)

def copy(rr, t, src=None, dest=None):
    return sdl2.SDL_RenderCopy(rr, t, src, dest)

def target(rr, t=None): sdl2.SDL_SetRenderTarget(rr, t)


def bmpt(rr, fname):
    s = sdl2.SDL_LoadBMP(enc(fname))
    t = s2t(rr, s)
    sfree(s)
    return t

def save_bmp(s, rr, filename):
    s_w = s.contents.w
    s_h = s.contents.h
    s_format = s.contents.format
    s_format2 = s_format.contents.format
    
    s_Bpp = s_format.contents.BytesPerPixel
    s_bpp = s_format.contents.BitsPerPixel
    s_cliprect = s.contents.clip_rect
    s_Rmask = s_format.contents.Rmask
    s_Gmask = s_format.contents.Gmask
    s_Bmask = s_format.contents.Bmask
    s_Amask = s_format.contents.Amask
    
    # pixels
    p = ctypes.create_string_buffer(s_w * s_h * s_Bpp)
    
    r = rect(0, 0, s_w, s_h)
    
    sdl2.SDL_RenderReadPixels(rr, ctypes.byref(r), s_format2, p, s_w * s_Bpp)
    rgb = sdl2.SDL_CreateRGBSurfaceFrom(p, s_w, s_h, s_bpp, s_w * s_Bpp,
                                        s_Rmask, s_Gmask, s_Bmask, s_Amask)
    sdl2.SDL_SaveBMP(rgb, enc(filename))

