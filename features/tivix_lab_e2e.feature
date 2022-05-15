# Created by amiendlarzewski at 15.05.2022
Feature: As a User
  I would like to use tivix rental portal
  so that I can successfully rent a car


  Scenario: Successful car rental
    Given User is at http://qalab.pl.tivixlabs.com/ web page
    And User waits for Car rental page to be loaded
    When User selects desired country to Poland
    And User selects desired city to Wroclaw
    And User Chooses desired card model Corsa
    And User sets car pick up date to 2022-05-20
    And User sets car drop off date to 2022-05-25
    And User clicks search button
    Then User will see list of available cars for rent


