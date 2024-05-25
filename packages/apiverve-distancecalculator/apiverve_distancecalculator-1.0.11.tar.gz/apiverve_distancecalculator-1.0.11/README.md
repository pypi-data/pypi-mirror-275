Distance Calculator API
============

Distance Calculator is a simple tool for calculating the distance between two locations. It returns the distance in miles and kilometers.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Distance Calculator API](https://apiverve.com/marketplace/api/distancecalculator)

---

## Installation
	pip install apiverve-distancecalculator

---

## Configuration

Before using the distancecalculator API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Distance Calculator API documentation is found here: [https://docs.apiverve.com/api/distancecalculator](https://docs.apiverve.com/api/distancecalculator).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_distancecalculator.apiClient import DistancecalculatorAPIClient

# Initialize the client with your APIVerve API key
api = DistancecalculatorAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "lat1": 36.7783,  "lon1": -119.4179,  "lat2": 34.0522,  "lon2": -118.2437 }
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
    "distanceMiles": 199.6804337234997,
    "distanceKm": 321.25354627586279,
    "location1": {
      "latitude": "36.728450",
      "longitude": "-119.53571",
      "city": "Sanger",
      "state": "California"
    },
    "location2": {
      "zipcode": "90013",
      "latitude": "34.044662",
      "longitude": "-118.24255",
      "city": "Los Angeles",
      "state": "California"
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