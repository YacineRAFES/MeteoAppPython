from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from matplotlib import ticker
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def canvas_wheel_event(event):
    event.ignore()


class MeteoJourneeCharts(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoJourneeCharts : ", self.nomville)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_principal)

        # Créer un layout pour le graphique
        self.meteo_journee_charts = QHBoxLayout()

        self.setMinimumHeight(250)

        meteo_journee_charts = QWidget()
        meteo_journee_charts.setObjectName("meteo_actuelle")
        meteo_journee_charts.setLayout(self.meteo_journee_charts)

        self.layout_principal.addWidget(meteo_journee_charts)

    def maj_charts_temperature(self, data):

        # enregistre les données dans les variables
        heure_dict = data.get_all_times()
        temp_dict = data.get_all_temperatures()

        # figure matplotlib graphique pour la température
        fig = Figure(layout="tight")
        ax = fig.subplots(1, 1)

        # Transparence de la figure et la zone de tracé
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

        min_temp = min(temp_dict) - 4
        max_temp = max(temp_dict) + 4
        ax.set_ylim(min_temp, max_temp)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
        for x, y in zip(heure_dict, temp_dict):
            ax.annotate(str(y),
                        xy=(x, y),
                        xytext=(0, 10),
                        textcoords="offset points",
                        ha='center',
                        fontsize=10,
                        color='black')
        ax.plot(heure_dict, temp_dict, '.-')
        ax.set_title("Températures")

        # Créer un canvas pour afficher la figure dans Qt
        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background-color:transparent;")

        canvas.wheelEvent = canvas_wheel_event

        # Ajouter le canvas au layout
        self.meteo_journee_charts.addWidget(canvas)

    def maj_charts_precipitation(self, data):

        # enregistre les données dans les variables
        heure_dict = data.get_all_times()
        precipitation_dict = data.get_all_precipitations()

        if all(p == 0 for p in precipitation_dict):
            return

        # figure matplotlib graphique pour la précipitation
        fig = Figure(layout="tight")
        ax = fig.subplots(1, 1)

        # Transparence de la figure et la zone de tracé
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

        ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
        for x, y in zip(heure_dict, precipitation_dict):
            ax.annotate(str(y),
                        xy=(x, y),
                        xytext=(0, 10),
                        textcoords="offset points",
                        ha='center',
                        fontsize=10,
                        color='black')
        ax.bar(heure_dict, precipitation_dict, color='#1f77b4')
        ax.set_title("Précipitations (mm)")

        # Créer un canvas pour afficher la figure dans Qt
        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background-color:transparent;")

        canvas.wheelEvent = canvas_wheel_event

        # Ajouter le canvas au layout
        self.meteo_journee_charts.addWidget(canvas)

    def vider(self):
        while self.meteo_journee_charts.count():
            item = self.meteo_journee_charts.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
