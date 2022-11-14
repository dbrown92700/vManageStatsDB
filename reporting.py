#!python3

import os, json, datetime

# Start date:
start_month, start_day, start_year = 10, 17, 2022
target_count = 750
scale = {'MB': 1, 'GB': 1000, 'TB': 1000000, 'KB': .001}

files = os.listdir()
stat_files = []
for item in files:
    if 'statsdb' in item:
        stat_files.append(item)
stat_files.sort()
output_file = open('EstimateReport.txt', 'w')
for target_file in stat_files:
    with open(target_file, 'r') as file:
        jdata = json.loads(file.read())
    time = datetime.datetime.fromtimestamp(jdata['timestamp'])
    output = f"{time.month:02}/{time.day:02}/{time.year} {time.hour:02}:{time.minute:02} "
    print(output)
    output_file.write(output + '\n')
    count = 0
    for edge in jdata['activeEdges']:
        if 'sdw1' in edge:
            count += 1
    one_day_estimate = jdata['dbEstimate'][0]['Total disk space']['1 day   '].split(' ')
    one_day = float(one_day_estimate[0]) * scale[one_day_estimate[1]]

    total_days = (time - datetime.datetime(start_year, start_month, start_day)).days
    total_est_scaled = 0
    for x in jdata['dbEstimate'][1]['Per index disk space ']:
        if x['status'] == 'success':
            days = int(x['dataSetInfo']['Total Days of records'])
            size_text = x['dataSetInfo']['Average Size per day '].split(' ')
            # print(f'{x["index"]}: {days} - {size_text}')
            size = float(size_text[0]) * scale[size_text[1]]
            estimate = days / total_days * size
            output = f'      {x["index"]}: {days} Days with {size} MB -scaled-> {estimate} MB for {total_days} days'
            print(output)
            output_file.write(output + '\n')
            total_est_scaled += estimate

    output = f"{one_day:8.2f} MB Estimate for " \
             f"{count:3d} Stores Online --> " \
             f"{one_day / count * target_count / 1000:6.2f} GB non-scaled ---> " \
             f"{total_est_scaled / count * target_count / 1000:6.2f} GB scaled for {total_days} days " \
             f"for {target_count} Stores"
    print(output + '\n')
    output_file.write(output + '\n\n')
output_file.close()
