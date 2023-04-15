Feature: Wholesoft Notes Login

Scenario: Login to Wholesoft Notes with valid paramters
Given User launches Chrome browser
When User Opens Home page
And User clicks on login
And User enters the username "test@wholesoft.net"
And User enters the password "testPassword9!"
And User clicks Login
Then User successfully logs in

Scenario: Login to Wholesoft Notes with valid paramters
Given User launches Chrome browser
When User Opens Home page
And User clicks on login
And User enters the username "test@invalid.net"
And User enters the password "invalidpassword"
And User clicks Login
Then User successfully fails to log in
