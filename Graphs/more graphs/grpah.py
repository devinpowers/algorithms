class Vertex(object):
    
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self,neighbor,weight=0):
        self.connectedTo[neighbor] = weight
        
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
    
    def __str__(self):
        return str(self.id)
    
# Graph object
class Graph(object):
    
    def __init__(self):
        self.masterList = {}
        self.totalNum = 0
    
    def addVertex(self, key):
        self.totalNum += 1
        newVertex = Vertex(key)
        self.masterList[key] = newVertex
        return newVertex
    
    def getVertex(self,n):
        if n in self.masterList:
            return self.masterList[n]
        else:
            return None
    
    def addEdge(self, fromV, toV, weight=0): 
        if fromV not in self.masterList:
            self.addVertex(fromV)
        if toV not in self.masterList:
            self.addVertex(toV)
        
        self.masterList[fromV].addNeighbor(self.addVertex(toV), weight)
        
    def getVertices(self):
        return self.masterList.keys()
    
    def __iter__(self):
        # this sepcial function allows us to iterate through master list
        return iter(self.masterList.values())
    
    def __contains__(self,n):
        # this special function allows us to use IN operator
        if n in self.masterList:
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    
    g.addEdge(0,1,5)
    # iteration through the master list
    for vert in g:
        print(vert)
    