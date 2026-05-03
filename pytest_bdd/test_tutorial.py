from pytest_bdd import given, scenarios, then, when


scenarios("tutorial.feature")


@given("we have pytest-bdd installed", target_fixture="installed")
def pytest_bdd_installed():
    return True


@when("we implement a test")
def implement_test():
    assert True


@then("pytest-bdd will test it for us!")
def it_tests_for_us(installed):
    assert installed