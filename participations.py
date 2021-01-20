from functions import *

competitions = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

with open('errors_participations.csv', 'w', newline = '') as error_file:
    error_writer = csv.writer(error_file)
    error_writer.writerow(['Competição', 'Ano', 'Jogo'])
    for year in years:
        for game in range(1, 601):
            if game % 100 == 0:
                print(year, game)
            for comp in competitions:
                try:
                    file = 'Súmulas/' + comp + '/' + year + '/Game '
                    path = 'Participações/' + comp + '/' + year + '/Game '
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
