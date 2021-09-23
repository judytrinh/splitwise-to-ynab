#!/usr/bin/env python3

import csv
from datetime import datetime, timedelta
from decimal import Decimal
from pprint import pprint
import requests
import sys

YNAB_BASE_URL = "https://api.youneedabudget.com/v1"
BUDGET_ID = 'last-used'

if len(sys.argv) < 3:
  print("ERROR: Not all required arguments were provided")
  sys.exit(1)

csv_file = sys.argv[1]
access_token = sys.argv[2]
account_id = sys.argv[3]
date_start = datetime.strptime(sys.argv[4],"%Y-%m-%d").date()
date_end = datetime.today().date()

if len(sys.argv) > 5:
  date_end = datetime.strptime(sys.argv[5], "%Y-%m-%d").date()

print(f"Importing Splitwise transactions starting from {date_start} to {date_end} inclusive from {csv_file}")

data = { 
  "transactions": []
}

with open(csv_file, newline='') as csvfile:
  reader = csv.reader(csvfile)
  for _ in range(4): next(reader)

  for row in reader:
    if len(row) == 0:
      break

    txn_date = datetime.strptime(row[0], "%Y-%m-%d").date()

    later_than_start = txn_date >= date_start
    earlier_than_end = txn_date <= date_end

    if later_than_start and earlier_than_end:
      description = row[1]
      amount = row[5]

      data["transactions"].append({
        "account_id": account_id,
        "date": str(txn_date),
        "amount": int(Decimal(amount) * 1000),
        "payee_id": None,
        "payee_name": "Eric Lee",
        "category_id": None,
        "memo": description,
        "cleared": "cleared",
        "approved": False
      })

headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_token}'
}
response = requests.post(f'{YNAB_BASE_URL}/budgets/{BUDGET_ID}/transactions', headers=headers, json=data)
pprint(response.json())
