from bank_application import BankApplication

def test_balance_display():
    app = BankApplication()
    app.create_account("john", "001", 200.0)
    app.create_account("Emily", "002", 100.0)

    before_sender = app.get_account_balance("001")
    before_receiver = app.get_account_balance("002")

    result = app.perform_transfer("001", "002", 100.0)
    
    after_sender = app.get_account_balance("001")
    after_receiver = app.get_account_balance("002")

    assert result is True
    assert before_sender == 200.0
    assert before_receiver == 100.0
    assert after_sender == 100.0
    assert after_receiver == 200.0
