import requests
from dotenv import load_dotenv
import os
import datetime
import json

load_dotenv()

APITUBE_KEY = os.getenv('APITUBE_KEY')

endpoint = 'https://api.apitube.io/v1/news/everything'

headers = {'Authorization': f'Bearer {APITUBE_KEY}'}

company = 'Tesla'
time_range = '1D'

# 'q': f'(title):{company}'
payload = {
    'title': f'{company}',
    'language': 'en',
    'published_at.start': f'NOW-{time_range}',
    'published_at.end': 'NOW'
}

response = requests.get(url=endpoint, params=payload, headers=headers) #, verify=False)
response.raise_for_status()
response_json = response.json()

current_timestamp = datetime.datetime.now()
current_timestamp_formatted = current_timestamp.strftime("%Y%m%d_%H%M%S")

localfile_path = os.path.join('.', 'test_requests', 'apitube', f'{company}_{current_timestamp_formatted}.json')

with open(localfile_path, mode='wb') as localfile:
    localfile.write(response.content)

with open(localfile_path, mode='rb') as localfile:
    print(json.load(localfile))


