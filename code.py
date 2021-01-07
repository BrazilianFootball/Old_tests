import tabula

## Copa do Brasil

path = 'https://conteudo.cbf.com.br/sumulas/2020/424'
end_path = 'se.pdf'

for i in range(112): # tem mais dois jogos para a final, ou seja, vai até 114
	file = path + str(i + 1) + end_path
	tabula.convert_into(file, 'Copa do Brasil/Sumulas/Jogo ' + str(i + 1) + '.csv', pages = 'all')

## Brasileirão

path = 'https://conteudo.cbf.com.br/sumulas/2020/142'
end_path = 'se.pdf'

for i in range(270): # falhas no 3 e 226, vai até o 380 no final do campeonato
	if i == 2:
		pass
	elif i == 225:
		pass
	else:
		file = path + str(i + 1) + end_path
		tabula.convert_into(file, 'Brasileirão/Sumulas/Jogo ' + str(i + 1) + '.csv', pages = 'all')
