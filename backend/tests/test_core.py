import pytest
from main import generate, to_gender_enum, to_version_enum, Version, Gender

@pytest.mark.parametrize("input,expected", [
        (None, Gender.MALE),
        ("male", Gender.MALE),
        ("MALE", Gender.MALE),
        ("MaLe", Gender.MALE),
        ("mAlE", Gender.MALE),
        ("FEMALE", Gender.FEMALE),
        ("female", Gender.FEMALE),
        ("fEmAle", Gender.FEMALE),
    ])

def test_gender_enum_works(input, expected):

    result = to_gender_enum(input)

    assert expected == result

@pytest.mark.parametrize("input,expected", [
        (None, Version.ANIMAL),
        ("animal", Version.ANIMAL),
        ("ANIMAL", Version.ANIMAL),
        ("aNiMaL", Version.ANIMAL),
        ("norse", Version.NORSE),
        ("NORSE", Version.NORSE),
        ("NoRSe", Version.NORSE),
        ("norwegian", Version.NORWEGIAN),
        ("NORWEGIAN", Version.NORWEGIAN),
        ("NoRWEgiAN", Version.NORWEGIAN),
        ("nynorsk", Version.NYNORSK),
        ("NYNORSK", Version.NYNORSK),
        ("NyNoRsK", Version.NYNORSK)
    ])

def test_version_enum_works(input, expected):

    result = to_version_enum(input)

    assert expected == result

def test_generate_animal_works():
    result = generate(Version.ANIMAL)

    assert result != None



    # assert result == Type.MALE

# def generate_type_animal_works():
#     element = 

# def test_generate_animal_name():
#     element = generate_animal_name()
#     assert element != None
#     assert len(element) == 2


#     name, adj = generate_animal_name()

#     assert name != None
#     assert len(name) >= 3
#     assert adj!= None
#     assert len(adj) >= 3

# def test_generate_male_name():
#     element = generate_male_name()

#     assert element != None
#     assert len(element) == 2


# def test_generate_female_name():
#     element = generate_female_name()

#     assert element != None
#     assert len(element) == 2