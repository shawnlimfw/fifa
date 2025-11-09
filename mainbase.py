import csv
player_database = {}

def initilisation():
    def setup_player_database():
        global player_database
        with open('filtered_male_players.csv', mode='r', newline='', encoding="utf8") as file:
            headers = []
            reader = csv.reader(file)
            for row in reader:
                try:
                    int(row[0])
                except:
                    for header in row:
                        headers.append(header)
                    continue
                identifier = (row[0], row[1])
                player_database[identifier] = {}
                for index, attribute in enumerate(row):
                    player_database[identifier][headers[index]] = attribute

    setup_player_database()


#main code starts here?
initilisation()




            
