# Reflection 1: Python makes it easier to automate tasks and work with large amounts of data, while Excel is easier for viewing data and making charts. Python is also better for repeating tasks without doing everything manually.

# Reflection 2: A business could use append mode to keep track of daily sales. Append mode is useful because it adds new records without deleting the old ones, making it easier to track sales over time.

import csv
from datetime import datetime
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

# Exercise 7

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

print("\nSales Summary by Product:")

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# Exercise 8

current_time = datetime.now()

with open("data/run_log.txt", "a") as log_file:
    log_file.write(
        f"{current_time}: Total Revenue = ${total_revenue:.2f}\n"
    )

print("\nRevenue logged successfully.")