Feature: Orange Basket
    As a farmer,
    I want to carry oranges in a basket,
    So that I will be able to carry large number of oranges easily,

Scenario: Add oranges to a basket
    Given the basket has 2 oranges
    When 4 oranges are added to the basket
    Then the basket contains 6 oranges