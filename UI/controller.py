import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno != ""  and int(anno)<= 2016 and int(anno)>=1816:
            self._model.calcola(anno)
        else:
            self._view.create_alert("anno non valido")




