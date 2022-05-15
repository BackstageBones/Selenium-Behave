# Created by amiendlarzewski at 15.05.2022
Feature: As a User
  I would like to use tivix rental portal
  so that I can successfully rent a car


  Scenario Outline: Successful car rental
    Given User is at http://qalab.pl.tivixlabs.com/ web page
    And User waits for Car rental page to be loaded
    When User selects desired country to <country>
    And User selects desired city to <city>
    And User Chooses desired card model <model>
    And User sets car pick up date to <pick_up_date>
    And User sets car drop off date to <drop_off_date>
    And User clicks search button
    Then User will see list of available cars for rent

    Examples:
      | country  | city    | model | pick_up_date | drop_off_date |

      | Poland   | Wroclaw | Corsa | 2022-05-20   | 2022-05-25    |
      | France   | Paris   | Focus | 2022-05-10   | 2022-05-18    |
      | Germainy | Berlin  | Fabia | 2022-05-10   | 2021-05-18    |


