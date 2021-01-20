import csv

def remove_space(string):
    new_string = ''
    for carac in string:
        if carac != ' ':
            new_string += carac
    
    return new_string

def find_carac(string, carac, n = 1):
    cont = 0
    for i in range(len(string)):
        if string[i] in carac:
            if cont < n - 1:
                cont += 1
            else:
                return i
    if cont == n:
        return len(string) - 1
    else:
        return None

def teams(line):
    team = []
    for element in line:
        if element != '':
            team.append(element)
    team1 = team[0]
    team2 = team[1]
    team1 = remove_space(team1)
    team2 = remove_space(team2)
    
    return team1, team2

def find_name(string):
    names = string.split()
    for i in range(len(names)):
        if names[i] == names[0]:
            div = i
    
    if div == 0:
        apelido = names[0]
        nome = ''
        for i in range(len(names)):
            if i != 0:
                if i == len(names) - 1:
                    nome += names[i]
                else:
                    nome += names[i] + ' '
    else:
        apelido = ''
        nome = ''
        for i in range(len(names)):
            if i < div:
                if i == div - 1:
                    apelido += names[i]
                else:
                    apelido += names[i] + ' '
            else:
                if i == len(names) - 1:
                    nome += names[i]
                else:
                    nome += names[i] + ' '
    
    return apelido, nome

def list2string(line):
    string = line[0]
    for i in range(1, len(line)):
        if line[i] not in 'T(g)RPA':
            string += ' ' + line[i]
            
    return string

def catch_data(all_data):
    if all_data[1] == ' ':
        no = all_data[0]
        n = 7
        begin_name = 2
    else:
        no = all_data[:2]
        n = 8
        begin_name = 3
    
    end_player = find_carac(all_data, '0123456789', n)
    complete_name = all_data[begin_name:end_player - 6]
    apelido, nome = find_name(complete_name)
    CBF = all_data[end_player - 5:end_player + 1]
    
    return CBF, apelido, nome, no, end_player

def find_players(file):
    with open(file) as output_file:
        fplayer = False
        players = [['CBF', 'Apelido', 'Nome', 'Nº', 'Clube']]
        reader = csv.reader(output_file, delimiter = ',')
        error = 0
        for line in reader:
            if 'Relação de Jogadores' in line:
                fplayer = True
                cont = 0

            if fplayer:
                try:
                    int(line[0])
                except:
                    try:
                        int(line[5][0])
                    except:
                        error += 1
                
                if error > 3:
                    break
                
                if cont == 1:
                    team1, team2 = teams(line)
                elif cont > 2:
                    if len(line) == 12:
                        CBF = line[5]
                        apelido = line[1]
                        nome = line[2]
                        no = line[0]
                        clube = team1
                        players.append([CBF, apelido, nome, no, clube])
                        CBF = line[11]
                        apelido = line[7]
                        nome = line[8]
                        no = line[6]
                        clube = team2
                        players.append([CBF, apelido, nome, no, clube])
                    else:
                        if line[0] == '':
                            clube = team2
                        else:
                            clube = team1
                        
                        all_data = list2string(list2string(line).split())
                        CBF, apelido, nome, no, end_player = catch_data(all_data)
                        players.append([CBF, apelido, nome, no, clube])
                        if clube == team1 and end_player != len(all_data) - 1:
                            clube = team2
                            all_data = all_data[end_player + 2:]
                            CBF, apelido, nome, no, end_player = catch_data(all_data)
                            players.append([CBF, apelido, nome, no, clube])
                            
                cont += 1

    return players

def list2string2(line):
    string = line[0]
    for i in range(1, len(line)):
        if line[i] != '':
            string += ' ' + line[i]
            
    return string

def find_game_players(file):
    with open(file) as output_file:
        subs = False
        changes = [['CBF', 'In', 'Out', 'Nº', 'Clube']]
        reader = csv.reader(output_file, delimiter = ',')
        error = 0
        players = find_players(file)
        for player in players[1:23]:
            player[1] = '00:00 - 1T'
            player[2] = '45:00 - 2T'
            changes.append(player)
            
        for line in reader:
            if 'Substituições' in line:
                subs = True
                cont = 0

            if subs:
                try:
                    int(line[0][0])
                except:
                    try:
                        int(line[5][0])
                    except:
                        error += 1
                
                if error > 2:
                    break
                
                if cont > 1:
                    if len(line) == 5:
                        if line[1] == 'INT':
                            time = 'INT'
                        else:
                            time = line[0] + ' - ' + line[1]
                        clube = line[2]
                        player_in = line[3]
                        player_out = line[4]
                        if player_in[1] == ' ':
                            no_in = player_in[0]
                        else:
                            no_in = player_in[:2]
                        
                        if player_out[1] == ' ':
                            no_out = player_out[0]
                        else:
                            no_out = player_out[:2]
                    else:
                        all_data = list2string2(line)
                        tp = find_carac(all_data, ':')
                        if all_data[tp + 4] == 'I':
                            time = 'INT'
                        else:
                            time = all_data[:tp + 3] + ' - ' + all_data[tp + 4: tp + 6]
                        
                        end_clube = find_carac(all_data[tp + 6:], '0123456789') - 1
                        if time == 'INT':
                            clube = all_data[tp + 8:tp + 6 + end_clube]
                        else:
                            clube = all_data[tp + 7:tp + 6 + end_clube]
                            
                        if all_data[tp + 6 + end_clube + 2] == ' ':
                            no_in = all_data[tp + 6 + end_clube + 1]
                        else:
                            no_in = all_data[tp + 6 + end_clube + 1:tp + 6 + end_clube + 3]
                        
                        bn = find_carac(all_data[tp + 6 + end_clube + 3:], '0123456789')
                        
                        if all_data[tp + 6 + end_clube + 3 + bn + 1] == ' ':
                            no_out = all_data[tp + 6 + end_clube + 3 + bn]
                        else:
                            no_out = all_data[tp + 6 + end_clube + 3 + bn:tp + 6 + end_clube + 3 + bn + 2]
                        
                    for player in players:
                        if player[3] == no_in and player[4] == clube:
                            player[1] = time
                            player[2] = '45 - 2T'
                            changes.append(player)

                    for player in changes:
                        if player[3] == no_out and player[4] == clube:
                            player[2] = time
                        
                        
                cont += 1

    return changes

def find_goals(file):
    players = find_players(file)
    with open(file) as output_file:
        begin = False
        goals = [['CBF', 'Tempo', '1T/2T', 'Type']]
        reader = csv.reader(output_file, delimiter = ',')
        error = 0
        for line in reader:
            if 'Gols' in line:
                begin = True
                cont = 0

            if begin:
                try:
                    int(line[0])
                except:
                    error += 1

                if error > 3:
                    break

                if cont > 1:
                    for player in players:
                        if player[3] == line[2] and player[4] == line[-1]:
                            goals.append([player[0], line[0], line[1], line[3]])

                cont += 1

    return goals
