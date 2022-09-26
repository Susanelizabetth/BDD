from pytest_bdd import scenarios, given, then, when, parsers

scenarios('./myfeatures/feature_4.feature')

class Process:
    @staticmethod
    def calculate(num):
        result = ""
        if num % 3 == 0:
            result += "Tresss"
        if num % 5 == 0:
            result += "Cincoo"
        return result if result else f"{num}"

@given(parsers.parse('the number {number:d}'), target_fixture = 'value')
def get_number(number):
    return dict(number=number)

@when('calculates the result')
def calculate(value):
    value['result'] = Process.calculate(value['number'])
    
@then(parsers.parse('the result should be {result}'))
def validate_result(value, result):
    assert value['result'] == result