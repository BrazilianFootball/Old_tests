from functions import *
import networkx as nx
from ipywidgets import *
from csv import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_files = {'America/MG' : 'Escudos\\americamg_bra.png',
             'AthleticoParanaense/PR' : 'Escudos\\atleticopr_bra.png',
             'Atletico/GO' : 'Escudos\\atleticogo_bra.png',
             'Atletico/MG' : 'Escudos\\atleticomg_bra.png',
             'Avai/SC' : 'Escudos\\avai_bra.png',
             'Bahia/BA' : 'Escudos\\bahia.png',
             'Botafogo/RJ' : 'Escudos\\botafogorj_bra.png',
             'CSA/AL' : 'Escudos\\csa_bra.png',
             'Ceara/CE' : 'Escudos\\ceara_bra.png',
             'Chapecoense/SC' : 'Escudos\\chapecoense_bra.png',
             'Corinthians/SP' : 'Escudos\\corinthians_bra.png',
             'Coritiba/PR' : 'Escudos\\coritiba_bra.png',
             'Criciuma/SC' : 'Escudos\\criciuma_bra.png',
             'Cruzeiro/MG' : 'Escudos\\cruzeiro_bra.png',
             'Figueirense/SC' : 'Escudos\\figueirense.png',
             'Flamengo/RJ' : 'Escudos\\flarj.png',
             'Fluminense/RJ' : 'Escudos\\flurj.png',
             'Fortaleza/CE' : 'Escudos\\fortaleza.png',
             'Goias/GO' : 'Escudos\\goias.png',
             'Gremio/RS' : 'Escudos\\gremio.png',
             'Internacional/RS' : 'Escudos\\internacional_bra.png',
             'Joinville/SC' : 'Escudos\\joinville.png',
             'Nautico/PE' : 'Escudos\\nautico.png',
             'Palmeiras/SP' : 'Escudos\\palmeiras.png',
             'Parana/PR' : 'Escudos\\parana.png',
             'PontePreta/SP' : 'Escudos\\pontepreta_bra.png',
             'Portuguesa/SP' : 'Escudos\\portuguesasp_bra.png',
             'RedBullBragantino/SP' : 'Escudos\\bragantino_bra.png',
             'SantaCruz/PE' : 'Escudos\\santa.png',
             'Santos/SP' : 'Escudos\\santos.png',
             'SaoPaulo/SP' : 'Escudos\\saopaulo_bra.png',
             'Sport/PE' : 'Escudos\\sport.png',
             'Tubarao/SC' : 'Escudos\\atleticotubarao_sc.png',
             'VascodaGama/RJ' : 'Escudos\\vasco.png',
             'Vitoria/BA' : 'Escudos\\vitoria.png'}

def change(string, old_char, new_char):
    new_string = ''
    for char in string:
        if char == old_char:
            new_string += new_char
        else:
            new_string += char
    return new_string

