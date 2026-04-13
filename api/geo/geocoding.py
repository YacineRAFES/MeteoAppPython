import requests


class GeoCoding:
    @staticmethod
    def GetGeo(nomville):
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={nomville}&count=1&language=en&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "latitude": data["results"][0]["latitude"],
                "longitude": data["results"][0]["longitude"],
                "code_country": data["results"][0]["country_code"]
            }
        elif response.status_code == 400:
            data = response.json()
            return {
                print(data["error"] + " : " + data["reason"])
            }
        else:
            return {
                print("Erreur lors de la requête : " + str(response.status_code))
            }
