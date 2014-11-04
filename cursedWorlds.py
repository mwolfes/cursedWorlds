#!/usr/bin/python
from lib.ui import cWinManager
from lib import world
import traceback
import curses

cw = cWinManager()
#player = world.player(10,20,"mesiter")
#theSetting = world.setting([player])

class states:
    onMap, onToolbar, onMain, onLegend = range(4)

def loop():
    try:
        while True:
            key = cw.screen.getch()

            if key == curses.KEY_RESIZE:
                cw.resize()

            if key == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()

                win = cw.getWindow(my,mx)
                if win:
                    win.win.addstr(1,1,"HERE")
                cw.refresh()
                #wy,wx = cw.Map.win.getparyx()
                #cw.Map.win.erase()
                #cw.screen.addstr(my,mx,str(my - wy) + "  " + str(mx - wx))
                #cw.refresh()

            if key==ord('q'):
                break

        cw.quit()
    except:
        cw.quit()
        traceback.print_exc()

loop()
