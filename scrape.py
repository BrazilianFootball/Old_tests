import tabula
import csv
import time

'''
Scrape for all data of CBF competitions since 2013

General path: https://conteudo.cbf.com.br/sumulas/YEAR/COMPETITION_ID + GAME_NUMBER + se.pdf

j up to 600 to catch all games of all competitions
'''
competitions = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
years = [str(i) for i in range(2013, 2021)]
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

competitions = [['/142', 'Serie A'], ['/242', 'Serie B'], ['/342', 'Serie C'], ['/542', 'Serie D'], ['/424', 'Copa do Brasil']]
end_path = 'se.pdf'

with open('errors.csv', 'w', newline = '') as file:
	writer = csv.writer(file)
	writer.writerow(['Competição', 'Ano', 'Jogo'])
	for i in range(13, 21):
        	path = 'https://conteudo.cbf.com.br/sumulas/20' + str(i)
        	for j in range(600):
                	if (j + 1) % 100 == 0:
                                print("Ano: 20" + str(i), "Jogos:", j)
        		for comp in competitions:
                		file = path + comp[0] + str(j + 1) + end_path
                		try:
                                        if j < 9:
                                                game = '00' + str(j + 1)
                                        elif j < 99:
                                                game = '0' + str(j + 1)
                                        else:
                                                game = str(j + 1)
                                        tabula.convert_into(file, comp[1] + '/20' + str(i) + '/Game ' + game + '.csv', pages = 'all')
                                        time.sleep(0.1)
        			except:
                			writer.writerow([comp[1], '20' + str(i), game])
