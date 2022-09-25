import json
import csv


ADS_CSV = 'ads.csv'
ADS_JSON = 'ads.json'
ADS_MODEL_NAME = 'ads.ad'
CATEGORY_CSV = 'categories.csv'
CATEGORY_JSON = 'categories.json'
CATEGORY_MODEL_NAME = 'ads.category'


def convert_csv_to_json(csv_filename, json_filename, model_name):

    with open(csv_filename, encoding='utf-8') as csv_file:
        csv_read = csv.DictReader(csv_file)
        result = []
        for row in csv_read:
            res = {"model": model_name, "pk": int(row['id'] if 'id' in row else row['Id'])}
            if 'id' in row:
                del row['id']
            elif 'Id' in row:
                del row['Id']
            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            res['fields'] = row
            result.append(res)

    with open(json_filename, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(result, indent=3, ensure_ascii=False))


convert_csv_to_json(ADS_CSV, ADS_JSON, ADS_MODEL_NAME)
convert_csv_to_json(CATEGORY_CSV, CATEGORY_JSON, CATEGORY_MODEL_NAME)
