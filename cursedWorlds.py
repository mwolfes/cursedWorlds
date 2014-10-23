#!/usr/bin/python
from lib.ui import cWinManager
from lib import world
import traceback
import curses


cw = cWinManager()
player = world.player(10,20,"mesiter")
theSetting = world.setting([player])

def loop():
    mx = 0
    my = 0
    try:
        while True:
            key = cw.screen.getch()
            if key==curses.KEY_RESIZE:
                cw.resizeTerm()

            if key==ord('l'):
                mx+=2
                cw.refreshMap(my,mx)
            if key==ord('h'):
                mx+=-2
                cw.refreshMap(my,mx)
            if key==ord('k'):
                my+=-1
                cw.refreshMap(my,mx)
            if key==ord('j'):
                my+=+1
                cw.refreshMap(my,mx)

            if key==ord('q'):
                break
        cw.quit()
    except:
        cw.quit()
        traceback.print_exc()

loop()