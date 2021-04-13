#!/usr/bin/env python3

import sys
import datetime

print(sys.argv)

if len(sys.argv) < 3:
  print("ERROR: Not all required arguments were provided")
  sys.exit(1)

csv = sys.argv[1]
date_start = datetime.datetime.strptime(sys.argv[2],"%Y-%m-%d").date()
date_end = datetime.datetime.today().date()
if len(sys.argv) >= 4:
  date_end = datetime.datetime.strptime(sys.argv[3], "%Y-%m-%d").date()

print(f'Importing Splitwise transactions starting from {date_start} to {date_end} inclusive from {csv}')

# take in args of
# - splitwise exported csv
# date range

# harcode access token
# choose account in ynab?
# iterate through csv lines
# create transaction only if Judy owes eric

