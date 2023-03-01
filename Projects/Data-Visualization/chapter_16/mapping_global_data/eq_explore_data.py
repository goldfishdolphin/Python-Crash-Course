import json

filename = 'Projects/Data-Visualization/chapter_16/mapping_global_data/data/eq_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'Projects/Data-Visualization/chapter_16/mapping_global_data/data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
