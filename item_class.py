class item:
    def __init__(self,line):
        parts = line.split()
        self.nid = parts[1]
        self.xyz = parts[2:]
    def getxyz(self):
        return self.xyz
    def getEid(self):
        return self.nid


class node(item):
    pass

class cquad4(item):
    pass
    
class cquad8(item):
    pass
    
class ctetra4(item):
    pass
    
class chexa(item):
    pass
    

class eleObject:
    def __init__(self):
        self.dynaEls = []
        self.cquad4Ele = []
        self.cquad8Ele = []
        self.ctetra4Ele = []
        self.chexaEle = []
        return
    def addDynaEle(self,item):
        self.dynaEls = self.dynaEls + item
        return
    def addcquad4Ele(self,item):
        self.dcquad4Els = self.cquad4Els + item
        return
    def addcquad8Ele(self,item):
        self.cqaud8Els = self.cquad8Els + item
        return
    def addctetra4Ele(self,item):
        self.ctetra4Els = self.ctetra4Els + item
        return
    def addchexaEle(self,item):
        self.chexaEls = self.chexaEls + item
        return
