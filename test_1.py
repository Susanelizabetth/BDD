import pathlib
from pytest_bdd import scenario, given, when, then
from pathlib import Path
import pytest

featureDir = 'myfeatures'
featureFile = 'feature_1.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureDir).joinpath(featureFile)

def pytest_configure():
    pytest.AMT = 0
    
@scenario(FEATURE_FILE, 'Deposito de dinero')
def test_withdrawal():
    print('TERMINO el test de deposito de dinero')
    pass

@given('El saldo de la cuenta es 100')
def current_balance():
    pytest.AMT = 100
 

@when('El titular retira 30')
def withdrawal_amount():
    pytest.AMT = pytest.AMT - 30


@then('El saldo de la cuenta es 70')
def final_balance():
    assert pytest.AMT == 70