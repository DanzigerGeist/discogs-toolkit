# Discogs Toolkit

A collection of scripts to help with Discogs data. These are mostly for my own use, but feel free to use them if you find them useful.

---

## Setup

### Requirements
* Python 3.6+

### Installation
* Clone the repository
* Install the requirements

```bash
pip3 install -r requirements.txt
```


### Authentication
Scripts that are using the Discogs API require an [API token](https://www.discogs.com/settings/developers) to be set. Look for "*discogs_token*" field on the top of the script.

```python
discogs_token = "YOUR_API_TOKEN_HERE"
```

---
## Scripts

### sort_my_collection.py

Prints your collection items list sorted first alphabetically by artist, then by release year. Originally used to sort the CDs on the shelf in my living room.