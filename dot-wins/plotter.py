import pandas as pd
import matplotlib.pyplot as plt
import pickle


TEAMS = ['TOR', 'NYK', 'GSW', 'POR', 'BOS', 'BRK', 'PHI', 'CLE',
         'SAC', 'DEN', 'SAS', 'LAL', 'LAC', 'DET', 'WAS', 'MIA',
         'HOU', 'MIL', 'ATL', 'ORL', 'UTA', 'PHO', 'CHO', 'OKC',
         'MIN', 'DAL', 'IND', 'CHI', 'MEM', 'NOP', 'NJN', 'CHA',
         'CHH', 'VAN', 'NOH', 'NOK', 'SEA']

CURRENT_TEAMS = sorted(['TOR', 'NYK', 'GSW', 'POR', 'BOS', 'BRK', 'PHI', 'CLE',
                 'SAC', 'DEN', 'SAS', 'LAL', 'LAC', 'DET', 'WAS', 'MIA',
                 'HOU', 'MIL', 'ATL', 'ORL', 'UTA', 'PHO', 'CHO', 'OKC',
                        'MIN', 'DAL', 'IND', 'CHI', 'MEM', 'NOP'], reverse=True)
YEARS = list(range(2000, 2018))

CHAMPIONS = {2000: 'LAL',
             2001: 'LAL',
             2002: 'LAL',
             2003: 'SAS',
             2004: 'DET',
             2005: 'SAS',
             2006: 'MIA',
             2007: 'SAS',
             2008: 'BOS',
             2009: 'LAL',
             2010: 'LAL',
             2011: 'DAL',
             2012: 'MIA',
             2013: 'MIA',
             2014: 'SAS',
             2015: 'GSW',
             2016: 'CLE',
             2017: 'GSW'}

def load_data():
    df = pickle.load(open( "df_years.p", "rb"))
    df['COLOR'] = 'black'
    for year in YEARS:
        champ = CHAMPIONS[year]
        df.loc[(df.TEAM==champ) & (df.YEAR==year), 'COLOR'] = 'red'

    team_map = {}
    for index, team in enumerate(CURRENT_TEAMS):
        team_map[team] = index

    df['game_num'] = ((df['YEAR'] - YEARS[0]) * 82) + (df['G'].astype(int) - 1)
    df.loc[df['YEAR']==2012, 'game_num'] = df.loc[df['YEAR']==2012, 'game_num'] + 16
    df['team_num'] = df['TEAM'].map(team_map)

    df_wins = df[(df['W/L'] == 1) & (df['TEAM'].isin(CURRENT_TEAMS))]
    return df_wins

def make_plots(df_wins):
    plt.figure(figsize=(60, 8))
    plt.scatter(df_wins['game_num'], df_wins['team_num'], c=df_wins['COLOR'], s=1)
    for team in CURRENT_TEAMS:
        plt.text(df_wins.game_num.max() + 3, team_map[team] - 0.2, team)
    plt.tight_layout()
    plt.axis('off')
    plt.savefig('wins.pdf', format='pdf', dpi=1200)
