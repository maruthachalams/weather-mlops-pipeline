import requests 

class MyScraper:
    def __init__(self):
        self.target_url = "https://wttr.in/coimbatore?format=j1"
        self.target_place = "coimbatore"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    def fetch_data(self):
        response = requests.get(self.target_url)
        weather_dict = response.json()
        current_temp = weather_dict["current_condition"][0]["temp_C"]
        return {"city": self.target_place, "temperature" : current_temp}
