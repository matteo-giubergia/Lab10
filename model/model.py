import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self.stati = {}
        for s in DAO.getStati():
            self.stati[s.CCode] = s

    def buildGraph(self,anno):
        self._graph.add_nodes_from(DAO.getAllNodes(anno))


    def calcola(self, anno):
        self.buildGraph(anno)
        print(len(self._graph.nodes))



