Feature: Overview Management

Background:
  Given the user is on the Overview page

Scenario: Validate overview count widgets
  Then the At Risk widget should be displayed
  And the count of At Risk should be match with list count
  Then the Delayed widget should be displayed
  And the count of Delayed should be match with list count

Scenario: Validate overview percentage widgets
  Then the Finished task widget should be displayed
  And the percentage of finished tasks should be match with list count
  Then the Budget Utilised widget should be displayed
  And the percentage of Budget Utilised should be match with list count


# Scenario: Validate overview graphs
#   Then the "Task Timeline" graph should be displayed
#   And the "Budget" graph should be displayed