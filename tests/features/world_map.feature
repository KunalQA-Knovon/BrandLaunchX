Feature: World Map Management
  As a user
  I want to add a country on the world map
  So that it appears in my map configuration

  Background:
    Given the user is logged in and on the World Map Data page

  Scenario: Verify add country and launch to the world map
    When the user selects a country
    And the user provides a valid sequence number
    And the user selects the expected launch date
    And the user enters the launch budget amount
    And the user selects the launch budget currency
    And the user enters the first-year revenue forecast amount
    # And the user selects the revenue forecast currency
    And the user clicks on the Next button
    Then the country should be added to the world map successfully
    And the user should be navigated to the next page