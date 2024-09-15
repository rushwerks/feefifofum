
Feature: Example test file for formatter
    This is an example feature file with poor formatting
      Scenario: Test scenario for formatting

    Given contracts exist in system A
    |contract_id       |
      |contract_1 |
      | contract_2 |


     And corresponding customers exists in system B
    # Comment 1
      # Comment 2
      | contract_id       | customer_id |
      | contract_1    |customer_1   |
      | contract_3 | customer_2 |

    Then the output table should show missing contract data and the error type
    """
    Multi-line
  comment
    """
    | contract_id      | error_type              | missing_in |
      | contract_2 | missing contract   |B         |
      | contract_3 | missing contract   | A        |
