#!/usr/local/bin/python3

from pprint import pprint
import json
from googlesearch import search

json_file = './data/output.json'

with open(json_file) as f:
    companies = json.load(f)

total = len(companies['data'])
print('num of companies:' + str(total))

i = 0;
skip = 475
for company in companies['data']:
    i += 1
    print("processing " + str(i) + " of " + str(total))
    if i < skip:
        continue
    for result in search(company['name']):
        pprint(result)
        companies['data'][i]['url'] = result
        break
    if i % 25:
        with open(json_file, 'w') as f:
            json.dump(companies, f, indent=4, ensure_ascii=False)

with open(json_file, 'w') as f:
    json.dump(companies, f, indent=4, ensure_ascii=False)
