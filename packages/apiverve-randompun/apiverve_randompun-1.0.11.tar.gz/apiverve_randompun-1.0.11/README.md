Random Pun API
============

Random Pun is a simple tool for getting random puns. It returns a random pun from a collection of puns.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Random Pun API](https://apiverve.com/marketplace/api/randompun)

---

## Installation
	pip install apiverve-randompun

---

## Configuration

Before using the randompun API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Random Pun API documentation is found here: [https://docs.apiverve.com/api/randompun](https://docs.apiverve.com/api/randompun).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_randompun.apiClient import RandompunAPIClient

# Initialize the client with your APIVerve API key
api = RandompunAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
This API does not require a Query
```

###### Simple Request

```
# Make a request to the API
result = api.execute()

# Print the result
print(result)
```

###### Example Response

```
{
  "status": "ok",
  "error": null,
  "data": {
    "category": "Lawyers",
    "rating": 3,
    "pun": "A local United Way office realized that the organization had never received a donation from the town's most successful lawyer. The person in charge of contributions called him to persuade him to contribute.'Our research shows that out of a yearly income of at least $500,000, you give not a penny to charity. Wouldn't you like to give back to the community in some way?'The lawyer mulled this over for a moment and replied, 'First, did your research also show that my mother is dying after a long illness, and has medical bills that are several times her annual income?'Embarrassed, the United Way rep mumbled, 'Um ... no.'The lawyer interrupts, 'or that my brother, a disabled veteran, is blind and confined to a wheelchair?'The stricken United Way rep began to stammer out an apology, but was interrupted again.'or that my sister's husband died in a traffic accident,' the lawyer's voice rising in indignation, 'leaving her penniless with three children?!'The humiliated United Way rep, completely beaten, said simply, 'I had no idea...'On a roll, the lawyer cut him off once again, 'So if I don't give any money to them, why should I give any to you?'"
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