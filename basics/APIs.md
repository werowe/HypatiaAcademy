

Sign up for free access to OpenWeather API [here](https://rapidapi.com/community/api/open-weather-map).


```python
import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"London%2Cuk"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

```
