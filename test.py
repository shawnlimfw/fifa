import csv

with open('filtered_male_players.csv', mode='w') as file:
    pass
with open('all_players.csv', mode='r', newline='', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            int(row[0])
        except:
            with open('filtered_male_players.csv', mode='a', newline='', encoding="utf8") as nfile:
                writer = csv.writer(nfile)
                writer.writerow(['Index']+row[3:5]+row[40:41]+row[46:51])
                continue
        if int(row[0]) < 16161:
            with open('filtered_male_players.csv', mode='a', newline='', encoding="utf8") as nfile:
                writer = csv.writer(nfile)
                writer.writerow([str(int(row[0])+1)]+row[3:5]+row[40:41]+row[46:51])