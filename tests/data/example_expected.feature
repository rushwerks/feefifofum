Feature: Example test file for formatter
  This is an example feature file with poor formatting


  Scenario: Test scenario for formatting

    Given some contract and business partner data exists in system A
      | contract_id | bp_id |
      | contract_1  | 1     |
      | contract_2  | 2     |

    And some contracts data exists in system B
      # Some random comment
      | contract_id |
      | contract_1  |
      | contract_3  |

    Then the output table should show missing contract data and the error type
      """
      Some other random comment
      """
      | contract_id | error_type       | missing_in |
      | contract_2  | missing contract | B          |
      | contract_3  | missing contract | A          |
