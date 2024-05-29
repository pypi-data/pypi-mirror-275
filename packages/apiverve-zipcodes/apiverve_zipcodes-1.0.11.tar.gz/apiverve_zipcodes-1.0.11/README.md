Zip Codes API
============

Zip Codes is a simple tool for looking up zip codes. It returns the city, state, and more of a zip code.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Zip Codes API](https://apiverve.com/marketplace/api/zipcodes)

---

## Installation
	pip install apiverve-zipcodes

---

## Configuration

Before using the zipcodes API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Zip Codes API documentation is found here: [https://docs.apiverve.com/api/zipcodes](https://docs.apiverve.com/api/zipcodes).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_zipcodes.apiClient import ZipcodesAPIClient

# Initialize the client with your APIVerve API key
api = ZipcodesAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "city": "San Francisco",  "state": "CA" }
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
    "search": "San Francisco",
    "foundCities": [
      {
        "zipcode": "94102",
        "state_abbr": "CA",
        "latitude": "37.779329",
        "longitude": "-122.41915",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94103",
        "state_abbr": "CA",
        "latitude": "37.772329",
        "longitude": "-122.41087",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94104",
        "state_abbr": "CA",
        "latitude": "37.791728",
        "longitude": "-122.40190",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94105",
        "state_abbr": "CA",
        "latitude": "37.789228",
        "longitude": "-122.39570",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94107",
        "state_abbr": "CA",
        "latitude": "37.766529",
        "longitude": "-122.39577",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94108",
        "state_abbr": "CA",
        "latitude": "37.792678",
        "longitude": "-122.40793",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94109",
        "state_abbr": "CA",
        "latitude": "37.792778",
        "longitude": "-122.42188",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94110",
        "state_abbr": "CA",
        "latitude": "37.748730",
        "longitude": "-122.41545",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94111",
        "state_abbr": "CA",
        "latitude": "37.798228",
        "longitude": "-122.40027",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94112",
        "state_abbr": "CA",
        "latitude": "37.720931",
        "longitude": "-122.44241",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94114",
        "state_abbr": "CA",
        "latitude": "37.758434",
        "longitude": "-122.43512",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94115",
        "state_abbr": "CA",
        "latitude": "37.786129",
        "longitude": "-122.43736",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94116",
        "state_abbr": "CA",
        "latitude": "37.743381",
        "longitude": "-122.48578",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94117",
        "state_abbr": "CA",
        "latitude": "37.770937",
        "longitude": "-122.44276",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94118",
        "state_abbr": "CA",
        "latitude": "37.782029",
        "longitude": "-122.46158",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94121",
        "state_abbr": "CA",
        "latitude": "37.778729",
        "longitude": "-122.49265",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94122",
        "state_abbr": "CA",
        "latitude": "37.758380",
        "longitude": "-122.48478",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94123",
        "state_abbr": "CA",
        "latitude": "37.801028",
        "longitude": "-122.43836",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94124",
        "state_abbr": "CA",
        "latitude": "37.732797",
        "longitude": "-122.39348",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94127",
        "state_abbr": "CA",
        "latitude": "37.734964",
        "longitude": "-122.45970",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94128",
        "state_abbr": "CA",
        "latitude": "37.621964",
        "longitude": "-122.39534",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94129",
        "state_abbr": "CA",
        "latitude": "37.799840",
        "longitude": "-122.46167",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94130",
        "state_abbr": "CA",
        "latitude": "37.819423",
        "longitude": "-122.36966",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94131",
        "state_abbr": "CA",
        "latitude": "37.741797",
        "longitude": "-122.43780",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94132",
        "state_abbr": "CA",
        "latitude": "37.724231",
        "longitude": "-122.47958",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94133",
        "state_abbr": "CA",
        "latitude": "37.801878",
        "longitude": "-122.41018",
        "city": "San Francisco",
        "state": "California"
      },
      {
        "zipcode": "94134",
        "state_abbr": "CA",
        "latitude": "37.719581",
        "longitude": "-122.41085",
        "city": "San Francisco",
        "state": "California"
      }
    ]
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