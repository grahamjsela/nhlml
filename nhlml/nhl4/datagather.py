import csv
import datetime
from urllib.request import Request, urlopen
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd


def main():

    f = open('game_stats.csv', mode="w")

    fl = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    i = 1

    fl.writerow(['game_id','away_team_name', 'away_id', 'away_powerPlayPercentage', 'away_savePctg', 'away_shootingPctg', 'away_shots', 'away_shotsAllowed', 'away_penaltyKillPercentage', 'away_powerplayspergame', 'away_faceOffWinPercentage', 'home_team_name', 'home_id', 'home_powerPlayPercentage', 'home_savePctg', 'home_shootingPctg', 'home_shots', 'home_shotsAllowed', 'home_penaltyKillPercentage', 'home_powerplayspergame', 'home_faceOffWinPercentage', 'result'])

    teams = {1: {'name': 'New Jersey Devils', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            2: {'name':'New York Islanders', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            3: {'name':'New York Rangers', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            4: {'name':'Philadelphia Flyers', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            5: {'name':'Pittsburgh Penguins', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            6: {'name':'Boston Bruins', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            7: {'name':'Buffalo Sabres', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            8: {'name':'Montréal Canadiens', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            9: {'name':'Ottawa Senators', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            10: {'name':'Toronto Maple Leafs', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            12: {'name':'Carolina Hurricanes', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            13: {'name':'Florida Panthers', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            14: {'name':'Tampa Bay Lightning', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            15: {'name':'Washington Capitals', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            16: {'name':'Chicago Blackhawks', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            17: {'name':'Detroit Red Wings', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            18: {'name':'Nashville Predators', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            19: {'name':'St. Louis Blues', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            20: {'name':'Calgary Flames', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            21: {'name':'Colorado Avalanche', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            22: {'name':'Edmonton Oilers', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            23: {'name':'Vancouver Canucks', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            24: {'name':'Anaheim Ducks', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            25: {'name':'Dallas Stars', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            26: {'name':'Los Angeles Kings', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            28: {'name':'San Jose Sharks', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            29: {'name':'Columbus Blue Jackets', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            30: {'name':'Minnesota Wild', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            52: {'name':'Winnipeg Jets', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            53: {'name':'Arizona Coyotes', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0},
            54: {'name': 'Vegas Golden Knights', 'games': 0.0, 'powerPlayPercentage': 0.0, 'savePctg': 0.0, 'shootingPctg': 0.0, 'shotsPerGame': 0.0, 'shotsAllowed': 0.0, 'penaltyKillPercentage': 0.0, 'powerplayspergame': 0.0, 'faceOffWinPercentage': 0.0}}

    j = 1
    
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
            away_id = int(data['teams']['away']['team']['id'])
            home_team_name = str(data['teams']['home']['team']['name'])
            home_id = int(data['teams']['home']['team']['id'])
            away_games = teams[away_id]['games']
            home_games = teams[home_id]['games']
            if (away_games != 0):
                if(home_games != 0):
                    away_powerPlayPercentage = teams[away_id]['powerPlayPercentage'] / away_games
                    away_savePctg = teams[away_id]['savePctg'] / away_games
                    away_shootingPctg = teams[away_id]['shootingPctg'] / away_games
                    away_shots = teams[away_id]['shotsPerGame'] / away_games
                    away_shotsAllowed = teams[away_id]['shotsAllowed'] / away_games
                    away_penaltyKillPercentage = teams[away_id]['penaltyKillPercentage'] / away_games
                    away_powerplayspergame = teams[away_id]['powerplayspergame'] / away_games
                    away_faceOffWinPercentage = teams[away_id]['faceOffWinPercentage'] / away_games

                    home_powerPlayPercentage = teams[home_id]['powerPlayPercentage'] / home_games
                    home_savePctg = teams[home_id]['savePctg'] / home_games
                    home_shootingPctg = teams[home_id]['shootingPctg'] / home_games
                    home_shots = teams[home_id]['shotsPerGame'] / home_games
                    home_shotsAllowed = teams[home_id]['shotsAllowed'] / home_games
                    home_penaltyKillPercentage = teams[home_id]['penaltyKillPercentage'] / home_games
                    home_powerplayspergame = teams[home_id]['powerplayspergame'] / home_games
                    home_faceOffWinPercentage = teams[home_id]['faceOffWinPercentage'] / home_games

                    away_goals = data['teams']['away']['teamStats']['teamSkaterStats']['goals']
                    home_goals = data['teams']['home']['teamStats']['teamSkaterStats']['goals']

                    

                    if j == 1:
                        result = home_goals - away_goals

                        fl.writerow([game_id,away_team_name, away_id, away_powerPlayPercentage, away_savePctg, away_shootingPctg, away_shots, away_shotsAllowed, away_penaltyKillPercentage, away_powerplayspergame, away_faceOffWinPercentage, home_team_name, home_id, home_powerPlayPercentage, home_savePctg, home_shootingPctg, home_shots, home_shotsAllowed, home_penaltyKillPercentage, home_powerplayspergame, home_faceOffWinPercentage, result])
                    else:
                        result = away_goals - home_goals
                        fl.writerow([game_id, home_team_name, home_id, home_powerPlayPercentage, home_savePctg, home_shootingPctg, home_shots, home_shotsAllowed, home_penaltyKillPercentage, home_powerplayspergame, home_faceOffWinPercentage, away_team_name, away_id, away_powerPlayPercentage, away_savePctg, away_shootingPctg, away_shots, away_shotsAllowed, away_penaltyKillPercentage, away_powerplayspergame, away_faceOffWinPercentage, result])
                    j = (j + 1)%2
            
            else:
                pass
            
           
            teams[away_id]['powerPlayPercentage'] = teams[away_id]['powerPlayPercentage'] + float(data['teams']['away']['teamStats']['teamSkaterStats']['powerPlayPercentage'])
            teams[away_id]['savePctg'] = float(teams[away_id]['savePctg']) + ((float(data['teams']['home']['teamStats']['teamSkaterStats']['shots']) - float(data['teams']['home']['teamStats']['teamSkaterStats']['goals']))/float(data['teams']['home']['teamStats']['teamSkaterStats']['shots']))
            teams[away_id]['shootingPctg'] = teams[away_id]['shootingPctg'] + float(data['teams']['away']['teamStats']['teamSkaterStats']['goals'] /data['teams']['away']['teamStats']['teamSkaterStats']['shots'])
            teams[away_id]['shotsPerGame'] = teams[away_id]['shotsPerGame'] + float(data['teams']['away']['teamStats']['teamSkaterStats']['shots'])
            teams[away_id]['shotsAllowed'] = teams[away_id]['shotsAllowed'] + float(data['teams']['home']['teamStats']['teamSkaterStats']['shots'])
            teams[away_id]['penaltyKillPercentage'] = float(teams[away_id]['penaltyKillPercentage']) + float(1.0 - float(data['teams']['home']['teamStats']['teamSkaterStats']['powerPlayPercentage']))
            teams[away_id]['powerplayspergame'] = teams[away_id]['powerplayspergame'] + float(data['teams']['away']['teamStats']['teamSkaterStats']['powerPlayOpportunities'])
            teams[away_id]['faceOffWinPercentage'] = teams[away_id]['faceOffWinPercentage'] + float(data['teams']['away']['teamStats']['teamSkaterStats']['faceOffWinPercentage'])
            teams[away_id]['games'] = teams[away_id]['games'] + 1

            teams[home_id]['powerPlayPercentage'] = teams[home_id]['powerPlayPercentage'] + float(data['teams']['home']['teamStats']['teamSkaterStats']['powerPlayPercentage'])
            teams[home_id]['savePctg'] = teams[home_id]['savePctg'] + ((float(data['teams']['away']['teamStats']['teamSkaterStats']['shots']) - float(data['teams']['away']['teamStats']['teamSkaterStats']['goals']))/float(data['teams']['away']['teamStats']['teamSkaterStats']['shots']))
            teams[home_id]['shootingPctg'] = teams[home_id]['shootingPctg'] + float(data['teams']['home']['teamStats']['teamSkaterStats']['goals'] / data['teams']['home']['teamStats']['teamSkaterStats']['shots'])
            teams[home_id]['shotsPerGame'] = teams[home_id]['shotsPerGame'] + float(data['teams']['home']['teamStats']['teamSkaterStats']['shots'])
            teams[home_id]['shotsAllowed'] = teams[home_id]['shotsAllowed'] + float(data['teams']['away']['teamStats']['teamSkaterStats']['shots'])
            teams[home_id]['penaltyKillPercentage'] = teams[home_id]['penaltyKillPercentage'] + float(1.0 - float(data['teams']['away']['teamStats']['teamSkaterStats']['powerPlayPercentage']))
            teams[home_id]['powerplayspergame'] = teams[home_id]['powerplayspergame'] + float(data['teams']['home']['teamStats']['teamSkaterStats']['powerPlayOpportunities'])
            teams[home_id]['faceOffWinPercentage'] = teams[home_id]['faceOffWinPercentage'] + float(data['teams']['home']['teamStats']['teamSkaterStats']['faceOffWinPercentage'])
            teams[home_id]['games'] = teams[home_id]['games'] + 1

        i = i + 1

    

    

if __name__ == "__main__":
    main()



