import os

competicoes = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

for comp in competicoes:
    for year in years:
        for game in range(1, 601):
            old_name = 'Participações/' + comp + '/' + year + '/Jogo ' + str(game) + '.csv'
            new_name = 'Participações/' + comp + '/' + year + '/Game '
            if game < 10:
                new_name += '00' + str(game) + '.csv'
            elif game < 100:
                new_name += '0' + str(game) + '.csv'
            else:
                new_name += str(game) + '.csv'
            try:
                os.rename(old_name, new_name)
            except:
                pass

for comp in competicoes:
    for year in years:
        for game in range(1, 601):
            old_name = 'Súmulas/' + comp + '/' + year + '/Jogo ' + str(game) + '.csv'
            new_name = 'Súmulas/' + comp + '/' + year + '/Game '
            if game < 10:
                new_name += '00' + str(game) + '.csv'
            elif game < 100:
                new_name += '0' + str(game) + '.csv'
            else:
                new_name += str(game) + '.csv'
            try:
                os.rename(old_name, new_name)
            except:
                pass
