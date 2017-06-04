import pickle
import pandas as pd

TEAMS = ['TOR', 'NYK', 'GSW', 'POR', 'BOS', 'BRK', 'PHI', 'CLE',
         'SAC', 'DEN', 'SAS', 'LAL', 'LAC', 'DET', 'WAS', 'MIA',
         'HOU', 'MIL', 'ATL', 'ORL', 'UTA', 'PHO', 'CHO', 'OKC',
         'MIN', 'DAL', 'IND', 'CHI', 'MEM', 'NOP', 'NJN', 'CHA',
         'CHH', 'VAN', 'NOH', 'NOK', 'SEA']
YEARS = list(range(2000, 2018))


def get_results(team, year):
    URL = ("http://www.basketball-reference.com"
           "/teams/{team}/{year}_games.html").format(team=team,
                                                     year=str(year))
    df = pd.read_html(URL)[0]
    df = df[df['G'] != 'G']
    df['TEAM'] = team
    df['YEAR'] = year
    df = df[['YEAR', 'TEAM', 'G', 'Unnamed: 7']]
    df.columns = ['YEAR', 'TEAM', 'G', 'W/L']
    df['W/L'] = df['W/L'].map({'W': 1, 'L': 0})
    return df


def make_year(year, teams=TEAMS):
    df_year = pd.DataFrame()
    for team in teams:
        try:
            df_year = df_year.append(get_results(team, year))
        except:
            print(team, year)
    return df_year


def make_years(years=YEARS, teams=TEAMS, cache=False):
    df_years = pd.DataFrame()
    for year in years:
        print('********', year)
        df_years = df_years.append(make_year(year))
    if cache:
        pickle.dump(df_years, open("df_years.p", "wb"))
    return df_years

df = make_years(cache=True)
