import os.path
from datetime import datetime
scale = {'tb': 1000, 'gb': 1, 'mb': .001, 'kb': .000001, 'b': .000000001}
edges_deployed = 25
edges_planned = 750
filename = 'elastic_curl.txt'

with open(filename) as file:
    text = file.read().split('\n')
capture_time = datetime.fromtimestamp(int(os.path.getmtime(filename)))
text_split = []
for line in text:
    while line.find('  ') > -1:
        line = line.replace('  ',' ')
    line = line.split(' ')
    if line[0] == 'green':
        line[2] = line[2].split('_')
        text_split.append(line)
for num, line in enumerate(text_split):
    if num == len(text_split) - 1:
        break
    stat1 = line[2]
    stat2 = text_split[num+1][2]
    if stat1[1].isalpha() or stat2[1].isalpha():
        continue
    if stat1[0] == stat2[0]:
        stop_time = datetime(int(stat2[1]), int(stat2[2]), int(stat2[3].split('t')[0]), int(stat2[3].split('t')[1]),
                             int(stat2[4]), int(stat2[5]))
    else:
        stop_time = capture_time
    elapsed = stop_time - datetime(int(stat1[1]), int(stat1[2]), int(stat1[3].split('t')[0]),
                                   int(stat1[3].split('t')[1]), int(stat1[4]), int(stat1[5]))
    if line[8][-2].isdigit():
        scale_factor = .000000001
    else:
        scale_factor = scale[line[8][-2::]]
    storage = float(line[8].rstrip('bkmgt')) * scale_factor
    daily_storage = storage / elapsed.total_seconds() * 24 * 3600
    print(f'{stat1[2]:2}/{stat1[3].split("t")[0]:02}/{stat1[1]}  {stat1[0]:30} {str(elapsed):30} Size: {line[8]:10} -> '
          f'{daily_storage * 1000:8.2f} MB / day '
          f'--> {edges_planned / edges_deployed * daily_storage:8.2f} GB / day for {edges_planned} Edge devices')

