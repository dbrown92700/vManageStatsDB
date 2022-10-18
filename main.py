#!/usr/bin/python3
"""
Copyright (c) 2012 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
__author__ = "David Brown <davibrow@cisco.com>"
__contributors__ = []
__copyright__ = "Copyright (c) 2012 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

from vmanage_api import rest_api_lib
from includes import *
from datetime import datetime
import json

if __name__ == '__main__':
    vmanage = rest_api_lib(vmanage_ip, vmanage_user, vmanage_password)
    estimate = vmanage.get_request('/management/elasticsearch/index/size/estimate')
    elasticsearch = vmanage.get_request('/management/elasticsearch/index/size')
    edges = vmanage.get_request('/device')
    vmanage.logout()
    Now = datetime.now()
    edge_list = []
    for device in edges['data']:
        if device['reachability'] == 'reachable' and device['personality'] == 'vedge':
            edge_list.append(device['host-name'])
    data = {
        'timestamp': Now,
        'activeEdges': edge_list,
        'dbSize': elasticsearch,
        'dbEstimate': estimate
    }
    filename = f'statsdb_{Now.year}-{Now.month:02}-{Now.day:02}_{Now.hour:02}-{Now.minute:02}.txt'
    with open(file_directory+filename, 'w') as file:
        file.write(json.dumps(data, indent=2))

# [END gae_python3_app]
