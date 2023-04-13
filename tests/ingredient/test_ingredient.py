from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req  1
def test_ingredient():
    manteiga = Ingredient("manteiga")
    assert repr(manteiga) == "Ingredient('manteiga')"
    assert manteiga.name == "manteiga"

    manteiga2 = Ingredient("manteiga")
    assert manteiga == manteiga2
    assert hash(manteiga) == hash(manteiga2)

    presunto = Ingredient("presunto")
    assert presunto != manteiga
    assert hash(presunto) != hash(manteiga)

    restriction1 = "<Restriction.ANIMAL_MEAT: 'ANIMAL_MEAT'>"
    restriction2 = "<Restriction.ANIMAL_DERIVED: 'ANIMAL_DERIVED'>"
    restrictions = []

    for item in presunto.restrictions:
        restrictions.append(repr(item))

    restrictions_boolean = False

    if restriction1 in restrictions and restriction2 in restrictions:
        restrictions_boolean = True
    assert restrictions_boolean is True
