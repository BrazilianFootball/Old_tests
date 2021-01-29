import os

# create main folders
try:
    os.stat('..\All data')
except:
    os.mkdir('..\All data')

try:
    os.stat('..\Participations and Goals')
except:
    os.mkdir('..\Participations and Goals')

def create_folders(competitions, years):
    for competition in competitions:
        try:
            os.stat(competition)
        except:
            os.mkdir(competition)
        for year in years:
            try:
                os.stat(competition + '\\' + year)
            except:
                os.mkdir(competition + '\\' + year)

years = [str(i) for i in range(2013, 2021)]

# create competitions folders to scrape
competitions = ['..\All data\Serie A',
                '..\All data\Serie B',
                '..\All data\Serie C',
                '..\All data\Serie D',
                '..\All data\Copa do Brasil']

create_folders(competitions, years)

# create competitions folders to relevant data
competitions = ['..\Participations and Goals\Serie A',
                '..\Participations and Goals\Serie B',
                '..\Participations and Goals\Serie C',
                '..\Participations and Goals\Serie D',
                '..\Participations and Goals\Copa do Brasil']

create_folders(competitions, years)
