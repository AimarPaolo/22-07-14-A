import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page, *args, **kwargs):
        # page stuff
        super().__init__(*args, **kwargs)
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.ddBorgo = None
        self.txtProbabilita = None
        self.txtDurata=None
        self.btn_graph = None
        self.btn_analisiArchi= None
        self.btn_Simula = None

        self.txt_result = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame del 14/07/2022 - NYC-Hotspots", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddBorgo = ft.Dropdown(label="Borgo")
        self._controller.fillDD()
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)

        row1 = ft.Row([self.ddBorgo, ft.Container(None, width=230),self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._controller.fillDD()

        # List View where the reply is printed
        self.btn_analisiArchi = ft.ElevatedButton(text="AnalisiArchi", on_click=self._controller.handle_analisi, disabled=True)
        self.txtProbabilita = ft.TextField(label="Probabilità")
        self.btn_Simula = ft.ElevatedButton(text="Simula", on_click=self._controller.handle_simula, disabled=True)
        row2 = ft.Row([ft.Container(None, width=250),ft.Container(None, width=250),self.btn_analisiArchi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        row3 = ft.Row([self.txtProbabilita, ft.Container(None, width=250),self.btn_Simula],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        self.txtDurata=ft.TextField(label="Durata")
        row4 = ft.Row([self.txtDurata, ft.Container(None, width=200), ft.Container(None, width=140)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)



        self.txt_result = ft.ListView(expand=1, spacing=5, padding=5, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()


    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()