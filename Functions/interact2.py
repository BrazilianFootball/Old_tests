from analysis3 import *
from IPython.display import display
#from ipywidgets import interactive, HBox, SelectMultiple, IntRangeSlider, BoundedIntText

players = preprocessing()

def visu1():
    competitions = SelectMultiple(options = ['Serie A', 'Serie B', 'Serie C', 'Serie D', 'Copa do Brasil'],
                                  value = ['Serie A'],
                                  description = 'Competitions:',
                                  disabled = False)

    years = IntRangeSlider(value = [2019, 2020],
                           min = 2013,
                           max = 2020,
                           step = 1,
                           description = 'Period:',
                           disabled = False,
                           continuous_update = False,
                           orientation = 'horizontal',
                           readout = True,
                           readout_format = 'd')

    max_clubs = BoundedIntText(value = 20,
                               min = 5,
                               max = 40,
                               step = 1,
                               description = 'Nº Nodes (max):',
                               disabled = False)

    save = Checkbox(value = False,
                    description = 'Save')

    def visualization(competitions, years, max_clubs, save):
        years = [i for i in range(years[0], years[1] + 1)] 
        list_of_clubs = find_clubs(competitions, years)
        relation = relations_list_of_clubs(list_of_clubs, players)
        relation.sort(reverse = True, key = lambda x : x[0][1])
        if max_clubs < len(relation):
            relation = relation[0:max_clubs]
        else:
            max_clubs = len(relation)
    
        graph(relation, competitions, years, max_clubs, save)
            
    ip = interactive(visualization,
                     competitions = competitions,
                     years = years,
                     max_clubs = max_clubs,
                     save = save)

    display(HBox(ip.children[0:2]))
    display(HBox(ip.children[2:4]))

    display(ip.children[-1])

# def visu2():
    # criar outra visualização com os técnicos, ou com gols, inventar algo
