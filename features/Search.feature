Feature: #1 - Basic Serach Flow

  Scenario: There should be ‘departure’ and ‘return’ fields on a search form.
    Given User open Mars Airlines Home Page
    When User verify search flight box that existing
    Then It should be "Departing" field
    And It should be "Returning" field

  Scenario Outline: Flights leave every six months, in July and December, both ways.
  	Given User open Mars Airlines Home Page
    And User verify search flight box that existing
    When Finding "<flight>" Flights leave field
    And Select "<flight>" : "<flightleave>"
    Then "<flight>" found flight leave on "<flightleave>"

	Examples: Departing flight
   	| flight         | flightleave										|
   	| departing      | July        										|
   	| departing      | December  											|
   	| departing      | July (next year) 							|
   	| departing      | December (next year)       		|
   	| departing      | July (two years from now)  		|
   	| departing 		 | December (two years from now) 	|

  Examples: Returning flight
   	| flight         | flightleave										|
   	| returning      | July        										|
   	| returning      | December  											|
   	| returning      | July (next year) 							|
   	| returning      | December (next year)       		|
   	| returning      | July (two years from now)  		|
   	| returning 		 | December (two years from now) 	|


	Scenario Outline: Trips for the next two years should be searchable.
	  Given User open Mars Airlines Home Page
	  And User verify search flight box that existing
	  And Select "departing" : "<departing>"
	  And Select "returning" : "<returning>"
	  When User click search button
	  Then User found message "Sorry, there are no more seats available." 

  Examples: Search flight
   	| departing       			| returning												|
   	| July      						| July (two years from now) 			|
   	| December							| December (two years from now)		|

  Scenario Outline: If there are seats, display “Seats available! Call 0800 MARSAIR to book!”
	  Given User open Mars Airlines Home Page
	  And User verify search flight box that existing
	  And Select "departing" : "<departing>"
	  And Select "returning" : "<returning>"
	  When User click search button
	  Then User found message "Seats available!" 

  Examples: Search flight
   	| departing       			| returning												|
   	| July 						 			|	December (two years from now) 	|

  Scenario Outline: If there are no seats, display “Sorry, there are no more seats available.”
	  Given User open Mars Airlines Home Page
	  And User verify search flight box that existing
	  And Select "departing" : "<departing>"
	  And Select "returning" : "<returning>"
	  When User click search button
	  Then User found message "Sorry, there are no more seats available." 

  Examples: Search flight
   	| departing       			| returning												|
   	| July      						| July (next year)       					|
   	| July      						| December (next year)  					|
   	| July      						| July (two years from now) 			|
   	| December     					| December (next year)						|
   	| December							| July (two years from now)				|
   	| December							| December (two years from now)		|
   	| July (next year) 			| July (two years from now)   		|
   	| July (next year) 			|	December (two years from now) 	|