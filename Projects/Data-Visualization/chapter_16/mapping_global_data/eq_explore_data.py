import json

filename = 'Projects/Data-Visualization/chapter_16/mapping_global_data/data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
