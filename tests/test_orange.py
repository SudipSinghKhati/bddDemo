"""Orange Basket feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

from project.orange import OrangeBasket

@scenario('../feature\orange.feature', 'Add oranges to a basket')
def test_add_oranges_to_a_basket():
    """Add oranges to a basket."""


@given(parsers.parse('the basket has {start:d} oranges'),target_fixture='basket')
def the_basket_has_2_oranges(start):
    """the basket has 2 oranges."""
    return OrangeBasket(initial_count = start)


@when(parsers.parse('{more:d} oranges are added to the basket'))
def oranges_are_added_to_the_basket(basket, more):
    basket.add(more)


@then(parsers.parse('the basket contains {final:d} oranges'))
def the_basket_contains_6_oranges(basket, final):
    assert basket.count == final
  

