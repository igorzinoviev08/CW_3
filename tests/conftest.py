import pytest
from app.models.operations_manager import OperationsManager


@pytest.fixture
def operations_instance():
    all_operations = [
        {
            'id': 1,
            'date': '2017-01-01T12:00:00',
            'description': 'Operation 2',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'

        },
        {
            'id': 2,
            'date': '2018-01-01T12:00:00',
            'description': 'Operation 2',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {
            'id': 3,
            'date': '2015-01-01T12:00:00',
            'description': 'Operation 3',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {
            'id': 4,
            'date': '2020-01-01T12:00:00',
            'description': 'Operation 4',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {},
        {
            'id': 5,
            'date': '2021-01-01T12:00:00',
            'description': 'Operation 5',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'RUB'}},
            'state': 'EXECUTED'
        },
        {
            'id': 6,
            'date': '2022-01-01T12:00:00',
            'description': 'Operation 6',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        }

    ]
    return OperationsManager(all_operations)
