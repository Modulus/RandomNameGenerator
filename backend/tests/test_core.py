from main import generate_animal_name, generate_male_name, generate_female_name


def test_generate_animal_name():
    element = generate_animal_name()
    assert element != None
    assert len(element) == 2


    name, adj = generate_animal_name()

    assert name != None
    assert len(name) >= 3
    assert adj!= None
    assert len(adj) >= 3

def test_generate_male_name():
    element = generate_male_name()

    assert element != None
    assert len(element) == 2


def test_generate_female_name():
    element = generate_female_name()

    assert element != None
    assert len(element) == 2