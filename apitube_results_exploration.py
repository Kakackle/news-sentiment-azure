"""
Notebook user for exploring apitube results in an interactive matter
"""
# %%
import json

# test_file_path = r'.\test_requests\apitube\Tesla_20250220_144736.json'
test_file_path = r'.\test_requests\apitube\Google_20250220_145556.json'
test_file = open(test_file_path, mode='rb')
test_data = json.load(test_file)
results = test_data.get('results')

# %%
domain_set = set()
domain_list = []
for r in results:
    domain = r.get('source').get('domain')
    domain_list.append(domain)
    domain_set.add(domain)

print(f'list len: {len(domain_list)}, set len: {len(domain_set)}')
print(f'set:\n {domain_set}')

# %%
test_file.close()
# %%
