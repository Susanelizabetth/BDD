
from pytest_bdd import given, when, then, parsers, scenarios
    
scenarios('./myfeatures/feature_2.feature')

@given(parsers.parse('there are {start:d} cucumbers'),target_fixture='cucumbers')
def existing_cucumbers(start):
   return dict(start=start)
 
@when(parsers.parse('I deposit {deposit:d} cucumbers'))
def deposit_cucumbers(cucumbers, deposit):
    cucumbers['deposit'] = deposit
    print(cucumbers)
    
@when(parsers.parse('I withdraw {withdraw:d} cucumbers'))
def withdraw_cucumbers(withdraw, cucumbers):
    cucumbers['withdraw'] = withdraw
    print(cucumbers)

@then(parsers.parse('I should have {end:d} cucumbers'))
def final_cucumbers(cucumbers, end):
    assert cucumbers['start'] + cucumbers['deposit'] - cucumbers['end'] == end