import csv

# Exercise 2

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")


# Exercise 5

total_rows = 0
filtered_rows = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                filtered_rows += 1

print(f"Rows written: {filtered_rows}")
print(f"Original rows: {total_rows}")

# Exercise 6

# csv.reader is useful when working with simple CSV files using indexes.
# csv.DictReader is better when accessing columns by their names.

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"\nDictReader Total Revenue: ${dict_total_revenue:.2f}")