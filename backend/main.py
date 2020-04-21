# -*- coding: utf-8 -*-

import pandas

import logging
import sys
from enum import Enum


logger = logging.getLogger("main")

class Version(Enum):
    NORWEGIAN = 1
    ANIMAL = 2
    NORSE = 3
    NYNORSK = 4


class Gender(Enum):
    MALE = 1
    FEMALE = 2

def len_animals():
    with open("./resources/animals.csv") as animals_file:
        return sum(1 for line in animals_file)

def len_adjectives():
    with open("./resources/adjectives.csv") as adjectives_file:
        return sum(1 for line in adjectives_file)

def amount_combos():
    return len_animals() * len_adjectives()

def to_gender_enum(gender_string):
    if gender_string:
        if gender_string.lower() == "male":
            return Gender.MALE
        else:
            return Gender.FEMALE
    return Gender.MALE

def to_version_enum(version_string):
    if version_string:
        if version_string.lower() == "animal":
            return Version.ANIMAL
        elif version_string.lower() == "norwegian":
            return Version.NORWEGIAN
        elif version_string.lower() == "norse":
            return Version.NORSE
        elif version_string.lower() == "nynorsk":
            return Version.NYNORSK
        else:
            return Version.ANIMAL
    else:
        return Version.ANIMAL

def generate(version, gender=None):
    if version == Version.NORWEGIAN:
        if gender == Gender.MALE:
            return generate_element(first_file="./resources/norwegian_boys.csv", second_file="./resources/norwegian_last.csv")
        else:
            return generate_element(first_file="./resources/norwegian_girls.csv", second_file="./resources/norwegian_last.csv")
    elif version == Version.NORSE:
        if gender == Gender.MALE:
            return generate_element(first_file="./resources/norse_male.csv", second_file="./resources/norse_male_last.csv")
        else:
            return generate_element(first_file="./resources/norse_female.csv", second_file="./resources/norse_female_last.csv")
    elif version == Version.NYNORSK:
        if gender == Gender.MALE:
            first_name_a, first_name_b = generate_element(first_file="./resources/nynorsk/first_female_a.csv", second_file="./resources/nynorsk/first_female_a.csv")
            last_name_a, last_name_b = generate_element(first_file="./resources/nynorsk/first_female_a.csv", second_file="./resources/nynorsk/first_female_a.csv")
            return ("{}{}".format(first_name_a, first_name_b), "{}{}".format(last_name_a, last_name_b))
        else:
            first_name_a, first_name_b = generate_element(first_file="./resources/nynorsk/first_female_a.csv", second_file="./resources/nynorsk/first_female_a.csv")
            last_name_a, last_name_b = generate_element(first_file="./resources/nynorsk/first_female_a.csv", second_file="./resources/nynorsk/first_female_a.csv") 
            return ("{}{}".format(first_name_a, first_name_b), "{}{}".format(last_name_a, last_name_b))
    else:
        return generate_element(first_file="./resources/adjectives.csv", second_file="./resources/animals.csv")
             


def generate_element(first_file, second_file):

    first_full_df = pandas.read_csv(first_file)

    first_df = first_full_df.sample()
    first_value = first_df.values[0][0]

    logger.debug("First value sampled", value=f"{first_value}")

    second_full_df = pandas.read_csv(second_file)
    second_df = second_full_df.sample()

    second_value = second_df.values[0][0]

    logger.debug("Second value sampled", second_value=f"{second_value}")

    # Replace spaces with - in animal name
    #animal_name = animal_name.replace(" ", "-")
    logger.debug(f"Returning  {first_value} {second_value}")

    return first_value.capitalize().strip(), second_value.capitalize().strip()




# if __name__ == "__main__":
#     adjective, animal = generate_animal_name()
#     print(f"{adjective.capitalize()}-{animal.capitalize()}")
#     print(f"{len_animals()}")
#     print(f"{len_adjectives()}")
