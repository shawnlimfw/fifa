import csv
import re

input_file = "teams_budget.csv"
output_file = "filtered_teams_budget.csv"

with open(input_file, "r", newline="", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        rank, club, value = row

        # 1. Skip rows containing "(W)"
        if "(W)" in club:
            continue

        # 2. Remove currency symbols and commas
        clean_value = re.sub(r"[£€$]", "", value)  # remove symbols and commas
        clean_value = clean_value.replace(",", ".")
        clean_value = clean_value.replace("M", "")  # remove M at the end

        # 3. Convert to float
        # clean_value = float(clean_value)

        # Write cleaned row
        writer.writerow([rank, club, clean_value])
