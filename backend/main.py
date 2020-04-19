import pandas

import logging
import sys


logger = logging.getLogger("main")

def len_animals():
    with open("./resources/animals.csv") as animals_file:
        return sum(1 for line in animals_file)

def len_adjectives():
    with open("./resources/adjectives.csv") as adjectives_file:
        return sum(1 for line in adjectives_file)

def amount_combos():
    return len_animals() * len_adjectives()

def generate_animal_name():
    return generate_element(first_file="./resources/adjectives.csv", second_file="./resources/animals.csv")

def generate_male_name():
    return generate_element(first_file="./resources/norwegian_boys.csv", second_file="./resources/norwegian_last.csv")

def generate_female_name():
    return generate_element(first_file="./resources/norwegian_girls.csv", second_file="./resources/norwegian_last.csv")

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




if __name__ == "__main__":
    adjective, animal = generate_animal_name()
    print(f"{adjective.capitalize()}-{animal.capitalize()}")
    print(f"{len_animals()}")
    print(f"{len_adjectives()}")
