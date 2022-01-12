import os
import re
from glob import glob
from Levenshtein import distance

def find_clubs(line):
    line = re.sub('"', '', line)
    line = re.sub(',', '', line)
    sep = line.find('/')
    c1 = line[:sep + 4].strip()
    c2 = line[sep + 4:].strip()

    return c1, c2
    
def treat_club(club):
    if club == 'A.b.c. / RN':
        return 'ABC / RN'
    elif club == 'Abc / RN':
        return 'ABC / RN'
    elif club == 'AVAÍ / SC':
        return 'Avaí / SC'
    elif club == 'A.s.a. / AL':
        return 'ASA / AL'
    elif club == 'America / MG':
        return 'América / MG'
    elif club == 'America Fc / MG':
        return 'América / MG'
    elif club == 'América de Natal / RN':
        return 'América / RN'
    elif club == 'AMÉRICA / RN':
        return 'América / RN'
    elif club == 'Arapongas / PR':
        return 'Arapongas Esporte Clube / PR'
    elif club == 'Atletico / PR':
        return 'Athletico Paranaense / PR'
    elif club == 'ATLETICO / PR':
        return 'Athletico Paranaense / PR'
    elif club == 'Atlético / PR':
        return 'Athletico Paranaense / PR'
    elif club == 'Sobradinho (df) / DF':
        return 'Sobradinho / DF'
    elif club == 'ÁGUIA NEGRA / MS':
        return 'Águia Negra / MS'
    elif club == 'Aguia Negra / MS':
        return 'Águia Negra / MS'
    elif club == 'Aguia / PA':
        return 'Águia de Marabá / PA'
    elif club == 'Ypiranga Rs / RS':
        return 'Ypiranga / RS'
    elif club == 'Vitoria F. C. / ES':
        return 'Vitória / ES'
    elif club == 'Villa Nova A.c. / MG':
        return 'Villa Nova / MG'
    elif club == 'Veranopolis / RS':
        return 'Veranópolis / RS'
    elif club == 'União / MT':
        return 'União de Rondonópolis / MT'
    elif club == 'Serra F. C. / ES':
        return 'Serra / ES'
    elif club == 'Ser Caxias / RS':
        return 'Caxias / RS'
    elif club == 'Santos Futebol Clube / AP':
        return 'Santos / AP'
    elif club == 'Sampaio Correa / MA':
        return 'Sampaio Corrêa / MA'
    elif club == 'SAMPAIO CORREA / MA':
        return 'Sampaio Corrêa / MA'
    elif club == 'SANTOS / SP':
        return 'Santos / SP'
    elif club == 'Bragantino / SP':
        return 'Red Bull Bragantino / SP'
    elif club == 'Maringá Futebol Clube / PR':
        return 'Maringá / PR'
    elif club == 'MURICI / AL':
        return 'Murici / AL'
    elif club == 'MURICI FUTEBOL CLUBE / AL':
        return 'Murici / AL'
    elif club == 'River / PI':
        return 'Ríver / PI'
    elif club == 'River A.c. / PI':
        return 'Ríver / PI'
    elif club == 'RÍVER / PI':
        return 'Ríver / PI'
    elif club == 'REAL NOROESTE / ES':
        return 'Real Noroeste / ES'
    elif club == 'Real Noroeste Capixaba / ES':
        return 'Real Noroeste / ES'
    elif club == 'Real Noroeste F. C. / ES':
        return 'Real Noroeste / ES'
    elif club == 'Palmas Ltda / TO':
        return 'Palmas / TO'
    elif club == 'PONTE PRETA / SP':
        return 'Ponte Preta / SP'
    elif club == 'PIAUÍ / PI':
        return 'Piauí / PI'
    elif club == 'Operario / PR':
        return 'Operário / PR'
    elif club == 'Luziania / DF':
        return 'Luziânia / DF'
    elif club == 'INDEPENDENTE / PA':
        return 'Independente / PA'
    elif club == 'Independente Tucuruí / PA':
        return 'Independente / PA'
    elif club == 'Guarany de Sobral / CE':
        return 'Guarany / CE'
    elif club == 'Guarani de Juazeiro / CE':
        return 'Guarani / CE'
    elif club == 'Fc Cascavel / PR':
        return 'Cascavel / PR'
    elif club == 'Crb / AL':
        return 'CRB / AL'
    elif club == 'Criciuma / SC':
        return 'Criciúma / SC'
    elif club == 'Csa / AL':
        return 'CSA / AL'
    elif club == 'FIGUEIRENSE / SC':
        return 'Figueirense / SC'
    elif club == 'FORTALEZA / CE':
        return 'Fortaleza / CE'
    elif club == 'C. R. B. / AL':
        return 'CRB / AL'
    elif club == 'C.r.a.c. / GO':
        return 'CRAC / GO'
    elif club == 'C.r.b. / AL':
        return 'CRB / AL'
    elif club == 'C.s.a. / AL':
        return 'CSA / AL'
    elif club == 'CAXIAS / RS':
        return 'Caxias / RS'
    elif club == 'CORITIBA / PR':
        return 'Coritiba / PR'
    elif club == 'CRICIÚMA / SC':
        return 'Criciúma / SC'
    elif club == 'Atlético Cearense / CE':
        return 'Atlético / CE'
    elif club == 'Atlético Roraima / RR':
        return 'Atlético / RR'
    elif club == 'BOTAFOGO / PB':
        return 'Botafogo / PB'
    elif club == 'BOTAFOGO / RJ':
        return 'Botafogo / RJ'
    elif club == 'Asa / AL':
        return 'ASA / AL'
    elif club == 'A.s.s.u. / RN':
        return 'ASSU / RN'
    
    return club
    
