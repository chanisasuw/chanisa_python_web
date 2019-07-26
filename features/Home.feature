Feature: Link to Home Page

  Scenario: “Book a ticket to the red planet now!” should apperar somewhere prominent on the page.
    Given User open Mars Airlines Home Page
    When User verify search flight box that existing
    Then User found "Book a ticket to the red planet now!" on search flight box

  Scenario: Clicking the MarsAir logo on the top left should also take the user to the home page.
  	Given User open Mars Airlines Home Page
  	When User clicking MarsAir logo
  	Then Redirect to home page

  Scenario: Clicking the MarsAir logo from search result page
  	Given User open Mars Airlines Home Page
  	And User click search button
  	When User clicking MarsAir logo
  	Then Redirect to home page

  # Scenario: Clicking xxxxxx takes the user to the home page.
  # 	Given User open Mars Airlines Home Page
  # 	When User cicking text "Book"
  # 	Then Redirect to home page