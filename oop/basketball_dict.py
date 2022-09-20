players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

class Player:
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")
    
    @classmethod
    def get_team(cls, team_list):
        player_list = []
        for player in team_list:
            player_list.append(Player(player))
        return player_list



new_team = []

for player in players:
    new_team.append(Player(player))


# for player in new_team:
#     player.print_info()

ninja_bonus = Player.get_team(players)

for player in ninja_bonus:
    player.print_info()