# Created by amiendlarzewski at 27.06.2022
Feature: As a User I would like to create an order
  and successfully browse through checkout page

   Scenario: Successful checkout - modivo web store
    Given User is at https://modivo.pl/ web page
     And User chooses Womans clothing
     And Users selects New products type of clothing from the header pane
     When User chooses Size filter for Top garmets with detailed size 38