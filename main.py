import pandas
import structlog

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
logger.msg(f"{adjective}{animal_name}")



print(f"{adjective}-{animal_name}")

# import  csv
#
# with open("./resources/animals.csv", "r") as csv_file:
#     reader = csv.reader(csv_file, delimiter=",")
#     animals = list(reader)
#
# with open("resources/adjectives.csv", "r") as csv_file:
#     reader = csv.reader(csv_file, delimiter=",")
#     adjectives = list(reader)
#
# print(animals)
# print(adjectives)