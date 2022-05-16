#!/usr/local/bin/python3

from pprint import pprint
import json
from googleapiclient.discovery import build
import os
from time import sleep

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
CUSTOM_SEARCH_ENGINE_ID = os.environ['GOOGLE_SEARCH_ENGINE']

json_file = './data/output.json'

with open(json_file) as f:
    companies = json.load(f)

total = len(companies['data'])
print('num of companies:' + str(total))

i = 0
skip = 475 #475

google = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
for company in companies['data']:
    print("processing " + str(i) + " of " + str(total))
    if i < skip:
        i += 1
        continue
    pprint(company['name'])
    sleep(1)
    response = google.cse().list(
        q=company['name'],
        cx=CUSTOM_SEARCH_ENGINE_ID,
        lr='lang:ja',
        num=3
    ).execute()
    url = response['items'][0]['link']
    companies['data'][i]['url'] = url
    if i % 10 == 0:
        with open(json_file, 'w') as f:
            json.dump(companies, f, indent=4, ensure_ascii=False)
    i += 1

with open(json_file, 'w') as f:
    json.dump(companies, f, indent=4, ensure_ascii=False)
