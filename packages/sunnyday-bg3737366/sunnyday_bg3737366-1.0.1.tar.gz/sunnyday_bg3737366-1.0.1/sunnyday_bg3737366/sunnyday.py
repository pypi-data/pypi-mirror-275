import requests

class Weather:
    def __init__(self, city=None, lat=None, lon=None):
        """prints weather"""
        api_key = "73b208fd708d74b4969af3f3ac69babd"
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=metric"
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={api_key}&units=metric"
        else:
            raise TypeError("provide City or Latitude and Longitude")

        if url:
            r = requests.get(url)
            self.data = r.json()

        if self.data['cod'] != "200":
            raise ValueError(self.data['message'])

    def next_12hr(self):
        return self.data['list'][:4]

    def next_12hr_simplified(self):
        data = []
        for dicty in self.data['list'][:4]:
            data.append((dicty['dt_txt'],
                    dicty['main']['temp'],
                    dicty['weather'][0]['description']))
        return data

if __name__ == "__main__":
    weather = Weather(city="Madrid")
    print(weather.data)