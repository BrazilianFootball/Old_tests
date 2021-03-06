from functions import *

'''
Script to create a .csv file with games index (ID game, home, away)
'''

folder = '../All data/'
competitions = ['Serie A']#, 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
# years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
years = ['2020']
all_players = []

for comp in competitions:
    for year in years:
        print(comp, year)
        with open('../Participations and Goals/' + comp + '/' + year + '/Index.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['Game', 'Home', 'Away'])
            for game in range(1, 601):
                try:
                    if game < 10:
                        file = folder + comp + '/' + year + '/Game 00' + str(game) + '.csv'
                        dig = 2
                    elif game < 100:
                        file = folder + comp + '/' + year + '/Game 0' + str(game) + '.csv'
                        dig = 1
                    else:
                        file = folder + comp + '/' + year + '/Game ' + str(game) + '.csv'
                        dig = 0
                    players = find_players(file)
                    writer.writerow(['0' * dig + str(game), players[1][-1], players[2][-1]])
                except:
                    pass
