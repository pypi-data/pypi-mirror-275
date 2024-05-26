Metadata Extractor API
============

Metadata Extractor is a simple tool for extracting metadata from web pages. It returns the meta title, meta description, and more.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Metadata Extractor API](https://apiverve.com/marketplace/api/metadataextractor)

---

## Installation
	pip install apiverve-metadataextractor

---

## Configuration

Before using the metadataextractor API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Metadata Extractor API documentation is found here: [https://docs.apiverve.com/api/metadataextractor](https://docs.apiverve.com/api/metadataextractor).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_metadataextractor.apiClient import MetadataextractorAPIClient

# Initialize the client with your APIVerve API key
api = MetadataextractorAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = {  "url": "https://myspace.com" }
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
    "url": "https://myspace.com/",
    "canonical": "https://myspace.com/discover/featured",
    "title": "Featured Content on Myspace",
    "image": "",
    "author": "",
    "description": "Featured Content on Myspace",
    "keywords": "Myspace, social entertainment, artist tools, social media, social discovery, creative community, empowering expression, stream music, music videos, music, share music, playlists, mixes, profiles, discovery, discover",
    "source": "",
    "price": "",
    "priceCurrency": "",
    "availability": "",
    "robots": "",
    "jsonld": {},
    "og:url": "https://myspace.com/discover/featured",
    "og:locale": "",
    "og:locale:alternate": "",
    "og:title": "Featured Content on Myspace",
    "og:type": "article",
    "og:description": "Featured Content on Myspace",
    "og:determiner": "",
    "og:site_name": "Myspace",
    "og:image": "",
    "og:image:secure_url": "",
    "og:image:type": "",
    "og:image:width": "",
    "og:image:height": "",
    "twitter:title": "",
    "twitter:description": "",
    "twitter:image": "",
    "twitter:image:alt": "",
    "twitter:card": "",
    "twitter:site": "",
    "twitter:site:id": "",
    "twitter:url": "",
    "twitter:account_id": "",
    "twitter:creator": "",
    "twitter:creator:id": "",
    "twitter:player": "",
    "twitter:player:width": "",
    "twitter:player:height": "",
    "twitter:player:stream": "",
    "twitter:app:name:iphone": "",
    "twitter:app:id:iphone": "",
    "twitter:app:url:iphone": "",
    "twitter:app:name:ipad": "",
    "twitter:app:id:ipad": "",
    "twitter:app:url:ipad": "",
    "twitter:app:name:googleplay": "",
    "twitter:app:id:googleplay": "",
    "twitter:app:url:googleplay": "",
    "responseBody": "",
    "article:published_time": "",
    "article:modified_time": "",
    "article:expiration_time": "",
    "article:author": "",
    "article:section": "",
    "article:tag": "",
    "og:article:published_time": "",
    "og:article:modified_time": "",
    "og:article:expiration_time": "",
    "og:article:author": "",
    "og:article:section": "",
    "og:article:tag": "",
    "fb:app_id": "373499472709067",
    "msapplication-TileColor": "#313131",
    "msapplication-TileImage": "https://x.myspacecdn.com/new/common/images/favicons/tile.png",
    "p:domain_verify": "9069a95798cb530a18cfa50cec2757d1"
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