import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.insiemeBorghi = set()
        self._grafo = nx.Graph()
        self.listaTuple = []
        self.listaMaggiori = []
        self.pesoMedio = 0

    def buildGraph(self, borgo):
        self._grafo.clear()
        codici = DAO.getNodi(borgo)
        for c in codici:
            self._grafo.add_node(c)
        self.addEdgesPesati()

    def addEdgesPesati(self):
        self.pesoMedio = 0
        self.listaTuple = []
        contatore = 0
        pTot = 0
        for n1 in self._grafo.nodes:
            for n2 in self._grafo.nodes:
                if n1 != n2:
                    if self._grafo.has_edge(n1, n2) is False:
                        peso = DAO.getPesoArchi(n1, n2)
                        if int(peso) > 0:
                            self.listaTuple.append((n1, n2, int(peso)))
                            pTot += int(peso)
                            contatore += 1
                            self._grafo.add_edge(n1, n2, weight=peso)
        self.pesoMedio = pTot/contatore

    def getBorghi(self):
        self.insiemeBorghi = set()
        borghi = DAO.get()
        for b in borghi:
            self.insiemeBorghi.add(b)
        return self.insiemeBorghi

    def getCaratteristicheGrafo(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getArchiMaggioriOrdinati(self):
        ordinata = sorted(self.listaTuple, key=lambda x: (-x[2], x[0], x[1]))
        for o in ordinata:
            if o[2] > self.pesoMedio:
                self.listaMaggiori.append(o)
        return self.listaMaggiori