import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for r in sorted(self._model.getBorghi()):
            self._view.ddBorgo.options.append(ft.dropdown.Option(r))



    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        if self._view.ddBorgo.value is None:
            self._view.txt_result.controls.append(ft.Text("Non hai selezionato un borgo"))
            self._view.update_page()
            return
        self._model.buildGraph(self._view.ddBorgo.value)
        nNodes, nEdges = self._model.getCaratteristicheGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi e {nEdges} archi"))
        self._view.btn_analisiArchi.disabled = False
        self._view.btn_Simula.disabled = False

        self._view.update_page()

    def handle_analisi(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Il peso medio degli archi vale: {self._model.pesoMedio}"))
        for n1, n2, peso in self._model.getArchiMaggioriOrdinati():
            print(n1)
            self._view.txt_result.controls.append(ft.Text(f"Arco da {n1} a {n2} con peso={peso}"))
        self._view.update_page()

    def handle_simula(self, e):
        pass
