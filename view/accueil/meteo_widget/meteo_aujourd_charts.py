from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MeteoAujourdhuiCharts(QWidget):
    def __init__(self):
        super().__init__()

        # Créer un layout pour le graphique
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Créer les données du graphique
        x = np.linspace(0, 2 * np.pi, 200)
        y = np.sin(x)

        # Créer une figure matplotlib
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title("Températures aujourd'hui")

        # Créer un canvas pour afficher la figure dans Qt
        canvas = FigureCanvas(fig)

        # Ajouter le canvas au layout
        layout.addWidget(canvas)
