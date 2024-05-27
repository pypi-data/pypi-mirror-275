Sunrise Sunset API
============

Sunrise Sunset is a simple tool for getting the sunrise and sunset times. It returns the sunrise and sunset times for a given location and date.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Sunrise Sunset API](https://apiverve.com/marketplace/api/sunrisesunset)

---

## Installation
	pip install apiverve-sunrisesunset

---

## Configuration

Before using the sunrisesunset API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Sunrise Sunset API documentation is found here: [https://docs.apiverve.com/api/sunrisesunset](https://docs.apiverve.com/api/sunrisesunset).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_sunrisesunset.apiClient import SunrisesunsetAPIClient

# Initialize the client with your APIVerve API key
api = SunrisesunsetAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "lat": 36.7201600,  "lon": -4.4203400,  "date": "05-26-2024" }
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
    "solarNoon": "2024-05-15T12:15:25.531Z",
    "nadir": "2024-05-15T00:15:25.531Z",
    "sunrise": "2024-05-15T05:11:29.338Z",
    "sunset": "2024-05-15T19:19:21.723Z",
    "sunriseEnd": "2024-05-15T05:14:24.538Z",
    "sunsetStart": "2024-05-15T19:16:26.523Z",
    "dawn": "2024-05-15T04:42:35.513Z",
    "dusk": "2024-05-15T19:48:15.548Z",
    "nauticalDawn": "2024-05-15T04:07:16.944Z",
    "nauticalDusk": "2024-05-15T20:23:34.117Z",
    "nightEnd": "2024-05-15T03:29:03.56Z",
    "night": "2024-05-15T21:01:47.501Z",
    "goldenHourEnd": "2024-05-15T05:48:14.811Z",
    "goldenHour": "2024-05-15T18:42:36.25Z"
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