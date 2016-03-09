![logo](https://github.com/LvanWissen/bolpy/blob/master/static/icon.png)
# bolpy
Use the Bol.com catalogue as a provider for ISBN-data

## Getting started
Add your own Bol.com API secret in `functions.py` or obtain one from: http://developers.bol.com/.

```
secret = YOUR_TOKEN_HERE
```
  
Then run:
```sh
$ python3 bolflask.py
```

## Output
Bootstrap webpage with a table with the following information (if available):
* ISBN-13
* Title
* Authors
* Price
* Publisher
* Year
* Print
* Print_type, e.g. hardcover or paperback
* Language

Possibility to download to `*.CSV`.

## Requirements
* Requests (http://docs.python-requests.org/en/master/)
* Flask (http://flask.pocoo.org/)
