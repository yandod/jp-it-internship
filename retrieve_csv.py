#!/usr/local/bin/python3

from pprint import pprint
import urllib.request
import zipfile
from os import listdir
from os.path import isfile, join
import csv
import json

url = 'https://positive-ryouritsu.mhlw.go.jp/positivedb/opendata/download_b.html?w=18'
temp_zip = './data/mhlw_csv.zip'
temp_csv_dir  = './data/mhlw_csv/'
json_file = './data/output.json'
urllib.request.urlretrieve(url, temp_zip)

with zipfile.ZipFile(temp_zip, "r") as zip_ref:
    zip_ref.extractall(temp_csv_dir)

csv_files =  [f for f in listdir(temp_csv_dir) if isfile(join(temp_csv_dir, f))]

pprint(csv_files)

json_data = dict()
json_data['data'] = list()

with open(temp_csv_dir + csv_files[0]) as f:
    reader = csv.reader(f)
    idx = 0;
    for row in reader:
        company = {
            'name': row[0],
            'prefecture': row[4],
            'size': row[5],
            'code': row[7],
        }
        if idx > 0:
            json_data['data'].append(company)
        idx += 1

pprint(json_data)
with open(json_file, 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)
    
