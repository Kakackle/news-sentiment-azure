import json
import os

test_file = r'.\test_requests\apitube\Tesla_20250217_154219.json'

bodies_list = []

## TODO: add sentiment analysis for each found body
with open(test_file, mode='rb') as localfile:
    test_data = json.load(localfile)
    results = test_data.get('results', [])
    for result in results:
        bodies_list.append(result.get('body', ''))

print(len(bodies_list))
print(bodies_list[0])