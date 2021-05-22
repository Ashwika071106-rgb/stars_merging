import pandas as pd
import csv

df = pd.read_csv("dwarf_stars.csv")

for i in df:
    df = df[df['distance'].notna()]

    for data in df:
        df[3] = df[3] *  0.000954588 
        df[4] = df[4] *  0.102763

df.tocsv("changed_values.csv")

changed_values = []
bright_stars = []

with open("changed_values.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        changed_values.append(row)

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        bright_stars.append(row)

headers_1 = changed_values[0]
changed_values = changed_values[1:]

headers_2 = bright_stars[0]
planet_data_2 = bright_stars[1:]

headers = headers_1 + headers_2

dwarf_stars_data = []

for index, data_row in enumerate(changed_values):
    dwarf_stars_data.append(changed_values[index] + bright_stars[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(dwarf_stars_data)
