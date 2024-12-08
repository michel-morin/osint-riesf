#!/usr/bin/env python

# Looking for people across Répertoire des Ingénieurs et des Scientifiques (IESF)

# Parameters to fill below before launch:
# search: string
## in case of compound first name or last name, use the following character: -

## Please use the bash command grep with the following parameters in your result output:
# firstname lastname

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,fr;q=0.8,fr-FR;q=0.5,en;q=0.3',
    'Referer': 'https://repertoire.iesf.fr/',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://repertoire.iesf.fr',
    'DNT': '1',
    'Connection': 'keep-alive',
}

json_data = {
    'view': 1,
    'layout': 1,
    'sort': 46,
    'dir': 1,
    'page': 1,
    'limit': 100,
    'search': 'john doe', # # not case sensitive
}

response = requests.put('https://repertoire.iesf.fr/n/node/5/items', cookies=cookies, headers=headers, json=json_data)
json = response.json()
print(json['rows'])
