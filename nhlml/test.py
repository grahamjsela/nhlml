import os
import sys

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function



def main():
    # notify(title    = 'A Real Notification',
    #    subtitle = 'with python',
    #    message  = 'Hello, this is me, notifying you!')

    home_teams = []
    away_teams = []

    teams = sys.argv[1:]
    for i in range(len(teams)):
        if i % 2 == 0:
            away_teams.append(teams[i])
        else:
            home_teams.append(teams[i])

    print(away_teams)
    print(home_teams)

if __name__ == "__main__":
    main()