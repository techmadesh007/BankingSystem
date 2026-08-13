import bisect
from datetime import datetime

from sortedcontainers import SortedDict


class StatementService:
    def __init__(self):
        self.sorted_account_ids = []
        self.transactions_by_date = SortedDict()

    def add_account_id(self, account_no):
        if account_no not in self.sorted_account_ids:
            bisect.insort(self.sorted_account_ids, account_no)

    def remove_account_id(self, account_no):
        position = bisect.bisect_left(
            self.sorted_account_ids,
            account_no
        )

        if (
            position < len(self.sorted_account_ids)
            and self.sorted_account_ids[position] == account_no
        ):
            self.sorted_account_ids.pop(position)

    def find_account_position(self, account_no):
        return bisect.bisect_left(
            self.sorted_account_ids,
            account_no
        )

    def find_right_position(self, account_no):
        return bisect.bisect_right(
            self.sorted_account_ids,
            account_no
        )

    def add_transaction(self, transaction):
        timestamp = transaction.timestamp

        if timestamp not in self.transactions_by_date:
            self.transactions_by_date[timestamp] = []

        self.transactions_by_date[timestamp].append(transaction)

    def get_transactions_between(self, start_date, end_date):
        start_datetime = self._convert_to_datetime(start_date, False)
        end_datetime = self._convert_to_datetime(end_date, True)

        transactions = []

        for timestamp, transaction_list in self.transactions_by_date.irange(
            minimum=start_datetime,
            maximum=end_datetime,
            inclusive=(True, True),
        ):
            transactions.extend(transaction_list)

        return transactions

    def get_sorted_account_ids(self):
        return list(self.sorted_account_ids)

    def get_accounts_sorted_by_balance(self, accounts):
        return sorted(
            accounts,
            key=lambda account: account.balance
        )

    def _convert_to_datetime(self, value, end_of_day):
        if isinstance(value, datetime):
            return value

        date_value = datetime.strptime(value, "%Y-%m-%d")

        if end_of_day:
            return date_value.replace(
                hour=23,
                minute=59,
                second=59,
                microsecond=999999
            )

        return date_value