class OperationsManager:
    def __init__(self, all_operations):
        self.all_operations = all_operations
        self.last_five_operations = self.sorted_last_five_operations()

    def filtering_completed_operations(self):
        filtered_operations = []

        for operation in self.all_operations:
            if operation.get("state") == "EXECUTED":
                filtered_operations.append(operation)
        return filtered_operations

    def sorted_last_five_operations(self):
        return sorted(self.filtering_completed_operations(), key=lambda item: item['date'], reverse=True)[:5]

    @staticmethod
    def reformat_date(date):
        return '.'.join(date.split('T')[0].split('-')[::-1])

    @staticmethod
    def hide_order(order):
        if len(order) == 16:
            return order[:4] + ' ' + order[4:6] + '**' + ' **** ' + order[12:16]
        return '**' + order[len(order) - 4:]

    def check_from_operation(self, operation):
        order_to = operation['to'].split()
        order_to[-1] = self.hide_order(order_to[-1])
        if operation.get('from'):
            order_from = operation['from'].split()
            order_from[-1] = self.hide_order(order_from[-1])
            return ' '.join(order_from) + ' -> ' + ' '.join(order_to)
        return ' '.join(order_to)

    def show_last_operation(self):
        for operation in self.last_five_operations:
            print(f'ОПЕРАЦИЯ: {operation["id"]}')
            print(f'{self.reformat_date(operation["date"])} {operation["description"]}')
            print(f'{self.check_from_operation(operation)}')
            print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
