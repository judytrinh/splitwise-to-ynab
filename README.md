# splitwise-to-ynab
My personal importer of Splitwise transactions to YNAB.

This has only been tested using a personal access token and is recommended to only be used for that purpose.

It also only supports the use case of sharing a Splitwise with just 1 other person.

# Quick Start

## Prerequisites

- Clone the repo.
- Ensure your python3 version is high enough (I'm on 3.8.2).
- Change the hardcoded name of your Splitwise roomie in the script to your desired payee.
- [Obtain your YNAB personal access token](https://api.youneedabudget.com/#personal-access-tokens) if you haven't before. Save it somewhere safe such as a secure password manager.
-  If you are importing transactions to a budget account that is *not* the last used one, obtain the id of your desired budget account if you haven't before. You can reference the [Quick Start](https://api.youneedabudget.com/) for how to list your budget accounts and their ids.

## Usage
You can export your list of transactions in a CSV from Splitwise.

In the root directory of the repo, replace the inputs appropriately and run the following:
```
python3 import.py splitwise-exported-txns.csv yourVeryLongYnabPersonalAccessToken yourBudgetAccountId DateStart DateEnd
```

## Notes
- **yourBudgetAccountId** can either be the literal id or "last-used".

- Date format is YYYY-MM-DD.

- **DateEnd** is optional. It will import all transactions starting from the DateStart inclusive until the very end if it is included.

- All dates are inclusive.


# Future Goals
- Implement a simple local web UI to easily select a date range, save access token to local storage
- See if it's easy to hit Splitwise via API to eliminate the CSV downloading step