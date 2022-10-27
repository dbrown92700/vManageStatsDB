# vManage server(s) and credentials
vmanage_ip = 'vmanage.sdwan.cisco.com:8443'
vmanage_user = 'davibrow'
vmanage_password = 'password'

# Choose a directory to store the results files in
file_directory = './results'

# Estimations are done on the total target number of edges in the fabric.
# Total current edges deployed can be filtered using the edge_name string.
# Leave empty to count all active edges
target_count = 750
edge_name = 'sdw1'