def replace(string):
    changes = [('á', 'a'), ('à', 'a'), ('â', 'a'), ('ã', 'a'),
               ('é', 'e'), ('ê', 'e'), ('í', 'i'), ('ó', 'o'),
               ('ô', 'o'), ('õ', 'o'), ('ú', 'u'), ('ç', 'c')]
    new_string = string
    for pair in changes:
        new_string = change(new_string, pair[0], pair[1])

    # abaixo uma gambiarra para evitar times duplicados
    if new_string == 'BOTAFOGO/RJ':
        new_string = 'Botafogo/RJ'
    elif new_string == 'Atletico/PR' or new_string == 'ATLETICO/PR':
        new_string = 'AthleticoParanaense/PR'
    elif new_string == 'A.b.c./':
        new_strig = 'A.b.c./RN'
    elif new_string == 'A.s.a./' or new_string == 'A.s.a./AL':
        new_strig = 'Asa/AL'
    elif new_string == 'America/' or new_string == 'AmericaFc/MG':
        new_strig = 'America/MG'
    elif new_string == 'A.s.a./':
        new_strig = 'A.s.a./AL'
    elif new_string == 'AMÉRICA/RN':
        new_strig = 'America/RN'
    elif new_string == 'AVAÍ/SC' or new_string == 'Avai/':
        new_strig = 'Avai/SC'
    elif new_string == 'Arapongas/PR':
        new_strig = 'ArapongasEsporteClube/PR'
    elif new_string == 'BOTAFOGO/PB':
        new_string = 'Botafogo/PB'
    elif new_string == 'Boa/':
        new_string = 'Boa/MG'
    elif new_string == 'Bragantino/' or new_string == 'Bragantino/SP':
        new_string = 'RedBullBragantino/SP'
    elif new_string == 'C.R.B./AL' or new_string == 'C.r.b./AL' or new_string == 'Crb/AL':
        new_string = 'CRB/AL'
    elif new_string == 'C.s.a./AL' or new_string == 'C.S.A./AL' or new_string == 'Csa/AL':
        new_string = 'CSA/AL'
    elif new_string == 'CAXIAS/RS' or new_string == 'SerCaxias/RS':
        new_string = 'Caxias/RS'
    elif new_string == 'CORITIBA/PR':
        new_string = 'Coritiba/PR'
    elif new_string == 'CRICIÚMA/SC':
        new_string = 'Criciuma/SC'
    elif new_string == 'Ceara/':
        new_string = 'Ceara/CE'
    elif new_string == 'Chapecoense/':
        new_string = 'Chapecoense/SC'
    elif new_string == 'FIGUEIRENSE/SC' or new_string == 'Figueirense/':
        new_string = 'Figueirense/SC'
    elif new_string == 'FORTALEZA/CE':
        new_string = 'Fortaleza/CE'
    elif new_string == 'INDEPENDENTE/PA':
        new_string = 'Independente/PA'
    elif new_string == 'Icasa/':
        new_string = 'Icasa/CE'
    elif new_string == 'Joinville/':
        new_string = 'Joinville/SC'
    elif new_string == 'MURICI/AL' or new_string == 'MURICIFUTEBOLCLUBE/AL':
        new_string = 'Murici/AL'
    elif new_string == 'MaringaFutebolClube/PR':
        new_string = 'Maringa/PR'
    elif new_string == 'Oeste/':
        new_string = 'Oeste/SP'
    elif new_string == 'PIAUÍ/PI':
        new_string = 'Piaui/PI'
    elif new_string == 'PONTEPRETA/SP':
        new_string = 'PontePreta/SP'
    elif new_string == 'PalmasLtda/TO':
        new_string = 'Palmas/TO'
    elif new_string == 'Palmeiras/':
        new_string = 'Palmeiras/SP'
    elif new_string == 'Parana/':
        new_string = 'Parana/PR'
    elif new_string == 'Paysandu/':
        new_string = 'Paysandu/PA'
    elif new_string == 'REALNOROESTE/ES' or new_string == 'RealNoroesteCapixaba/ES' or new_string == 'RealNoroesteF.C./ES':
        new_string = 'RealNoroeste/ES'
    elif new_string == 'RiverA.c./PI' or new_string == 'RÍVER/PI':
        new_string = 'River/PI'
    elif new_string == 'SAMPAIOCORREA/MA':
        new_string = 'SampaioCorrea/MA'
    elif new_string == 'SANTOS/SP':
        new_string = 'Santos/SP'
    elif new_string == 'SantosFutebolClube/AP':
        new_string = 'Santos/AP'
    elif new_string == 'SaoCaetano/':
        new_string = 'SaoCaetano/SP'
    elif new_string == 'SerraF.C./ES':
        new_string = 'Serra/ES'
    elif new_string == 'Sobradinho(df)/DF':
        new_string = 'Sobradinho/DF'
    elif new_string == 'VillaNovaA.c./MG':
        new_string = 'VillaNova/MG'
    elif new_string == 'YpirangaRs/RS':
        new_string = 'Ypiranga/RS'
    elif new_string == 'ÁGUIANEGRA/MS' or new_string == 'ÁguiaNegra/MS':
        new_string = 'AguiaNegra/MS'
    elif new_string == 'ÁguiadeMaraba/PA':
        new_string = 'AguiadeMaraba/PA'
    
    return new_string

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
                                        players[year - 2013].append([line[0], replace(team), 1, [competition]])
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
                        team1 = replace(line[1])
                        team2 = replace(line[2])
                        
                        if team1 not in list_of_clubs:
                            list_of_clubs.append(team1)
                        if team2 not in list_of_clubs:
                            list_of_clubs.append(team2)

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
    G = nx.Graph()
    for club in relation:
        G.add_node(club[0][0], color = 'steelblue', weight = club[0][1])

    for club in relation:
        for i in range(1, len(club)):
            G.add_edge(club[0][0], club[i][0], color = 'lightskyblue', width = club[i][1])

    fig, ax = plt.subplots(figsize = (20, 20))
    pos = nx.spring_layout(G, scale = 1)
    nx.draw_networkx_edge_labels(G,
                                 pos,
                                 edge_labels = nx.get_edge_attributes(G, 'relation'),
                                 label_pos = 1.5,
                                 font_size = 9,
                                 font_color = 'red',
                                 font_family = 'sans-serif',
                                 font_weight = 'normal',
                                 alpha = 1.0,
                                 bbox = None,
                                 ax = ax,
                                 rotate = True)

    nx.draw_networkx(G,
                     pos = pos,
                     ax = ax,
                     node_color = [nx.get_node_attributes(G, 'color')[g] for g in G.nodes()],
                     edge_color = [nx.get_edge_attributes(G, 'color')[g] for g in G.edges()],
                     node_size = [nx.get_node_attributes(G, 'weight')[g] * 10 for g in G.nodes()],
                     width = [nx.get_edge_attributes(G, 'width')[g] * 0.5 for g in G.edges])

    print(text)
    trans = ax.transData.transform
    trans2 = fig.transFigure.inverted().transform
    weights = nx.get_node_attributes(G, 'weight')
    w_max = 0
    w_min = 1000
    for club in weights:
        if weights[club] > w_max:
            w_max = weights[club]
        if weights[club] < w_min:
            w_min = weights[club]

    dif = w_max - w_min
    new = 0
    relabel = {}
    
    for g in G.nodes():
        if g in img_files:
            img = mpimg.imread(img_files[g])
            weight = nx.get_node_attributes(G, 'weight')[g]
            # option A (great)
            imsize = (weight - w_min)/dif * 0.04 + 0.02
            # option B (reasonable)
            # imsize = weight/w_max * 0.05
            # option C (terrible)
            # imsize = weight/w_min * 0.03
            
            (x, y) = pos[g]
            xx, yy = trans((x, y))
            xa, ya = trans2((xx, yy))
            a = plt.axes([xa - imsize/2.0, ya - imsize/2.0, imsize, imsize])
            a.imshow(img)
            a.set_aspect('equal')
            a.axis('off')
            relabel[g] = new
            new += 1

    nx.relabel_nodes(G, relabel, copy = False)
                
    plt.show()
    return G, pos, ax, fig
