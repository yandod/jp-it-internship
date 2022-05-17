#!/usr/local/bin/python3

from pprint import pprint
import csv
import json

json_file = './data/output.json'
csv_file = './data/output.csv'

with open(json_file) as f:
    companies = json.load(f)

with open(csv_file, 'w') as f:
    writer = csv.writer(f)

    writer.writerow([
        'name',
        'prefecture',
        'size',
        'code',
        'url',
        'internship_1',
        'internship_2',
        'internship_3',
    ])

    for company in companies['data']:
        if 'url' not in company:
            company['url'] = ''
        if 'internship_1' not in company:
            company['internship_1'] = ''
        if 'internship_2' not in company:
            company['internship_2'] = ''
        if 'internship_3' not in company:
            company['internship_3'] = ''
        
        writer.writerow([
            company['name'],
            company['prefecture'],
            company['size'],
            company['code'],
            company['url'],
            company['internship_1'],
            company['internship_2'],
            company['internship_3'],
        ])
            # "name": "株式会社IIJグローバルソリューションズ",
            # "prefecture": "東京都",
            # "size": "301～500人",
            # "code": "",
            # "url": "https://www.iijglobal.co.jp/"

