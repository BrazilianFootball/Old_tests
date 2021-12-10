import os
import csv
import time
import tabula
from functions import *

i_year = 2021
f_year = 2021
years = [str(i) for i in range(i_year, f_year + 1)]
print('Creating folders')
def create_folders(competitions, years):
	try:
		os.stat('../../raw_data')
	except:
		os.mkdir('../../raw_data')

	try:
		os.stat('../../clean_data')
	except:
		os.mkdir('../../clean_data')
	
    for competition in competitions:
        try:
            os.stat(competition)
        except:
            os.mkdir(competition)
        for year in years:
            try:
                os.stat(competition + '/' + year)
            except:
                os.mkdir(competition + '/' + year)
                
competitions = ['../../raw_data/Serie A',
                '../../raw_data/Serie B',
                '../../raw_data/Serie C',
                '../../raw_data/Serie D',
                '../../raw_data/Copa do Brasil']

create_folders(competitions, years)
competitions = ['../../clean_data/Serie A',
                '../../clean_data/Serie B',
                '../../clean_data/Serie C',
                '../../clean_data/Serie D',
                '../../clean_data/Copa do Brasil']

create_folders(competitions, years)

print('Scraping')
competitions = [['/142', 'Serie A'],
				['/242', 'Serie B'],
				['/342', 'Serie C'],
				['/542', 'Serie D'],
				['/424', 'Copa do Brasil']]
				
end_path = 'se.pdf'
with open('../../errors.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['Competição', 'Ano', 'Jogo'])
    for i in range(i_year, f_year + 1):
        path = 'https://conteudo.cbf.com.br/sumulas/' + str(i)
        for j in range(600):
            if (j + 1) % 50 == 0:
                print('Ano: ' + str(i), 'Jogos:', j + 1)
            for comp in competitions:
				game = str(j + 1).zfill(3)
        		local = '../../raw_data/' + comp[1] + '/' + str(i) + '/Game ' + game + '.csv'
        		file = path + comp[0] + str(j + 1) + end_path
        		try:
    				tabula.io.convert_into(file, local, pages = 'all')
    				time.sleep(0.1)
        		except:
    				writer.writerow([comp[1], str(i), game])
                
years = [str(i) for i in range(2013, f_year + 1)]
print('Creating index')
folder = '../../raw_data/'
competitions = ['Serie A',
				'Serie B',
				'Serie C',
				'Serie D',
				'Copa do Brasil']
				
for comp in competitions:
    for year in years:
        print(comp, year)
        with open('../../clean_data/' + comp + '/' + year + '/Index.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(['Game', 'Home', 'Away'])
            for game in range(1, 601):
                try:
                    file = folder + comp + '/' + year + '/Game ' + str(game).zfill(3) + '.csv'
                    players = find_players(file)
                    writer.writerow([str(game).zfill(3), players[1][-1], players[2][-1]])
                except:
                    pass
                    
print('Finding players')
all_players = []
for comp in competitions:
    for year in years:
        print(comp, year)    
        for game in range(1, 601):
            try:
                file = folder + comp + '/' + year + '/Game ' + str(game).zfill(3) + '.csv'
                players = find_players(file)
                for player in players:
                    if player[:3] not in all_players:
                        all_players.append(player[:3])
            except:
                pass

print('Excluding duplicates')
IDs = []
final_players = []
for player in all_players:
    if player[0] not in IDs:
        IDs.append(player[0])
        final_players.append(player)
    else:
        index = IDs.index(player[0])
        if len(player[1]) > len(final_players[index][1]):
            final_players[index] = player            

print('Saving players')
with open('../../players.csv', 'w', newline = '') as file:
	writer = csv.writer(file)
	for line in final_players:
            writer.writerow(line)

print('Catching game players')
with open('../../errors_participations.csv', 'w', newline = '') as error_file:
    error_writer = csv.writer(error_file)
    error_writer.writerow(['Competição', 'Ano', 'Jogo'])
    for year in years:
        for game in range(1, 601):
            if game % 100 == 0:
                print(year, game)
            for comp in competitions:
                try:
                    file = '../../raw_data/' + comp + '/' + year + '/Game ' + str(game).zfill(3) + '.csv'
                    path = '../../clean_data/' + comp + '/' + year + '/Game ' + str(game).zfill(3) + '.csv'
                    participations = find_game_players(file)
                    with open(path, 'w', newline = '') as file:
                        writer = csv.writer(file)
                        for line in participations:
                            writer.writerow(line)
                except:
                    error_writer.writerow([comp, year, game])

print('Catching goals')
for comp in competitions:
    for year in years:
        path = '../../clean_data/' + comp + '/' + year + '/'
        with open(path + 'goals.csv', 'w', newline = '') as file:
            all_goals = [['CBF', 'Time', 'Type', 'Game']]
            writer = csv.writer(file)
            for game in range(1, 601):
                try:
                    file = folder + comp + '/' + year + '/Game ' + str(game).zfill(3) + '.csv'
                    goals = find_goals(file)
                    for i in range(1, len(goals)):
                        if goals[i][0].isnumeric():
                            all_goals.append([goals[i][0], goals[i][1] + ' - ' + goals[i][2], goals[i][-1], str(game).zfill(3)])
                except:
                    pass
            
            for line in all_goals:
                writer.writerow(line)
