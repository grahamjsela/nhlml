import csv
from urllib.request import Request, urlopen
import json
import requests


def main():

    f = open('averages.csv', mode="w")

    fl = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    fl.writerow(['id', 'name', 'powerPlayPercentage', 'powerplayspergame', 'penaltyKillPercentage', 'shotsPerGame', 'shotsAllowed', 'savePctg', 'shootingPctg', 'faceOffWinPercentage'])
    
    url = 'https://statsapi.web.nhl.com/api/v1/teams'
    
    all_teams = requests.get(url).text
    teams = json.loads(all_teams)
    
    teams = teams['teams']

    for i in range(len(teams)):
        id = str(teams[i]['id'])
        name = str(teams[i]['name'])

        url = 'https://statsapi.web.nhl.com/api/v1/teams/{}/stats'.format(id)
        data = json.loads(requests.get(url).text)


        powerPlayPercentage = str(data['stats'][0]['splits'][0]['stat']['powerPlayPercentage'])
        savePctg = str(data['stats'][0]['splits'][0]['stat']['savePctg'])
        shootingPctg = str(data['stats'][0]['splits'][0]['stat']['shootingPctg'])
        shotsPerGame = str(data['stats'][0]['splits'][0]['stat']['shotsPerGame'])
        shotsAllowed = str(data['stats'][0]['splits'][0]['stat']['shotsAllowed'])
        penaltyKillPercentage = str(data['stats'][0]['splits'][0]['stat']['penaltyKillPercentage'])
        powerplayspergame = str(data['stats'][0]['splits'][0]['stat']['powerPlayOpportunities'] / data['stats'][0]['splits'][0]['stat']['gamesPlayed'])
        faceOffWinPercentage = str(data['stats'][0]['splits'][0]['stat']['faceOffWinPercentage'])

        fl.writerow([id, name, powerPlayPercentage, powerplayspergame, penaltyKillPercentage, shotsPerGame, shotsAllowed, savePctg, shootingPctg, faceOffWinPercentage])


    f.close


if __name__ == "__main__":
    main()
