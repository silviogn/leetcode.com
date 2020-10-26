import unittest

class Solution:
    # https://leetcode.com/problems/invalid-transactions/submissions/

    def invalidTransactions(self, transactions):
        output_transactions = {}

        if len(transactions) == 0:
            return []

        group_transactions = {}

        for transaction_id in range(0, len(transactions)):
            name, time, amount, city = transactions[transaction_id].split(',')

            if int(amount) > 1000:
                self.insert_output_transaction(transaction_id, output_transactions, transactions[transaction_id])

            if name not in group_transactions.keys():
                group_transactions[name] = [{'id': transaction_id, 'transaction': transactions[transaction_id]}]
            else:
                for trans_dict in group_transactions[name]:
                    local_id = trans_dict.get("id")

                    local_transaction = trans_dict.get("transaction")

                    local_name, local_time, local_amount, local_city = local_transaction.split(',')

                    if name == local_name and city != local_city and abs(int(time) - int(local_time)) <= 60:
                        self.insert_output_transaction(transaction_id, output_transactions, transactions[transaction_id])
                        self.insert_output_transaction(local_id, output_transactions, local_transaction)

                group_transactions[name].append({'id': transaction_id, 'transaction': transactions[transaction_id]})

        return [trans for trans in output_transactions.values()]


    def insert_output_transaction(self, transaction_id, output_transactions, transaction):
        if transaction_id not in output_transactions.keys():
            output_transactions[transaction_id] = transaction


class TestSolution(unittest.TestCase):
    def test_return(self):
        self.assertEqual(Solution().invalidTransactions(["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona", "bob,820,596,bangkok",
         "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"]),['bob,689,1910,barcelona', 'bob,832,1726,barcelona', 'bob,820,596,bangkok'])



if __name__ == '__main__':
        unittest()
