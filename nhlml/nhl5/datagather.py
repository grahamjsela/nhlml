import csv
import datetime
from os import P_PGID
from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup
from bs4.element import PYTHON_SPECIFIC_ENCODINGS
import requests
import pandas as pd


def main():

    f = open('game_stats.csv', mode="a")

    fl = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    df = pd.read_csv('game_stats.csv', header = 0)

    index = len(df.index) - 1

    i = int(df.iloc[-1]['game_id']) + 1
    
    while(1):

        if i < 10:
            game_id = '000' + str(i)
        elif i < 100:
            game_id = '00' + str(i)
        elif i < 1000:
            game_id = '0' + str(i)
        else:
            game_id = str(i)

        url = 'https://statsapi.web.nhl.com/api/v1/game/202002{}/boxscore'.format(game_id)
        
        test = requests.get(url).text
        data = json.loads(test)
        try:
            message = data['message']
            print("Game not available")
            f.close
            return
        except:
            pass

        if int(data['teams']['away']['teamStats']['teamSkaterStats']['shots']) != 0:
            away_team_name = str(data['teams']['away']['team']['name'])
            away_id = str(data['teams']['away']['team']['id'])
            away_powerPlayPercentage = str(data['teams']['away']['teamStats']['teamSkaterStats']['powerPlayPercentage'])
            away_savePctg = str((float(data['teams']['home']['teamStats']['teamSkaterStats']['shots']) - float(data['teams']['home']['teamStats']['teamSkaterStats']['goals']))/float(data['teams']['home']['teamStats']['teamSkaterStats']['shots']))
            away_shootingPctg = str(data['teams']['away']['teamStats']['teamSkaterStats']['goals'] /data['teams']['away']['teamStats']['teamSkaterStats']['shots'])
            away_shots = str(data['teams']['away']['teamStats']['teamSkaterStats']['shots'])
            away_shotsAllowed = str(data['teams']['home']['teamStats']['teamSkaterStats']['shots'])
            away_penaltyKillPercentage = str(1 - float(data['teams']['home']['teamStats']['teamSkaterStats']['powerPlayPercentage']))
            away_powerplayspergame = str(data['teams']['away']['teamStats']['teamSkaterStats']['powerPlayOpportunities'])
            away_faceOffWinPercentage = str(data['teams']['away']['teamStats']['teamSkaterStats']['faceOffWinPercentage'])

            home_team_name = str(data['teams']['home']['team']['name'])
            home_id = str(data['teams']['home']['team']['id'])
            home_powerPlayPercentage = str(data['teams']['home']['teamStats']['teamSkaterStats']['powerPlayPercentage'])
            home_savePctg = str((float(data['teams']['away']['teamStats']['teamSkaterStats']['shots']) - float(data['teams']['away']['teamStats']['teamSkaterStats']['goals']))/float(data['teams']['away']['teamStats']['teamSkaterStats']['shots']))
            home_shootingPctg = str(data['teams']['home']['teamStats']['teamSkaterStats']['goals'] / data['teams']['home']['teamStats']['teamSkaterStats']['shots'])
            home_shots = str(data['teams']['home']['teamStats']['teamSkaterStats']['shots'])
            home_shotsAllowed = str(data['teams']['away']['teamStats']['teamSkaterStats']['shots'])
            home_penaltyKillPercentage = str(1 - float(data['teams']['away']['teamStats']['teamSkaterStats']['powerPlayPercentage']))
            home_powerplayspergame = str(data['teams']['home']['teamStats']['teamSkaterStats']['powerPlayOpportunities'])
            home_faceOffWinPercentage = str(data['teams']['home']['teamStats']['teamSkaterStats']['faceOffWinPercentage'])

            away_goals = data['teams']['away']['teamStats']['teamSkaterStats']['goals']
            home_goals = data['teams']['home']['teamStats']['teamSkaterStats']['goals']

            if home_goals > away_goals:
                result = '1'
            else:
                result = '0'

            
            fl.writerow([game_id,away_team_name, away_id, away_powerPlayPercentage, away_savePctg, away_shootingPctg, away_shots, away_shotsAllowed, away_penaltyKillPercentage, away_powerplayspergame, away_faceOffWinPercentage, home_team_name, home_id, home_powerPlayPercentage, home_savePctg, home_shootingPctg, home_shots, home_shotsAllowed, home_penaltyKillPercentage, home_powerplayspergame, home_faceOffWinPercentage, result])

        i = i + 1

    f.close


if __name__ == "__main__":
    main()



