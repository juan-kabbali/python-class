from wallet import Wallet
import pytest

OPENING_BALANCE = 20


@pytest.fixture()
def empty_wallet():
    return Wallet(0)


@pytest.fixture()
def wallet():
    return Wallet(OPENING_BALANCE)


def test_empty_wallet(empty_wallet):
    assert empty_wallet.is_empty()


def test_not_empty_wallet(wallet):
    assert not wallet.is_empty()


def test_add_founds(wallet):
    amount = 50
    wallet.add_founds(amount)
    assert wallet.balance == amount + OPENING_BALANCE


@pytest.mark.parametrize("amount", [-2, -50])
def test_add_negative_founds(wallet, amount):
    with pytest.raises(Exception) as exception_info:
        wallet.add_founds(amount)
    assert str(exception_info.value) == "amount must be a positive number"
