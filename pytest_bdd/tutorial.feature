Feature: showing off pytest-bdd

  Scenario: run a simple test
    Given we have pytest-bdd installed
    When we implement a test
    Then pytest-bdd will test it for us!