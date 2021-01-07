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
        players = ['CBF', 'Apelido', 'Nome', 'Nº', 'Clube']
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