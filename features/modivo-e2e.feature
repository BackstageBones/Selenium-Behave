# Created by amiendlarzewski at 27.06.2022
Feature: As a User I would like to create an order
  and successfully browse through checkout page

  Scenario: Successful checkout - modivo web store
    Given User is at modivo online shopping store
    And User chooses Womans clothing
    And Users selects New products type of clothing from the header pane
    And User chooses Clothes type of clothing with selection for BLOUSES_AND_SHIRTS
    When User chooses Size filter for Top garmets with detailed size M 38
    And User adds a cloth to cart
    And User proceeds to checkout page