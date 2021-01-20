from functions import *

folder = 'All data/'
competitions = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
all_players = []

for comp in competitions:
    for year in years:
        print(comp, year)    
        for game in range(1, 601):
            try:
                if game < 10:
                    file = folder + comp + '/' + year + '/Game 00' + str(game) + '.csv'
                elif game < 100:
                    file = folder + comp + '/' + year + '/Game 0' + str(game) + '.csv'
                else:
                    file = folder + comp + '/' + year + '/Game ' + str(game) + '.csv'
                players = find_players(file)
                for player in players:
                    if player[:3] not in all_players:
                        all_players.append(player[:3])
            except:
                pass

with open('players.csv', 'w', newline = '') as file:
	writer = csv.writer(file)
	for line in all_players:
            writer.writerow(line)
