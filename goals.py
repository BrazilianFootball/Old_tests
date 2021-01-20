from functions import *

folder = 'All data/'
competitions = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

for comp in competitions:
    for year in years:
        path = 'Participations and Goals/' + comp + '/' + year + '/'
        with open(path + 'goals.csv', 'w', newline = '') as file:
            all_goals = [['CBF', 'Time', 'Type', 'Game']]
            writer = csv.writer(file)
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
                    goals = find_goals(file)

                    for i in range(1, len(goals)):
                        all_goals.append([goals[i][0], goals[i][1] + ' - ' + goals[i][2], goals[i][-1] ,'0' * dig + str(game)])
                except:
                    pass
            
            for line in all_goals:
                writer.writerow(line)
