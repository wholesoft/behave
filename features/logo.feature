Feature: Wholesoft Notes Logo

  Scenario: Logo present on Wholesoft Notes home page
     Given launch chrome browser
      When open Wholesoft Notes home page
      Then verify that the logo is present on the page
      And close the browser