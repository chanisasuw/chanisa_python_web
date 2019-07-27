Feature: #3 – Invalid Return Dates

  Scenario: When a valid code is entered, the search result should have a “Promotional code [code] used: [discount]% discount!” message.
	  Given User open Mars Airlines Home Page
	  And User verify search flight box that existing
	  And Select "departing" : "July"
	  And Select "returning" : "December (two years from now)"
	  When Enter promotion code "AF3-FJK-418"
	  And User click search button
	  Then User found message promotional code :"Promotional code "
	  And check discount "30% discount"

  Scenario: Otherwise, show “Sorry, code [invalid promo code] is not valid”.
	  Given User open Mars Airlines Home Page
	  And User verify search flight box that existing
	  And Select "departing" : "July"
	  And Select "returning" : "December (two years from now)"
	  When Enter promotion code "TEST"
	  And User click search button
	  Then User found message promotional code :"Sorry, code "


