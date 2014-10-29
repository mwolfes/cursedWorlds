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

            if key==ord('a'):
                mx+=2
                cw.refreshMap(my,mx,theSetting)
            if key==ord('d'):
                mx+=-2
                cw.refreshMap(my,mx,theSetting)
            if key==ord('w'):
                my+=-1
                cw.refreshMap(my,mx,theSetting)
            if key==ord('s'):
                my+=1
                cw.refreshMap(my,mx,theSetting)

            if key==ord('l'):
                player.x+=2
                cw.refreshMap(my,mx,theSetting)
            if key==ord('h'):
                player.x+=-2
                cw.refreshMap(my,mx,theSetting)
            if key==ord('k'):
                player.y+=-1
                cw.refreshMap(my,mx,theSetting)
            if key==ord('j'):
                player.y+=1
                cw.refreshMap(my,mx,theSetting)

            if key==ord('q'):
                break
        cw.quit()
    except:
        cw.quit()
        traceback.print_exc()

loop()
