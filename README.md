# vManageStatsDB
Used for tracking the estimated database disk space needed for vManage.

These two scripts will pull the database statistics info from vManage and calculate changes over time.  The main.py script pulls a list of currently deployed edge devices, the database size report, and the database size needed estimation report and stores these in a single JSON object with a timestamp in a file.

The reporting.py file parses all the files to show changes over time in the estimated GB/day requirements.

These were built to calculate the long term target database size as branches were deployed, so the reporting calculation has two settings, target_count and edge_name.  Target_count is the total number of branches expected, and edge_name is a filter string to count only the branch edges.

## Use
Edit settings.py for your environment.

To grab statistics
> python3 main.py

To run calculations
> python3 reporting.py

To trend, run main.py on a daily basis.
