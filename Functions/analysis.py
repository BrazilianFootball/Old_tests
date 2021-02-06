from functions import *
from networkx import *
from ipywidgets import *
from csv import *
from matplotlib.pyplot import *

def preprocessing():
    players = [[year, ['ID', 'Team', 'Games', 'Competitions']] for year in range(2013, 2021)]
    index = [[year] for year in range(2013, 2021)]
    competitions = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil']
    clubs = []
    clubs_lower = []
    path = 'Participations and Goals/'
    
    for year in range(2013, 2021):
        for competition in competitions:
            for game in range(1, 601):
                try:
                    file = path + competition + '/' + str(year) + '/Game ' + str(game) + '.csv'
                    with open(file, mode = 'r') as list_of_players:
                        read = reader(list_of_players, delimiter = ',')
                        for line in read:
                            if line != ['CBF', 'Apelido', 'Nome', 'Nº', 'Clube']:
                                if line[0] != '' and line[0] != 'CBF':
                                    # I saw that some clubs, like Botafogo/RJ, have two diferents names:
                                    # Botafogo/RJ and BOTAFOGO/RJ, for example. So:
                                    if line[-1].lower() not in clubs_lower:
                                        clubs_lower.append(line[-1].lower())
                                        clubs.append(line[-1])

                                    ind = clubs_lower.index(line[-1].lower())
                                    team = clubs[ind]
                            
                                    if [line[0], line[-1]] not in index[year - 2013]:
                                        index[year - 2013].append([line[0], team])
                                        players[year - 2013].append([line[0], team, 1, [competition]])
                                    else:
                                        ind = index[year - 2013].index([line[0], team])
                                        players[year - 2013][ind][2] += 1
                                        if competition not in players[year - 2013][ind][3]:
                                            players[year - 2013][ind][3].append(competition)
                except:
                    pass
    return players

def clubs(competitions, years):
    list_of_clubs = []
    for year in years:
        for competition in competitions:
            file = 'Participations and Goals/{}/{}/Index.csv'.format(competition, str(year))
            with open(file, mode = 'r') as index:
                read = reader(index, delimiter = ',')
                for line in read:
                    if line != ['Game', 'Home', 'Away']:
                        if line[1] not in list_of_clubs:
                            list_of_clubs.append(line[1])
                        if line[2] not in list_of_clubs:
                            list_of_clubs.append(line[2])

    return list_of_clubs

def relations_one_club(team, players):
    athletes = []
    athletes_clubs = []
    clubs_lower = []

    for ind in range(len(players)):
        for player in players[ind]:
            if type(player) == list and player != ['ID', 'Team', 'Games', 'Competitions']:
                if team.lower() in player[1].lower() and player[0] not in athletes:
                    athletes.append(player[0])
                    athletes_clubs.append([player[0], team])
                    clubs_lower.append([team.lower()])

    for ind in range(len(players)):
        for player in players[ind]:
            if type(player) == list and player[0] in athletes:
                place = athletes.index(player[0])
                if player[1].lower() not in clubs_lower[place]:
                    clubs_lower[place].append(player[1].lower())
                    athletes_clubs[place].append(player[1])
            
    clubs = [[team, len(athletes)]]
    clubs_lower = [team.lower()]
    for element in athletes_clubs:
        for club in element:
            if not club.isdigit():
                if club.lower() not in clubs_lower and club != team:
                    clubs_lower.append(club.lower())
                    clubs.append([club, 1])
                elif club.lower() in clubs_lower and club != team:
                    ind = clubs_lower.index(club.lower())
                    clubs[ind][1] += 1
                
    clubs = sorted(clubs, key = lambda x : x[1], reverse = True)
    return clubs

def relations_list_of_clubs(list_of_clubs, players):
    relations = []
    for club in list_of_clubs:
        relations.append(relations_one_club(club, players))

    for club in relations:
        i = 1
        while i < len(club):
            if club[i][0] not in list_of_clubs:
                club.remove(club[i])
            else:
                i += 1
    
    return relations

def graph(relation):
    text = 'Below we can see what relationship exists between the players of each club. Each node represents a club and an edge between\ntwo nodes represents that these clubs have players in commom (that is, players who have served in both clubs).\n\nThe bigger the node, the more players passed through the club.\nSimilarly, a thicker edge represents that the two clubs have more players in commom.'
    G = Graph()
    for club in relation:
        G.add_node(club[0][0], color = 'steelblue', weight = club[0][1])

    for club in relation:
        for i in range(1, len(club)):
            G.add_edge(club[0][0], club[i][0], color = 'lightskyblue', width = club[i][1])

    fig, ax = subplots(figsize = (20, 20))
    pos = spring_layout(G, scale = 1)
    draw_networkx_edge_labels(G,
                              pos,
                              edge_labels = get_edge_attributes(G, 'relation'),
                              label_pos = 1.5,
                              font_size = 9,
                              font_color = 'red',
                              font_family = 'sans-serif',
                              font_weight = 'normal',
                              alpha = 1.0,
                              bbox = None,
                              ax = ax,
                              rotate = True)

    draw_networkx(G,
                  pos = pos,
                  ax = ax,
                  node_color = [get_node_attributes(G, 'color')[g] for g in G.nodes()],
                  edge_color = [get_edge_attributes(G, 'color')[g] for g in G.edges()],
                  node_size = [get_node_attributes(G, 'weight')[g] * 10 for g in G.nodes()],
                  width = [get_edge_attributes(G, 'width')[g] * 0.5 for g in G.edges])

    print(text)
    show()
