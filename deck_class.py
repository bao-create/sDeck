class deck:
    def __init__(self,dynaFlag):
        self.typef = dynaFlag
        self.node = []
        self.eles = []
        
        return
    def setNodeList(self,nodeObjectList):
        self.node =nodeObjectList
        return
    def appendNode(self,nodeObject):
        self.node = self.node + nodeObject
        return
    def setEleList(self,eleObjectList):
        self.eles = eleObjectList
        return
    def appendEle(self,eleObject):
        self.eles = self.eles + eleObject
        
        return
    