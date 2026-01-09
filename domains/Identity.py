class Identity:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def getID(self):
        return self._id
    
    def setName(self, name):
        self._name = name
    def getName(self):
        return self._name