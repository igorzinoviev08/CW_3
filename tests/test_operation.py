from app.models.operations_manager import OperationsManager


def test_operations_show_last_operation(operations_instance, capsys):
    operations_instance.show_last_operation()
    captured = capsys.readouterr()
    assert 'ОПЕРАЦИЯ: 2' in captured.out
    assert '01.01.2022 Operation 6' in captured.out
    assert 'ОПЕРАЦИЯ: 3' not in captured.out


def test_check_from_operation(operations_instance):
    operation = {
        'id': 1,
        'date': '2017-01-01T12:00:00',
        'description': 'Operation 2',
        'from': 'Account A',
        'to': 'Account B',
        'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
        'state': 'EXECUTED'
    }
    result = operations_instance.check_from_operation(operation)
    assert result == 'Account **A -> Account **B'


def test_hide_order():
    order1 = '1234567890123456'
    result1 = OperationsManager.hide_order(order1)
    assert result1 == '1234 56** **** 3456'

    order2 = '12345678'
    result2 = OperationsManager.hide_order(order2)
    assert result2 == '**5678'


def test_reformat_date():
    date1 = '2021-07-10T12:00:00'
    result1 = OperationsManager.reformat_date(date1)
    assert result1 == '10.07.2021'

    date2 = '2022-12-31T23:59:59'
    result2 = OperationsManager.reformat_date(date2)
    assert result2 == '31.12.2022'
