Weather API
============

Weather is a simple tool for getting the current weather. It returns the temperature, humidity, and more for a given location.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Weather API](https://apiverve.com/marketplace/api/weatherforecast)

---

## Installation
	pip install apiverve-weather

---

## Configuration

Before using the weatherforecast API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Weather API documentation is found here: [https://docs.apiverve.com/api/weatherforecast](https://docs.apiverve.com/api/weatherforecast).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_weather.apiClient import WeatherforecastAPIClient

# Initialize the client with your APIVerve API key
api = WeatherforecastAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "city": "San Francisco" }
```

###### Simple Request

```
# Make a request to the API
result = api.execute(query)

# Print the result
print(result)
```

###### Example Response

```
{
  "status": "ok",
  "error": null,
  "data": {
    "location": {
      "name": "San Francisco",
      "region": "California",
      "country": "United States of America",
      "lat": 37.78,
      "lon": -122.42,
      "tz_id": "America/Los_Angeles",
      "localtime_epoch": 1715809997,
      "localtime": "2024-05-15 14:53"
    },
    "current": {
      "tempC": 17.2,
      "tempF": 63,
      "windMph": 16.1,
      "windKph": 25.9,
      "windDegree": 300,
      "windDir": "WNW",
      "pressureMb": 1013,
      "pressureIn": 29.91,
      "precipMm": 0,
      "precipIn": 0,
      "feelslikeC": 17.2,
      "feelslikeF": 63,
      "visKm": 16,
      "visMiles": 9,
      "gustMph": 20.6,
      "gustKph": 33.1
    },
    "forecast": {
      "forecastday": [
        {
          "date": "2024-05-15",
          "date_epoch": 1715731200,
          "day": {
            "maxtemp_c": 16.7,
            "maxtemp_f": 62.1,
            "mintemp_c": 10.9,
            "mintemp_f": 51.6,
            "avgtemp_c": 13.6,
            "avgtemp_f": 56.6,
            "maxwind_mph": 13.2,
            "maxwind_kph": 21.2,
            "totalprecip_mm": 0.06,
            "totalprecip_in": 0,
            "totalsnow_cm": 0,
            "avgvis_km": 10,
            "avgvis_miles": 6,
            "avghumidity": 80,
            "daily_will_it_rain": 0,
            "daily_chance_of_rain": 0,
            "daily_will_it_snow": 0,
            "daily_chance_of_snow": 0,
            "condition": {
              "text": "Sunny",
              "code": 1000
            },
            "uv": 9
          }
        },
        {
          "date": "2024-05-16",
          "date_epoch": 1715817600,
          "day": {
            "maxtemp_c": 17.3,
            "maxtemp_f": 63.1,
            "mintemp_c": 12,
            "mintemp_f": 53.5,
            "avgtemp_c": 14,
            "avgtemp_f": 57.2,
            "maxwind_mph": 12.8,
            "maxwind_kph": 20.5,
            "totalprecip_mm": 0.06,
            "totalprecip_in": 0,
            "totalsnow_cm": 0,
            "avgvis_km": 10,
            "avgvis_miles": 6,
            "avghumidity": 81,
            "daily_will_it_rain": 0,
            "daily_chance_of_rain": 0,
            "daily_will_it_snow": 0,
            "daily_chance_of_snow": 0,
            "condition": {
              "text": "Sunny",
              "code": 1000
            },
            "uv": 8
          }
        },
        {
          "date": "2024-05-17",
          "date_epoch": 1715904000,
          "day": {
            "maxtemp_c": 17,
            "maxtemp_f": 62.6,
            "mintemp_c": 11.5,
            "mintemp_f": 52.7,
            "avgtemp_c": 13.9,
            "avgtemp_f": 57,
            "maxwind_mph": 12.3,
            "maxwind_kph": 19.8,
            "totalprecip_mm": 0.05,
            "totalprecip_in": 0,
            "totalsnow_cm": 0,
            "avgvis_km": 10,
            "avgvis_miles": 6,
            "avghumidity": 78,
            "daily_will_it_rain": 0,
            "daily_chance_of_rain": 0,
            "daily_will_it_snow": 0,
            "daily_chance_of_snow": 0,
            "condition": {
              "text": "Sunny",
              "code": 1000
            },
            "uv": 9
          }
        }
      ]
    }
  }
}
```

---

## Customer Support

Need any assistance? [Get in touch with Customer Support](https://apiverve.com/contact).

---

## Updates
Stay up to date by following [@apiverveHQ](https://twitter.com/apiverveHQ) on Twitter.

---

## Legal

All usage of the APIVerve website, API, and services is subject to the [APIVerve Terms of Service](https://apiverve.com/terms) and all legal documents and agreements.

---

## License
Licensed under the The MIT License (MIT)

Copyright (&copy;) 2024 APIVerve, and Evlar LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.