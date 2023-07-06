def test_operations_show_last_operation(operations_instance, capsys):
    operations_instance.show_last_operation()
    captured = capsys.readouterr()
    assert 'ОПЕРАЦИЯ: 2' in captured.out
    assert '01.01.2022 Operation 6' in captured.out
    assert 'ОПЕРАЦИЯ: 3' not in captured.out
