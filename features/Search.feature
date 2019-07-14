Feature: Search

  Scenario: Search PyPI
    Given I open TrueID Home Page
    When I verify main menu that existing  "ดูทีวีออนไลน์"
    Then I am taken to the PyPi Search Results page
    And I see a search result "behave 1.2.5"