def treat_player(player):
    aux = re.sub(' ', '', player).strip()
    player = re.sub(',', '', player)
    player = re.sub('"', '', player).strip()
    k = 1
    while k < len(aux) and aux[0:k + 1].isdigit():
        k += 1
        
    no = aux[0:k]
    aux = aux[:-6]
    if aux == '':
    	trpa = ''
    elif 'TP' in aux:
        trpa = 'T P'
    elif 'RP' in aux:
        trpa = 'R P'
    elif 'TA' in aux:
        trpa = 'T A'
    elif 'RA' in aux:
        trpa = 'R A'
    elif 'T(g)P' in aux:
        trpa = 'T(g) P'
    elif 'R(g)P' in aux:
        trpa = 'R(g) P'
    elif 'T(g)A' in aux:
        trpa = 'T(g) A'
    elif 'R(g)A' in aux:
        trpa = 'R(g) A'
    elif aux[-4:] == 'R(g)':
    	trpa = 'R(g) P'
    elif aux[-4:] == 'T(g)':
    	trpa = 'T(g) P'
    elif aux[-1] == 'T':
    	trpa = 'T P'
    elif aux[-1] == 'R':
    	trpa = 'R P'
    else:
        trpa = ''
    
    if trpa in player:
        name = player[player.find(no) + len(no):player.find(trpa)].strip()
    else:
        name = player[player.find(no) + len(no):player.find(re.sub(' ', '', trpa))].strip()
    cbf_id = player[-6:]
    
    return [cbf_id, no, name, trpa]
    
def extract_players(game):
    game_players = []
    file = open(game, encoding = 'ISO-8859-1')
    data = file.readlines()
    file.close()
    cont = 0
    for line in data:
        if cont == 3:
            if line[0].isdigit():
                p0c0 = True
            else:
                p0c0 = False
            
            players = re.sub(',', '', line)
            players = re.sub('"', '', players).strip()
            a = re.findall('\D\d{6}', players)
            if len(a) > 0:
                a = a[0][1:]
                sep = players.find(a)
                p0 = players[:sep + 6]
                p1 = players[sep + 6:]
                if p0c0:
                    game_players.append(treat_player(p0) + [c0])
                    if p1 != '':
                        game_players.append(treat_player(p1) + [c1])
                else:
                    game_players.append(treat_player(p0) + [c1])
                    
            else:
                cont += 1

        if cont == 2:
            cont += 1

        if cont == 1:
            c0, c1 = find_clubs(line)
            c0 = treat_club(c0)
            c1 = treat_club(c1)
            cont += 1

        if 'Relação de Jogadores' in line:
            cont += 1
            
    return game_players
    
