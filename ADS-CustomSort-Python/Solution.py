from functools import cmp_to_key

class Sort:
    def __init__(self, team_name, wins, losses, draws, no_result, points):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.no_result = no_result
        self.points = points

    def __str__(self):
        return f"{self.team_name}: Points={self.points}, Wins={self.wins}, Losses={self.losses}, Draws={self.draws}, NoResult={self.no_result}"

        

def compare(s1, s2):
    if s1.points < s2.points:
        return 1
    elif s1.points > s2.points:
        return -1
    else:
        if s1.wins < s2.wins:
            return 1
        elif s1.wins > s2.wins:
            return -1
        else:
            if s1.losses > s2.losses:
                return 1
            elif s1.losses < s2.losses:
                return -1
            else:
                if s1.draws < s2.draws:
                    return 1
                elif s1.draws > s2.draws:
                    return -1
                else:
                    if s1.no_result > s2.no_result:
                        return 1
                    elif s1.no_result < s2.no_result:
                        return -1
                    else:
                        if s1.team_name > s2.team_name:
                            return 1
                        elif s1.team_name < s2.team_name:
                            return -1
    return 0
            


team_data = []
while True:
    try:
        s = input()
        s=s.split(",")

        if s == []:
            break

        data = Sort(s[0], int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5]))
        team_data.append(data)

    except:
        break

team_data.sort(key=cmp_to_key(compare))
print("Sorted Leaderboard:")
for team in team_data:
    print(team)
