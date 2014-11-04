import curses
from lib import world
from math import floor



class cWin:
    def __init__(self, parent, posy = 0.0, posx = 0.0 , sizey = 1.0, sizex = 1.0, level = 0 ):
        self.parent = parent
        self.level = level
        self._posy = posy
        self._posx = posx
        self._sizey = sizey
        self._sizex = sizex
        self.spacing = 0
        yy, xx , wy , wx = self.getWinDimensions()
        self.win = parent.subwin(wy,wx,yy,xx)

    def getWinDimensions(self):
        my, mx = self.parent.getmaxyx()
        yy = int(floor(my * self._posy)) + self.spacing
        xx = int(floor(mx * self._posx)) + self.spacing
        wy = int(floor(my * self._sizey))  - self.spacing
        wy -= wy % 2
        wx = int(floor(mx * self._sizex))  - self.spacing
        wx -= wx % 2
        return ( yy, xx , wy , wx )

    def getMaxYX(self):
        return self.win.getmaxyx()

    def refresh(self):
        self.win.noutrefresh()

class cWbox(cWin):
    def refresh(self):
        self.win.box()
        self.win.noutrefresh()

        
class cWinManager:

    def _init_wins(self):
        self.Tools = cWbox(self.screen,0.0,0.0,0.7,0.1)
        self.Map = cWbox(self.screen,0.0,0.1,0.7,0.7)
        self.Legend = cWbox(self.screen,0.0,0.8,0.7,0.2)
        self.Main = cWbox(self.screen,0.7,0.0,0.3,1)
        self.winlist = [self.Map,self.Tools,self.Legend,self.Main]

    def __init__(self):
        self.screen = curses.initscr()
        self.maxy,self.maxx = self.screen.getmaxyx()
        self.maxx -= self.maxx % 2
        self.maxy -= self.maxy % 2
        curses.resizeterm(self.maxy,self.maxx)

        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        if curses.has_colors():
            curses.start_color()
        self.screen.keypad(1)
        curses.mousemask(1)

        self._init_wins()
        self.refresh()



    def resize(self):
        self.screen.erase()
        self._init_wins()
        self.refresh()

    def refresh(self):
        self.screen.noutrefresh()
        for win in self.winlist:
            win.refresh()
        curses.doupdate()

    def quit(self):
        self.screen.keypad(0)
        curses.curs_set(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def getWindow(self, y , x):
        for entry in self.winlist:
            if entry.win.enclose(y,x):
                return entry
        return 0

#   def refreshMap(self,my,mx,setting):
#       self.screen.erase()
#       self.screen.box()
#       self.screen.refresh()
#       #redraw the map
#       self.map.erase()
#       self.map.box() #for testing, remove at the end??? 
#       #place all objects
#       for entity in setting.entities:
#           if entity.getShape():
#               self.map.addstr(entity.y,entity.x,entity.getShape()[0])
#       self.map.refresh(my,mx,1,1,self.maxy - 3,self.maxx-2)
#
#   def resizeTerm(self):
#       self.maxy,self.maxx = self.screen.getmaxyx()
#       self.screen.clear()
#       curses.resizeterm(maxy,maxx)
#       self.screen.box()
#       self.screen.refresh()