def find_change_1(line):
    line = re.sub(' ', '', line).strip()
    sep = line.find('T') + 1
    t = line[:sep]
    if t[-3:] == 'INT':
    	t = t[:-3] + ' - ' + t[-3:]
    else:
	    t = t[:-2] + ' - ' + t[-2:]
	    
    t = re.sub(',', '', t)
    line = line[sep:]
    sep = line.find(re.findall('[0-9]{1,3}', line)[0])
    club = treat_club(re.sub('/', ' / ', re.sub(',', '', line[:sep])))
    line = line[sep:]
    player_in, player_out = re.findall('[0-9]{1,3}', line)
    return t, player_in, player_out, club
    
def extract_participations_1(game):
    players = extract_players(game)
    active_players = [['In', 'Out', 'ID', 'Club']]
    club1 = ''
    club2 = ''
    for player in players:
        if player[3][0] == 'T':
            active_players.append(['00:00 - 1T', '45:00 - 2T', player[0], player[-1]])
            
        if club1 == '':
            club1 = player[-1]
        elif player[-1] != club1:
            club2 = player[-1]
            
    file = open(game, encoding = 'ISO-8859-1')
    data = file.readlines()
    file.close()
    cont = 0
    for line in data:
        if cont == 2 and line[1].isdigit() and not line[2].isdigit():
            t, player_in, player_out, club = find_change_1(line)
            if distance(club, club1) < distance(club, club2):
                club = club1
            else:
                club = club2
                
            for i in range(len(active_players)):
                if re.sub(' ', '', active_players[i][-1]) == club:
                    club = active_players[i][-1]
                    break
                    
            for player in players:
                if player[-1] == club:
                    if player[1] == player_out:
                        player_out = player[0]
                    elif player[1] == player_in:
                        player_in = player[0]
                        
            for i in range(len(active_players)):
                if active_players[i][-1] == club:
                    if active_players[i][2] == player_out:
                        active_players[i][1] = t
                        
            active_players.append([t, '45:00 - 2T', player_in, club])
        elif cont == 1:
            cont += 1
        elif cont == 2:
        	cont += 1
        
        if 'Substituições' in line:
            cont += 1
            
    return active_players

def find_change_2(line):
    line = re.sub(' ', '', line).strip()
    t = line[:5]
    line = line[5:]
    sep = line.find('/') + 3
    club = line[:sep]
    line = line[sep:]
    player_in, player_out = re.findall('[0-9]{1,2}', line)
    return t, player_in, player_out, club

def extract_participations_2(game):
    changes = []
    players = extract_players(game)
    active_players = [['In', 'Out', 'ID', 'Club']]
    club1 = ''
    club2 = ''
    for player in players:
        if player[3][0] == 'T':
            active_players.append(['00:00 - 1T', '45:00 - 2T', player[0], player[-1]])
            
        if club1 == '':
            club1 = player[-1]
        elif player[-1] != club1:
            club2 = player[-1]
            
    file = open(game, encoding = 'ISO-8859-1')
    data = file.readlines()
    file.close()
    cont = 0
    for line in data:
        if cont == 2 and line[1].isdigit():
            t, player_in, player_out, club = find_change_2(line)
            if distance(club, club1) < distance(club, club2):
                club = club1
            else:
                club = club2
                
            for i in range(len(active_players)):
                if re.sub(' ', '', active_players[i][-1]) == club:
                    club = active_players[i][-1]
                    break
                    
            for player in players:
                if player[-1] == club:
                    if player[1] == player_out:
                        player_out = player[0]
                    elif player[1] == player_in:
                        player_in = player[0]
                        
            for i in range(len(active_players)):
                if active_players[i][-1] == club:
                    if active_players[i][2] == player_out:
                        active_players[i][1] = t
                        break
                        
            active_players.append([t, '45:00 - 2T', player_in, club])
            changes.append([t, i, len(active_players) - 1])
        elif cont == 1:
            cont += 1
        
        if 'Substituições' in line:
            cont += 1
    
    max_time = 0
    for i in range(len(changes)):
        if max_time <= int(changes[i][0][:changes[i][0].find(':')]):
            max_time = int(changes[i][0][:changes[i][0].find(':')])
        else:
            i -= 1
            break
            
    for k in range(len(changes)):
        if i == (len(changes) - 1) or k > i:
            active_players[changes[k][1]][1] += ' - 2T'
            active_players[changes[k][2]][0] += ' - 2T'
        elif k <= i:
            active_players[changes[k][1]][1] += ' - 1T'
            active_players[changes[k][2]][0] += ' - 1T'
            
    return active_players
    

