def test_get_positions(access_token):
    from account_data import AccountData

    acc_data = AccountData(access_token)
    res = acc_data.get_positions()
    assert "entry" in res
    assert "quantity" in res
