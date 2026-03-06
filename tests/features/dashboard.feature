Feature: Dashboard Overview Validation

  Background:
    Given the user is on the Dashboard page

  # -----------------------------
  # Global Impact Section
  # -----------------------------
  Scenario: Validate global cost and delay impact
    Then the Cost Impact value should be displayed
    And the Delay value should be displayed

  # -----------------------------
  # Launch Date
  # -----------------------------
  # Scenario: Validate launch date
  #   Then the Launch Date should be displayed
  #   And the Launch Date should match with actual launch date

  # -----------------------------
  # Summary Cards
  # -----------------------------
  Scenario: Validate dashboard summary cards count
    Then the total tasks card should be visible
    And the total tasks card count should match with tasks list
    And the completed tasks card should be visible
    And the completed tasks card count should match with tasks list
    And the ongoing tasks card should be visible
    And the ongoing tasks card count should match with tasks list
    And the at risk tasks card should be visible
    And the at risk tasks card count should match with tasks list


  # -----------------------------
  # Task Completion by Function
  # -----------------------------
  Scenario Outline: Validate task completion by function
    Then the function "<function_name>" should be displayed
    And the total task count for "<function_name>" should match with task list
    And the completed percentage for "<function_name>" should be match between 0 and 100

    Examples:
      | function_name        |
      | Marketing            |
      | Launch Localisation  |
      | Market Access        |
      | Regulatory Team     |
      | Medical Affairs     |
      | Patient Strategy    |
      | Forecasting          |
      | Commerical Effectiveness |
      | Tech Ops |
      | Manufacturing |

  # -----------------------------
  # Country Wise Launch Status
  # -----------------------------
  # Scenario Outline: Validate country-wise launch status
  #   Then the country "<country_name>" should be displayed
  #   And the task at risk count for "<country_name>" should be greater than or equal to 0
  #   And the task delayed count for "<country_name>" should be greater than or equal to 0
  #   And the task at risk percentage for "<country_name>" should be between 0 and 100
  #   And the task delayed percentage for "<country_name>" should be between 0 and 100

  #   Examples:
  #     | country_name |
  #     | USA          |
  #     | Germany      |

  # # -----------------------------
  # # Cross Data Consistency
  # # -----------------------------
  Scenario: Validate task count consistency
    Then the sum of Completed, Ongoing, delayed and At Risk tasks should be equal to Total Tasks