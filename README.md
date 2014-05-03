lsdl
====

Lion's PySDL2 Alternative Interface
-----------------------------------

[SDL2][1] supports multiple window and hardware accelerated textures.

[PySDL2][2] is a pure python wrapper around SDL2.

PySDL2 comes with a lot of "extra stuff," though.
If you want simple and direct access, you may appreciate this wrapper.

    pysdl2                     lsdl
    -------------------        -------------------
    sdl2.SDLK_a                lsdl.kA
    sdl2.SDLK_RETURN           lsdl.RET
    sdl2.SDLK_F1               lsdl.F1

**lsdl** is an alternative wrapper to the core functionality granted by PySDL2.

                                    lsdl.py
                                      |
                  SDL2 --(ctypes)-- PySDL2 (sdl2.py)
                   |
                   C

             LSDL is Lion's PySDL2 Alternative Interface.


I invite you to use this however you like, make changes as you like,
share as you like.

I appreciate friendly notes and help requests at:

* LionKimbro@gmail.com
* 206.427.2545
* "Lion Kimbro" on Facebook


Lion Kimbro, 2014-05-03


[1]: http://www.libsdl.org/ "SDL2"
[2]: http://pysdl2.readthedocs.org/ "PySDL2"
