Feature: #4 – Invalid Return Dates

	Scenario Outline: “Unfortunately, this schedule is not possible. Please try again.” displayed when return date is less than 1 year from the departure.
	  Given User open Mars Airlines Home Page
	  And User verify search flight box that existing
	  And Select "departing" : "<departing>"
	  And Select "returning" : "<returning>"
	  When User click search button
	  Then User found message "Unfortunately, this schedule is not possible. Please try again." 

   Examples: Search flight
   	| departing       			      |  returning								|
   	| July                     		|  July										|
   	| July                     	   |  December									|
   	| December								|	July										|
   	|	December								|	December									|
   	| December								|	July (next year)						|
   	|	July (next year)					|  July										|
   	|	July (next year)					|  December									|
   	|	July (next year)					|  July (next year)						|
   	| July (next year)					|  December (next year)					|
   	| July (two years from now) 		|  July										|
   	| July (two years from now) 		|  December									|
   	| July (two years from now) 		|  July (next year)					 	|
   	| July (two years from now) 		|  December (next year)					|
   	| July (two years from now) 		|  July (two years from now) 	      |
   	| July (two years from now) 		|  December (two years from now) 	|
   	| December (two years from now) 	|  July  									|  	
   	| December (two years from now) 	|  December  								|  	
   	| December (two years from now) 	|  July (next year)	  					|  
   	| December (two years from now) 	|  December (next year)	  				| 
   	| December (two years from now) 	|  July (two years from now) 			|
   	| December (two years from now) 	|  December (two years from now) 	|
