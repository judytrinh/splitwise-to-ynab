#!/usr/bin/env python3

import csv
from datetime import datetime, timedelta
import sys

print(sys.argv)

if len(sys.argv) < 3:
  print("ERROR: Not all required arguments were provided")
  sys.exit(1)

csv_file = sys.argv[1]
date_start = datetime.strptime(sys.argv[2],"%Y-%m-%d").date()
date_end = datetime.today().date()
if len(sys.argv) >= 4:
  date_end = datetime.strptime(sys.argv[3], "%Y-%m-%d").date()

print(f"Importing Splitwise transactions starting from {date_start} to {date_end} inclusive from {csv_file}")

with open(csv_file, newline='') as csvfile:
  reader = csv.reader(csvfile)
  for _ in range(4): next(reader)

  for row in reader:
    if len(row) == 0:
      exit()

    txn_date = datetime.strptime(row[0], "%Y-%m-%d").date()

    later_than_start = txn_date >= date_start
    earlier_than_end = txn_date <= date_end

    if later_than_start and earlier_than_end:
      description = row[4]
      amount = row[5]
      print(', '.join(row))
      print(f'{row[0]}: {row[5]} {later_than_start} {earlier_than_end}')

# for each date, if >= date_start and <= date_end, create the txn

# harcode access token
# choose account in ynab?
# iterate through csv lines
# create transaction only if Judy owes eric

