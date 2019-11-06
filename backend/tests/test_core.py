from main import generate_element


def test_generate_element():
    element = generate_element()
    assert element != None
    assert len(element) == 2


    name, adj = generate_element()

    assert name != None
    assert len(name) >= 3
    assert adj!= None
    assert len(adj) >= 3
    