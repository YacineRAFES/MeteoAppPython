from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMessageBox, QHBoxLayout, QLabel, QPushButton, QGridLayout, QWidget, QDialog

def message_box(message):
    msgBox = QMessageBox()
    msgBox.setText(message)
    msgBox.exec()

def message_box_geocoding(data):
    fenetre = QDialog()
    fenetre.setWindowTitle("Sélection de la ville")

    # Les attributs pour stocker le résultat
    fenetre.result_id = None
    fenetre.result_city = None
    fenetre.result_country = None
    fenetre.result_region = None
    fenetre.result_department = None
    fenetre.result_town = None
    fenetre.result_latitude = None
    fenetre.result_longitude = None
    fenetre.result_code_country = None

    # Méthode pour stocker le résultat
    def set_result(
            id,
            city,
            country,
            region,
            department,
            town,
            latitude,
            longitude,
            code_country
    ):
        fenetre.result_id = id
        fenetre.result_city = city
        fenetre.result_country = country
        fenetre.result_region = region
        fenetre.result_department = department
        fenetre.result_town = town
        fenetre.result_latitude = latitude
        fenetre.result_longitude = longitude
        fenetre.result_code_country = code_country
        fenetre.accept()

    # Associe la méthode à l'objet fenetre
    fenetre.set_result = set_result

    layout = QGridLayout(fenetre)

    for i, entry in enumerate(data):
        pixmap = QPixmap("assets/01d@2x.png")
        icon = QLabel()
        icon.setPixmap(pixmap.scaled(32, 32))
        layout.addWidget(icon, i, 0)

        layout.addWidget(QLabel(entry["city"]), i, 1)
        layout.addWidget(QLabel(entry["country_code"]), i, 2)
        layout.addWidget(QLabel(entry["country"]), i, 3)
        layout.addWidget(QLabel(str(entry["latitude"])), i, 4)
        layout.addWidget(QLabel(str(entry["longitude"])), i, 5)

        bouton = QPushButton("Choisir")
        bouton.clicked.connect(
            lambda _,
                id=entry["id"],
                city=entry["city"],
                country=entry["country"],
                region=entry["region"],
                department=entry["department"],
                town=entry["town"],
                latitude=entry["latitude"],
                longitude=entry["longitude"],
                code_country=entry["country_code"],
                : fenetre.set_result(id, city, country, region, department, town, latitude, longitude, code_country)
        )
        layout.addWidget(bouton, i, 6)

    fenetre.exec()

    # Return avec les valeurs sélectionnées par l'utilisateur
    return {
        "id": fenetre.result_id,
        "city": fenetre.result_city,
        "country": fenetre.result_country,
        "region": fenetre.result_region,
        "department": fenetre.result_department,
        "town": fenetre.result_town,
        "latitude": fenetre.result_latitude,
        "longitude": fenetre.result_longitude,
        "code_country": fenetre.result_code_country
    }