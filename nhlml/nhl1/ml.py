import numpy as np
from numpy.core.records import array
import pandas as pd
from sklearn.neural_network import MLPClassifier
import sys
from sklearn.model_selection import train_test_split
import os


#Main machine learning file. This file pulls the information from the created CSV's and runs a ML program on it, then predicts off of 
#Up to date team average stats. The program runs 1000 times, and creates an average win percentage off of these 1000 'games' played.
#
def main():

    #Open the csv's that were created by the other two files.
    game_stats = pd.read_csv('game_stats.csv', header = 0)
    averages = pd.read_csv('averages.csv', header = 0)

    #Pull the columns that are associated with the X in the ML program.
    X = game_stats[['away_powerPlayPercentage',
                'away_savePctg',
                'away_shootingPctg',
                'away_shots',
                'away_shotsAllowed',
                'away_penaltyKillPercentage',
                'away_powerplayspergame',
                'away_faceOffWinPercentage',
                'home_powerPlayPercentage',
                'home_savePctg',
                'home_shootingPctg',
                'home_shots',
                'home_shotsAllowed',
                'home_penaltyKillPercentage',
                'home_powerplayspergame',
                'home_faceOffWinPercentage',
                ]]
    #Get the result of each game.
    Y = game_stats.iloc[:,-1]

    
    #Translate the command line instructions into their actual team name so that the program can pull the averages.
    dict = {'njd':'New Jersey Devils',
            'nyi': 'New York Islanders',
            'nyr': 'New York Rangers',
            'phi': 'Philadelphia Flyers',
            'pit': 'Pittsburgh Penguins',
            'bos': 'Boston Bruins',
            'buf': 'Buffalo Sabres',
            'mtl': 'Montréal Canadiens',
            'ott': 'Ottawa Senators',
            'tor': 'Toronto Maple Leafs',
            'car': 'Carolina Hurricanes',
            'fla': 'Florida Panthers',
            'tbl': 'Tampa Bay Lightning',
            'wsh': 'Washington Capitals',
            'chi': 'Chicago Blackhawks',
            'det': 'Detroit Red Wings',
            'nsh': 'Nashville Predators',
            'stl': 'St. Louis Blues',
            'cgy': 'Calgary Flames',
            'col': 'Colorado Avalanche',
            'edm': 'Edmonton Oilers',
            'van': 'Vancouver Canucks',
            'ana': 'Anaheim Ducks',
            'dal': 'Dallas Stars',
            'lak': 'Los Angeles Kings',
            'sjs': 'San Jose Sharks',
            'cbj': 'Columbus Blue Jackets',
            'min': 'Minnesota Wild',
            'wpg': 'Winnipeg Jets',
            'ari':'Arizona Coyotes',
            'vgk': 'Vegas Golden Knights'}

    

    
    #Numpy array for running program.
    Y = Y.to_numpy()
    X = X.to_numpy()
    

    

    home_teams = []
    away_teams = []

    #Make a list of all games that want to be predicted.
    teams = sys.argv[1:]
    for j in range(len(teams)):
        if j % 2 == 0:
            away_teams.append(teams[j])
        else:
            home_teams.append(teams[j])

        
    #For each game being predicted, predict 1000 times and make a percentage of won games.
    for k in range(len(away_teams)):

        away = dict[away_teams[k]]
        home = dict[home_teams[k]]

        away = averages.loc[averages['name']== away]
        home = averages.loc[averages['name']== home]

        sub = str(dict[away_teams[k]]) + ' at ' + str(dict[home_teams[k]])
        
        predictor = [away['powerPlayPercentage'].item(),
                away['savePctg'].item(),
                away['shootingPctg'].item(),
                away['shotsPerGame'].item(),
                away['shotsAllowed'].item(),
                away['penaltyKillPercentage'].item(),
                away['powerplayspergame'].item(),
                away['faceOffWinPercentage'].item(),
                home['powerPlayPercentage'].item(),
                home['savePctg'].item(),
                home['shootingPctg'].item(),
                home['shotsPerGame'].item(),
                home['shotsAllowed'].item(),
                home['penaltyKillPercentage'].item(),
                home['powerplayspergame'].item(),
                home['faceOffWinPercentage'].item()]

        predictor = np.array(predictor).reshape(1,-1)

        home_arr = []
        away_arr = []
        
        for i in range(1000):

            #The ML
            train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2)
            clf = MLPClassifier()
            clf.fit(train_X, train_Y)
        
            accuracy = clf.score(test_X, test_Y)
            guess = clf.predict(predictor)

            if guess == 1:
                home_arr.append(accuracy)
            else:
                away_arr.append(accuracy)

        if len(home_arr) > len(away_arr):
            per = len(home_arr) / 10
            msg = str(dict[home_teams[k]]) + ' %' + str(per)
        else:
            per = len(away_arr) / 10
            msg = str(dict[away_teams[k]]) + ' %' + str(per)
        notify(subtitle=sub, message=msg)

#Print the result to the mac notification panel.       
def notify(subtitle, message):
    t = '-title {!r}'.format('NHL1')
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

if __name__ == "__main__":
    main()