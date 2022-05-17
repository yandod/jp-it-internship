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
skip = 0 #475

google = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
for company in companies['data']:
    print("processing " + str(i) + " of " + str(total))
    if i < skip:
        i += 1
        continue
    pprint(company['name'])
    sleep(1)
    response = google.cse().list(
        q=company['name'] + ' インターンシップ',
        cx=CUSTOM_SEARCH_ENGINE_ID,
        lr='lang:ja',
        num=3
    ).execute()
    if 'items' in response:
        try:
            companies['data'][i]['internship_1'] = response['items'][0]['link']
        except IndexError:
            companies['data'][i]['internship_1'] = ''
        try:
            companies['data'][i]['internship_2'] = response['items'][1]['link']
        except IndexError:
            companies['data'][i]['internship_2'] = ''
        try:
            companies['data'][i]['internship_3'] = response['items'][2]['link']
        except IndexError:
            companies['data'][i]['internship_3'] = ''
    
    if i % 10 == 0:
        with open(json_file, 'w') as f:
            json.dump(companies, f, indent=4, ensure_ascii=False)
    i += 1

with open(json_file, 'w') as f:
    json.dump(companies, f, indent=4, ensure_ascii=False)
