help = """
This sciprt takes 4 cli arguments:
1. The path to the SharedCache. On windows it generaly C:/EVE/SharedCache/ or
%AppData%/Local/CCP/EVE/SharedCache. If you did not downloaded the entier game
(via the launcher) you will miss some icons.
2. The marketGroups.yaml file for SDE (https://developers.eveonline.com/).
3. The iconIDs.yaml file for SDE.
4. The output directory. If not already created the script will create it.
"""

import yaml
import csv
import os
import sys
import shutil


if len(sys.argv) != 5:
    print(help)
    sys.exit(1)

shared_cache_path = sys.argv[1]
market_groups_path = sys.argv[2]
icon_data_path = sys.argv[3]
output_path = sys.argv[4]

if not os.path.isdir(shared_cache_path):
    print(f"{shared_cache_path} is not a valid directory path")
    sys.exit(1)
if not os.path.isfile(market_groups_path):
    print(f"{shared_cache_path} is not a valid file path")
    sys.exit(1)
if not os.path.isfile(icon_data_path):
    print(f"{shared_cache_path} is not a valid file path")
    sys.exit(1)

if not os.path.isdir(output_path):
    os.makedirs(output_path)

index_tq_path = os.path.join(shared_cache_path, "index_tranquility.txt")
res_files_path = os.path.join(shared_cache_path, "ResFiles")
if not os.path.isfile(index_tq_path) or not os.path.isdir(res_files_path):
    print("cant find SharedCache content")
    sys.exit(1)

market_groups_files = open(market_groups_path, 'r')
market_groups = yaml.safe_load(market_groups_files)
market_groups_files.close()
icon_id = [group.get("iconID") or 0 for group in market_groups.values()]

icon_data_file = open(icon_data_path, 'r')
icon_data = yaml.safe_load(icon_data_file)
icon_data_file.close()
icon_path_to_id = {}
for id in icon_id:
    icon_path_to_id[icon_data[id]["iconFile"].lower()] = id

index_tq_file = open(index_tq_path, 'r', newline='')
index_tq_reader = csv.reader(index_tq_file, delimiter=',')
for row in index_tq_reader:
    if row[0] == "app:/EVE.app/Contents/Resources/build/resfileindex.txt":
        index_path = os.path.join(res_files_path, row[1])
        break
else:
    print("cant find resfileindex.txt in index_tranquility.txt")
    sys.exit(1)
index_tq_file.close()

index_file = open(index_path, 'r', newline='')
index_reader = csv.reader(index_file, delimiter=',')
for row in index_reader:
    if row[0].lower() in icon_path_to_id:
        res_file = os.path.join(res_files_path, row[1])
        output = os.path.join(output_path, str(icon_path_to_id[row[0]]) + ".png")
        shutil.copyfile(res_file, output)
