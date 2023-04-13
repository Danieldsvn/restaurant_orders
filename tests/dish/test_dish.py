import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    lasanha = Dish("lasanha", 20.00)
    assert lasanha.name == "lasanha"
    assert repr(lasanha) == "Dish('lasanha', R$20.00)"

    lasanha2 = Dish("lasanha", 20.00)
    assert hash(lasanha) == hash(lasanha2)
    assert lasanha == lasanha2

    lasanha_grande = Dish("lasanha", 30.00)
    assert hash(lasanha) != hash(lasanha_grande)

    presunto = Ingredient("presunto")
    lasanha.add_ingredient_dependency(presunto, 1)

    # Teste do método get_ingredientes
    ingredients = []
    for ingredient in lasanha.get_ingredients():
        ingredients.append(repr(ingredient))

    ingredient_bollean = False

    if "Ingredient('presunto')" in ingredients:
        ingredient_bollean = True
    assert ingredient_bollean is True

    # Teste do método get_restrictions
    restriction1 = "<Restriction.ANIMAL_MEAT: 'ANIMAL_MEAT'>"
    restriction2 = "<Restriction.ANIMAL_DERIVED: 'ANIMAL_DERIVED'>"
    restrictions = []

    for item in lasanha.get_restrictions():
        restrictions.append(repr(item))

    restrictions_boolean = False

    if restriction1 in restrictions and restriction2 in restrictions:
        restrictions_boolean = True
    assert restrictions_boolean is True

    # Testes do valor de price
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("lasanha", "20")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("lasanha", -20)
