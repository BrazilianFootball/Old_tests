from functions import *

'''
Script to find out which players played each game (time in and time out)
and save to a .csv file
'''

competitions = ['Copa do Brasil']#['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
# years = [str(i) for i in range(2013, 2021)]
years = [str(i) for i in range(2020, 2021)]

with open('../../errors_participations.csv', 'w', newline = '') as error_file:
    error_writer = csv.writer(error_file)
    error_writer.writerow(['Competição', 'Ano', 'Jogo'])
    for year in years:
        # for game in range(1, 601):
        for game in range(119, 121):
            if game % 100 == 0:
                print(year, game)
            for comp in competitions:
                try:
                    file = '../../All data/' + comp + '/' + year + '/Game '
                    path = '../../Participations and Goals/' + comp + '/' + year + '/Game '
                    if game < 10:
                        file += '00' + str(game) + '.csv'
                        path += '00' + str(game) + '.csv'
                    elif game < 100:
                        file += '0' + str(game) + '.csv'
                        path += '0' + str(game) + '.csv'
                    else:
                        file += str(game) + '.csv'
                        path += str(game) + '.csv'
                    participations = find_game_players(file)
                    with open(path, 'w', newline = '') as file:
                        writer = csv.writer(file)
                        for line in participations:
                            writer.writerow(line)
                except:
                    error_writer.writerow([comp, year, game])
