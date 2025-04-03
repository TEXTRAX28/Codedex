import csv

with open("Bestseller - Sheet1.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    max_value = 0
    bestsellers = None

    for row in reader:
        current_row = float(row[4])

        if current_row > max_value:
            max_value = current_row
            bestsellers = row

with open("Bestsellers.csv", "w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerow(bestsellers)
    csvfile.close()

print(f"The best seller is: {bestsellers} ")
print(f"With the number of sales (in millions): {bestsellers[4]} ")

