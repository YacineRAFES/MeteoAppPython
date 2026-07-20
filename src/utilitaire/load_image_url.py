import urllib.request
from urllib.error import URLError, HTTPError


class LoadImageUrl:
    @staticmethod
    def load_image_url(url):
        try:
            data = urllib.request.urlopen(url).read()
            return data
        except (URLError, HTTPError) as e:
            print(f"Erreur lors du chargement de l'image: {e}")
            return None
