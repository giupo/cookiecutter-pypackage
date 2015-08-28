from pytest_bdd import scenario, given, when, then

context = dict()


@given('I have the <number>')
def have_the_number(number):
    pass


@when('I compute its factorial')
def compute_its_factorial(number):
    context['result'] = factorial(number)


@then('I see the <result>')
def check_number(result):
    assert result == context['result']


def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number


@scenario('zero.feature', 'Factorial of a number',
          example_converters=dict(number=float, result=float))
def test_zero():
    pass
