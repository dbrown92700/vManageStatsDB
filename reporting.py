#!python3

import os, json, datetime
from settings import *

files = os.listdir(file_directory)
stat_files = []
for item in files:
	if 'statsdb' in item:
		stat_files.append(item)
stat_files.sort()
for target_file in stat_files:
	with open(f'{file_directory}/{target_file}', 'r') as file:
		jdata = json.loads(file.read())
	time = datetime.datetime.fromtimestamp(jdata['timestamp'])
	count = 0
	for edge in jdata['activeEdges']:
		if edge_name in edge:
			count += 1
	one_day = float(jdata['dbEstimate'][0]['Total disk space']['1 day   '].split(' ')[0])
	print(f"{time.month:02}/{time.day:02}/{time.year} {time.hour:02}:{time.minute:02} " \
	f"{one_day:8.2f} MB Estimate for " \
	f"{count:3d} Stores Online --> " \
	f"{one_day/count*target_count/1000:6.2f} GB for {target_count} Stores")

