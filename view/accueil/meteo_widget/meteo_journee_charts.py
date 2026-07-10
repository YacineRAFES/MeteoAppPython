from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patheffects as path_effects


class MeteoJourneeCharts(QWidget):
    def __init__(self, nomville):
        super().__init__()
        self.nomville = nomville

        print("MeteoJourneeCharts : ", self.nomville)


        # Créer un layout pour le graphique
        self.meteo_journee_charts = QVBoxLayout()
        self.setLayout(self.meteo_journee_charts)

        self.setMinimumHeight(250)

    def maj_charts(self, data):

        # enregistre les données dans les variables
        heure_dict = data.get_all_times()
        temp_dict = data.get_all_temperatures()

        # figure matplotlib graphique pour la température
        fig = Figure()
        ax = fig.subplots(1, 1)
        min_temp = min(temp_dict) - 4
        max_temp = max(temp_dict) + 4
        ax.set_ylim(min_temp, max_temp)
        for x, y in zip(heure_dict, temp_dict):
            ax.annotate(str(y),
                        xy=(x, y),
                        xytext=(0, 10),
                        textcoords="offset points",
                        ha='center',
                        fontsize=10,
                        color='black',
                        path_effects=[
                            path_effects.withStroke(
                                linewidth=5,      # Épaisseur du contour
                                foreground='white' # Couleur du contour
                            )
                        ])
        ax.plot(heure_dict, temp_dict, '.-')
        ax.set_title("Températures aujourd'hui")



        # Créer un canvas pour afficher la figure dans Qt
        canvas = FigureCanvas(fig)

        canvas.wheelEvent = self.canvas_wheel_event

        # Ajouter le canvas au layout
        self.meteo_journee_charts.addWidget(canvas)

    def vider(self):
        while self.meteo_journee_charts.count():
            item = self.meteo_journee_charts.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def canvas_wheel_event(self, event):
        event.ignore()
