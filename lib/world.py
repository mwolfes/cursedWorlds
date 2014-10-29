class entity:
    def __init__(self,ypos,xpos):
        self.y = ypos
        self.x = xpos
    def getShape(self):
        return []

class player(entity):
    def __init__(self,ypos,xpos,name):
        self.y = ypos
        self.x = xpos
        self.name = name
    def getShape(self):
        return ["+"]

class setting:
    def __init__(self,entities = []):
        self.entities = entities
