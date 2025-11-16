import csv

# Step 1: Read the CSV into memory
rows = []
with open("teams_budget.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

# Step 2: Modify the data in memory
# Example: change column 1 of row 2
for row in rows:
    row[0].replace('2', '3')

# Step 3: Write it back
with open("teams_budget.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)