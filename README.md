# 🌤️ MeteoApp - Application Météo Python

## Description

**MeteoApp** est une application météo graphique développée en Python qui permet aux utilisateurs d'obtenir des prévisions météorologiques précises pour n'importe quelle ville dans le monde. L'application offre une interface intuitive et moderne pour consulter la météo actuelle, les prévisions journalières et les prévisions sur une semaine.

## Fonctionnalités principales

- **Affichage multicités** : Vérifiez la météo de plusieurs villes internationales simultanément
- **Recherche de ville** : Recherchez et obtenez les prévisions pour n'importe quelle ville dans le monde
- **Prévisions détaillées** :
  - Météo actuelle (température, humidité, condition)
  - Prévisions journalières
  - Prévisions sur 7 jours
- **Interface utilisateur moderne** : Design élégant basé sur PySide6
- **Données en temps réel** : Intégration avec l'API Open-Meteo pour les données précises
- **Mise en cache** : Système de cache pour optimiser les performances
- **Géolocalisation** : Conversion des coordonnées GPS via l'API de géocodage

## Technologies utilisées

- **Framework UI** : PySide6 (Qt pour Python)
- **Requêtes HTTP** : Requests
- **API Météo** : [Open-Meteo](https://open-meteo.com/) (gratuit, sans clé)
- **API Géocodage** : Open-Meteo Geocoding
- **Langage** : Python 3.11+

## Utilisation

Pour lancer l'application :

```bash
python main.py
```

L'application va :
1. S'ouvrir avec une fenêtre affichant les prévisions de plusieurs villes internationales
2. Vous permettre de rechercher une ville spécifique via la barre de recherche
3. Afficher la météo actuelle, journalière et hebdomadaire pour la ville sélectionnée

## Structure du projet

```
MeteoAppPython/
├── main.py                          # Point d'entrée de l'application
├── style.qss                        # Feuille de styles Qt
├── README.md                        # Ce fichier
├── LICENSE                          # Licence du projet
│
├── api/                             # Module d'API météo
│   ├── check_status_api.py          # Vérification de l'état des API
│   ├── current_weather.py           # Récupération météo actuelle
│   ├── day_weather.py               # Prévisions journalières
│   ├── geocoding.py                 # Conversion lieu → coordonnées
│   └── week_weather.py              # Prévisions hebdomadaires
│
├── view/                            # Interface utilisateur
│   ├── body.py                      # Composant principal de recherche
│   ├── les_villes_internationales.py # Gestion des villes affichées
│   └── meteo_widget/                # Widgets de prévisions
│       ├── meteo_actuelle.py        # Affichage météo actuelle
│       ├── meteo_journee.py         # Affichage prévisions jour
│       └── meteo_semaine.py         # Affichage prévisions semaine
│
├── utilitaire/                      # Fonctions utilitaires
│   ├── conversion.py                # Conversions d'unités/données
│   ├── geocoding_cache.py           # Mise en cache du géocodage
│   ├── get_weather_icon.py          # Récupération des icônes météo
│   ├── load_image_url.py            # Chargement images depuis URL
│   └── weather_thread.py            # Gestion des threads météo
│
├── assets/                          # Ressources de l'application
│   └── weather_code.json            # Mapping codes météo → descriptions
│
└── cache/                           # Dossier de cache
    └── geocoding.csv                # Cache du géocodage
```

## API utilisées

### Open-Meteo API
L'application utilise l'API gratuite Open-Meteo pour récupérer :
- Les prévisions météorologiques actuelles et futures
- Les codes météo et descriptions
- La géolocalisation (conversion adresse → latitude/longitude)

**Avantage** : Aucune clé API requise, pas de limite de taux gratuit raisonnable

## Utilisation des données

1. **Recherche de ville** : Entrez le nom d'une ville dans la barre de recherche
2. **Sélection** : La première correspondance sera affichée
3. **Affichage** : Les prévisions s'actualisent automatiquement

## Personnalisation

### Thème et Styles
Modifiez le fichier `style.qss` pour personnaliser l'apparence de l'application.

### Villes affichées par défaut
Modifiez la liste `VILLES` dans `view/les_villes_internationales.py` pour afficher d'autres villes.

Consultez les commentaires TODO dans le code pour plus de détails.

## Documentation du code

Le code est documenté avec des commentaires et des docstrings. Les fonctions principales incluent :

- `get_current_weather()` : Récupère la météo actuelle
- `get_week_weather()` : Récupère les prévisions sur 7 jours
- `get_day_weather()` : Récupère les prévisions journalières
- `geocoding()` : Convertit un lieu en coordonnées GPS

## Licence

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteur

Yacine RAFES

