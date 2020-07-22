class item:
    def __init__(self,line):
        parts = line.split()
        self.eid = parts[1]
        self.nodes = parts[2:]
    
    def getEid(self):
        return self.eid
    def getNodes(self):
        return self.nodes


class node(item):
    def __init__(self,line):
        parts = line.split()
        self.nid = parts[1]
        self.xyz = parts[2:]
    
    def getNid(self):
        return self.nid
    def getxyz(self):
        return self.xyz
    pass

class cquad4(item):
    pass
    
class cquad8(item):
    pass
    
class ctetra4(item):
    pass
    
class chexa(item):
    pass
class ELE_SOLID(item):
    pass
class ELE_SHELL(item):
    pass
    

class eleObject:
    def __init__(self):
        self.ELE_SOLID = {}
        self.ELE_SHELL = {}
        self.cquad4Ele = {}
        self.cquad8Ele = {}
        self.ctetra4Ele = {}
        self.chexaEle = {}
        return
    def addELE_SOLID(self,item):
        self.ELE_SOLID.update({str(item.getEid):item})
        return
    def addELE_SHELL(self,item):
        self.ELE_SHEL.update({str(item.getEid):item})   
    def addcquad4Ele(self,item):
        self.dcquad4Els.update({str(item.getEid):item})
        return
    def addcquad8Ele(self,item):
        self.cqaud8Els.update({str(item.getEid):item})
        return
    def addctetra4Ele(self,item):
        self.ctetra4Els.update({str(item.getEid):item})
        return
    def addchexaEle(self,item):
        self.chexaEls.update({str(item.getEid):item})
        return
