Card Generator API
============

Card Generator is a simple tool for generating test/sample card numbers. It returns a list of card numbers for testing.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Card Generator API](https://apiverve.com/marketplace/api/cardgenerator)

---

## Installation
	pip install apiverve-cardgenerator

---

## Configuration

Before using the cardgenerator API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Card Generator API documentation is found here: [https://docs.apiverve.com/api/cardgenerator](https://docs.apiverve.com/api/cardgenerator).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_cardgenerator.apiClient import CardgeneratorAPIClient

# Initialize the client with your APIVerve API key
api = CardgeneratorAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "brand": "visa",  "count": 5 }
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
    "brand": "visa",
    "count": 5,
    "cards": [
      {
        "cvv": 610,
        "issuer": "NATIONAL BANK OF UMM AL-QAIWAIN PSC.",
        "number": "4797343479420732",
        "expiration": "2029-05-15T21:49:17.139Z",
        "brand": "visa",
        "number_alt": "4797 3434 7942 0732"
      },
      {
        "cvv": 753,
        "issuer": "CB KOLTSO URALA",
        "number": "4272242937720507",
        "expiration": "2029-05-15T21:49:17.15Z",
        "brand": "visa",
        "number_alt": "4272 2429 3772 0507"
      },
      {
        "cvv": 269,
        "issuer": "BANKMED S.A.L.",
        "number": "4067387803515132",
        "expiration": "2029-05-15T21:49:17.152Z",
        "brand": "visa",
        "number_alt": "4067 3878 0351 5132"
      },
      {
        "cvv": 507,
        "issuer": "BANK LEUMI LE-ISRAEL B.M.",
        "number": "4580423754659492",
        "expiration": "2029-05-15T21:49:17.154Z",
        "brand": "visa",
        "number_alt": "4580 4237 5465 9492"
      },
      {
        "cvv": 147,
        "issuer": "NMB BANK, LTD.",
        "number": "4027239824895648",
        "expiration": "2029-05-15T21:49:17.156Z",
        "brand": "visa",
        "number_alt": "4027 2398 2489 5648"
      }
    ],
    "owner": {
      "name": "Johnathan Graham",
      "address": {
        "street": "4233 Kris Forges",
        "city": "New Jeffereyshire",
        "state": "Michigan",
        "zipCode": "09601-1440"
      }
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