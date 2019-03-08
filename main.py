import pandas



dataframe = pandas.read_csv("./resources/animals.csv")

print(dataframe)
print(dataframe.sample(n=1))

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