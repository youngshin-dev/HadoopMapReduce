# !/usr/bin/python

# A mapper for Hadoop job to get the total hits for each sites.
# The data "access_log" can be obtained from Udacity.


import sys

for line in sys.stdin:
    data = line.strip().split('"')
    if len(data) == 3:
        first, request, remaing = data
        file = request.strip().split(" ")
        site = file[1]
        if "http://www.the-associates.co.uk" in site:
            site = site.replace("http://www.the-associates.co.uk", '')

        print site