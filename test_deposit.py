import pytest
from deposit import Deposit, BudgetException


@pytest.fixture
def deposit():
    return Deposit()


def test_deposit_initial_budget(deposit):
    assert deposit.budget == 0


def test_deposit_valid_deposit(deposit):
    deposit.deposit(50)
    assert deposit.budget == 50


def test_deposit_invalid_deposit_zero_amount(deposit):
    with pytest.raises(BudgetException) as exception_info:
        deposit.deposit(0)
    assert str(exception_info.value) == "Invalid deposit amount. " \
                                        "Amount must be greater than zero."


def test_deposit_invalid_deposit_negative_amount(deposit):
    with pytest.raises(BudgetException) as exception_info:
        deposit.deposit(-50)
    assert str(exception_info.value) == "Invalid deposit amount." \
                                        " Amount must be greater than zero."


def test_deposit_valid_withdrawal(deposit):
    deposit.deposit(100)
    deposit.withdraw(50)
    assert deposit.budget == 50


def test_deposit_invalid_withdrawal_zero_amount(deposit):
    with pytest.raises(BudgetException) as exception_info:
        deposit.withdraw(0)
    assert str(exception_info.value) == "Invalid withdrawal amount." \
                                        " Amount must be greater than zero."


def test_deposit_invalid_withdrawal_negative_amount(deposit):
    with pytest.raises(BudgetException) as exception_info:
        deposit.withdraw(-50)
    assert str(exception_info.value) == "Invalid withdrawal amount." \
                                        " Amount must be greater than zero."


def test_deposit_invalid_withdrawal_insufficient_funds(deposit):
    deposit.deposit(50)
    with pytest.raises(BudgetException) as exception_info:
        deposit.withdraw(100)
    assert str(exception_info.value) == "Insufficient funds. Cannot" \
                                        " withdraw more than available budget."
