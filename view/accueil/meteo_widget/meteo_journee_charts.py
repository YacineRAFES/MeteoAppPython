from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MeteoJourneeCharts(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un layout pour le graphique
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.setMinimumHeight(250)


        # Créer une figure matplotlib
        fig = Figure()
        ax = fig.subplots(1, 1)
        ax.plot(["11:00", "14:00", "15:00", "16:00"], [34, 36, 38, 39])
        ax.set_title("Températures aujourd'hui")

        # Créer un canvas pour afficher la figure dans Qt
        canvas = FigureCanvas(fig)

        canvas.wheelEvent = self.canvas_wheel_event

        # Ajouter le canvas au layout
        layout.addWidget(canvas)

    def canvas_wheel_event(self, event):
        event.ignore()

    def maj_charts(self):
        meteoHeure = QVBoxLayout()

