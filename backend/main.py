import pandas
import structlog


def len_animals():
    with open("./resources/animals.csv") as animals_file:
        return sum(1 for line in animals_file)

def len_adjectives():
    with open("./resources/adjectives.csv") as adjectives_file:
        return sum(1 for line in adjectives_file)

def amount_combos():
    return len_animals() * len_adjectives()

def generate_element():
    logger = structlog.get_logger()

    animals_df = pandas.read_csv("./resources/animals.csv")

    animal_name_df = animals_df.sample()
    print(animal_name_df)
    animal_name = animal_name_df.values[0][0]

    logger.msg("animal name sampled", name=f"{animal_name}")

    adjectives_df = pandas.read_csv("./resources/adjectives.csv")
    adjective_df = adjectives_df.sample()

    adjective = adjective_df.values[0][0]

    logger.msg("adjective sampled", adjective=f"{adjective}")

    # Replace spaces with - in animal name
    animal_name = animal_name.replace(" ", "-")
    logger.msg(f"Returning  {adjective} {animal_name}")

    return adjective.capitalize(), animal_name.capitalize()


if __name__ == "__main__":
    adjective, animal = generate_element()
    print(f"{adjective.capitalize()}-{animal.capitalize()}")
    print(f"{len_animals()}")
    print(f"{len_adjectives()}")
