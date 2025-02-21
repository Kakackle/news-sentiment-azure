import requests
from dotenv import load_dotenv
import os
import datetime
import json

load_dotenv()

APITUBE_KEY = os.getenv('APITUBE_KEY')

endpoint_type = 'everything' # or 'top-headlines'
endpoint = f'https://api.apitube.io/v1/news/{endpoint_type}'

headers = {'Authorization': f'Bearer {APITUBE_KEY}'}

company = 'Google'
time_range = '1D' # NOW - time_range, as in articles between now and now - 1 day (D)
sort_order = 'published_at' # 'source.rank.opr' for open page rank - not that reliable when lacking articles in range
per_page = 20 # in case we want to limit the result number, may be necessary for more
# specific queries to keep the quality high

# 'q': f'(title):{company}'
payload = {
    'title': f'{company}',
    # 'language': 'en OR fr OR es',
    'language': 'en',
    
    # 'category': 'politics,science,technlogy,environment,business', # limit categories for relatedness
    #category.name???

    # 'source.country.code': 'us,gb,au,ie,ca', # ensure english language by limiting to english speaking countries
    # 'source.country.code': 'us',

    # ideal version
    # 'published_at.start': f'NOW-{time_range}',
    # 'published_at.end': 'NOW',

    # since there is a delay in the free tier of the apitube news API
    'published_at.start': f'NOW-2D',
    'published_at.end': f'NOW-1D',

    # 'source.rank.opr.max': '0.9'
    'is_duplicate': 'false', # filter out duplicate articles
    'sort_by': f'{sort_order}',
    'sort_order': 'desc',

    'source.rank': '0.5' # vague "source quality", higher is better
    # 'sentiment.overall.polarity': 'positive' # for testing purposes
}

payload_lucene = {'q:':'(title:Google AND (language.name:English OR language.name:French))'}

response = requests.get(url=endpoint, params=payload_lucene, headers=headers) #, verify=False)
response.raise_for_status()
response_json = response.json()

current_timestamp = datetime.datetime.now()
current_timestamp_formatted = current_timestamp.strftime("%Y%m%d_%H%M%S")

localfile_path = os.path.join('.', 'test_requests', 'apitube', f'{company}_{current_timestamp_formatted}.json')

with open(localfile_path, mode='wb') as localfile:
    localfile.write(response.content)

with open(localfile_path, mode='rb') as localfile:
    print(json.load(localfile))


