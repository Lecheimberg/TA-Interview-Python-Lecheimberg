from bank_account import BankAccount

def test_create_account():
    acc = BankAccount("Lucas", "001", 1000.0)
    assert acc.get_account_holder_name() == "Lucas"
    assert acc.get_account_number() == "001"
    assert acc.get_balance() == 1000.0

def test_perform_transfer():
    acc1 = BankAccount("john", "002", 200.0)
    acc2 = BankAccount("Emily", "003", 100.0)

    result = acc1.withdraw(100.0)
    acc2.deposit(100.0)

    assert result is True
    assert acc1.get_balance() == 100.0
    assert acc2.get_balance() == 200.0

def test_transfer_insufficient_balance():
    acc1 = BankAccount("Ann", "004", 100.0)
    acc2 = BankAccount("Andrew", "005", 500.0)

    result = acc1.withdraw(150.0)

    assert result is False
    assert acc1.get_balance() == 100.0
    assert acc2.get_balance() == 500.0
