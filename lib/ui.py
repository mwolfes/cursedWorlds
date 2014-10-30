import curses
from lib import world



class cWin:
    def __init__(self, parent, level = 0, posy = 0.0, posx = 0.0 , sizey = 1.0, sizex = 1.0 ):
        self.parent = parent
        self.level = level
        self.posy = posy
        self.posx = posx
        self.sizey = sizey
        self.sizex = sizex

        my, mx = self.parent.getmaxyx()

        self.win = curses.newwin(int(my * sizey),int(mx*sizex),int(my * posy),int(mx * posx))
        
class cWinManager:
    def __init__(self):
        self.screen = curses.initscr()
        self.maxy,self.maxx = self.screen.getmaxyx()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        if curses.has_colors():
            curses.start_color()
        self.screen.keypad(1)
        self.screen.box()

        self.map = curses.newpad(75,75)
        self.map.box()

    def quit(self):
        self.screen.keypad(0)
        curses.curs_set(1)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def refreshMap(self,my,mx,setting):
        self.screen.erase()
        self.screen.box()
        self.screen.refresh()
        #redraw the map
        self.map.erase()
        self.map.box() #for testing, remove at the end??? 
        #place all objects
        for entity in setting.entities:
            if entity.getShape():
                self.map.addstr(entity.y,entity.x,entity.getShape()[0])
        self.map.refresh(my,mx,1,1,self.maxy - 3,self.maxx-2)

    def resizeTerm(self):
        self.maxy,self.maxx = self.screen.getmaxyx()
        self.screen.clear()
        curses.resizeterm(maxy,maxx)
        self.screen.box()
        self.screen.refresh()

