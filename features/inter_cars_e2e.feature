# Created by amiendlarzewski at 10.06.2022
Feature: As a User
  I would like to be able to search for different car parts
  so that I can proceed with my purchase

  Scenario: Searching for car part without selecting car brand
    Given User is at https://intercars.com.pl/ web page
    And User waits for search bar to be loaded
    When User enters car part wahacz przedni in the search bar
    Then User will see that ToDo popup is displayed


    Scenario: Searching fo car part with selecting car brand
      Given User is at https://intercars.com.pl/ web page
      And User waits for search bar to be loaded
      When User chooses vehicle make VW, model PASSAT CC B6 and type 3.6 FSI 4MOTION
      And User enters car part wahacz przedni in the search bar
      Then User will see that search results are not displayed