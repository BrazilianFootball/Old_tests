import tabula
import csv
import time

competicoes = [['/142', 'Serie A'], ['/242', 'Serie B'], ['/342', 'Serie C'], ['/542', 'Serie D'], ['/424', 'Copa do Brasil']]
end_path = 'se.pdf'

with open('errors.csv', 'w', newline = '') as file:
	writer = csv.writer(file)
	writer.writerow(['Competição', 'Ano', 'Jogo'])
	for i in range(3, 11):
                if i == 10:
                        path = 'https://conteudo.cbf.com.br/sumulas/2020'
                        for j in range(600):
                                if (j + 1) % 100 == 0:
                                        print("Ano: 2020", "Jogos:", j)
                                for comp in competicoes:
                                        file = path + comp[0] + str(j + 1) + end_path
                                        try:
                                                tabula.convert_into(file, comp[1] + '/2020/Jogo ' + str(j + 1) + '.csv', pages = 'all')
                                                time.sleep(0.1)
                                        except:
                                                writer.writerow([comp[1], '2020', str(j + 1)])
                else:
        		path = 'https://conteudo.cbf.com.br/sumulas/201' + str(i)
                	for j in range(600):
                        	if (j + 1) % 100 == 0:
                                	print("Ano: 201" + str(i), "Jogos:", j)
        			for comp in competicoes:
                			file = path + comp[0] + str(j + 1) + end_path
                        		try:
                                                tabula.convert_into(file, comp[1] + '/201' + str(i) + '/Jogo ' + str(j + 1) + '.csv', pages = 'all')
                                                time.sleep(0.1)
        				except:
                				writer.writerow([comp[1], '201' + str(i), str(j + 1)])
