class deck:
    def __init__(self,dynaFlag):
        self.typef = dynaFlag
        self.node = {}
        self.eles = []
        
        
        return
    def setNodeList(self,nodeObjectDict):
        self.node = nodeObjectDict
        return
    def appendNode(self,nodeObject):
        self.node.update({str(nodeObject.getNid()):nodeObject}) 
        return
    def setEleList(self,eleObjectDict):
        self.eles = eleObjectDict
        return
    #def appendEle(self,eleObject): 
        #self.eles = self.eles + eleObject
        
        #return
    