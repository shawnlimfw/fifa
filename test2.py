
league_table = {'B': {'W': 3, 'D':8, 'L':10, 'F':90, 'A':12},
 'A': {'W': 3, 'D':9, 'L':10, 'F':90, 'A':12},
 'F': {'W': 8, 'D':12, 'L':10, 'F':90, 'A':12},
 'C': {'W': 10, 'D':2, 'L':10, 'F':90, 'A':12},
 'E': {'W': 2, 'D':1, 'L':10, 'F':90, 'A':12},
 'L': {'W': 4, 'D':0, 'L':10, 'F':90, 'A':12},
 'D': {'W': 3, 'D':8, 'L':10, 'F':90, 'A':12},}

new = dict(sorted(league_table.items(), key=lambda item: (-item[1]['W']*3 - item[1]['D'], -item[1]['F']+item[1]['A'], item[0])))

print(new)