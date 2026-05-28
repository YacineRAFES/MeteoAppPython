import requests



def get_geocoding(nomville):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={nomville}&count=10&language=en&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        json_results = response.json()
        city_lists = []

        for ville in json_results["results"]:
            city_data = {
                "id": ville.get("id"),
                "city": ville.get("name"),
                "country": ville.get("country"),
                "region": ville.get("admin1"),
                "department": ville.get("admin2"),
                "town": ville.get("admin3"),
                "latitude": ville.get("latitude"),
                "longitude": ville.get("longitude"),
                "code_country": ville.get("country_code")
            }

            city_lists.append(city_data)

        return city_lists
    elif response.status_code == 400:
        data = response.json()
        return {
            print(data["error"] + " : " + data["reason"])
        }
    else:
        return {
            print("Erreur lors de la requête : " + str(response.status_code))
        }
