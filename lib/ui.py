import curses
from lib import world
from math import floor



class cWin:
    def __init__(self, parent, posy = 0.0, posx = 0.0 , sizey = 1.0, sizex = 1.0, level = 0 ):
        self.parent = parent
        self.level = level
        self.posy = posy
        self.posx = posx
        self.sizey = sizey
        self.sizex = sizex
        self.spacing = 1

        my, mx = self.parent.getmaxyx()
        yy = int(floor(my * posy)) + self.spacing
        xx = int(floor(mx * posx)) + self.spacing
        wy = int(floor(my * sizey))  - self.spacing
        wx = int(floor(mx * sizex))  - self.spacing

        self.win = curses.newwin(wy,wx,yy,xx)

    def getMaxYX(self):
        return self.win.getmaxyx()

    def refresh(self):
        self.win.noutrefresh()

class cWbox(cWin):
    def refresh(self):
        self.win.box()
        self.win.noutrefresh()

        
class cWinManager:
    def __init__(self):
        self.screen = curses.initscr()
        self.maxy,self.maxx = self.screen.getmaxyx()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        #if curses.has_colors():
            #curses.start_color()
        self.screen.keypad(1)
        self.screen.box()

        self.Tools = cWin(self.screen,0.0,0.0,0.8,0.1)
        self.Map = cWbox(self.screen,0.0,0.1,0.8,0.7)
        self.Legend = cWin(self.screen,0.0,0.8,0.8,0.19)
        self.Main = cWbox(self.screen,0.8,0.0,0.2,0.99)
        self.winlist = [self.Map,self.Tools,self.Legend,self.Main]

#       self.map = curses.newpad(75,75)
#       self.map.box()

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


