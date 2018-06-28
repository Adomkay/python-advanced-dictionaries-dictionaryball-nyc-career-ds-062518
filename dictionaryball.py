import pdb

game_dictionary = {
    'home':{
        'team_name': 'Brooklyn Nets',
        'colors': ['Black', 'White'],
        'players': {'Alan Anderson':{'number': 0,'shoe':16, 'points':22, 'rebounds':12, 'assists':12, 'steals':3, 'blocks':1, 'slam_dunks':1},
            'Reggie Evans':{'number':30,'shoe':14, 'points':12, 'rebounds':12, 'assists':12, 'steals':12, 'blocks':12, 'slam_dunks':7},
            'Brook Lopez':{'number': 11,'shoe':17, 'points':17, 'rebounds':19, 'assists':10, 'steals':3, 'blocks':1, 'slam_dunks':15},
            'Mason Plumlee':{'number':1,'shoe':19, 'points':26, 'rebounds':12, 'assists':6, 'steals':3, 'blocks':8, 'slam_dunks':5},
            'Jason Terry':{'number':31,'shoe':15, 'points':19, 'rebounds':2, 'assists':2, 'steals':4, 'blocks':11, 'slam_dunks':1}
    }
},
'away':{
    'team_name': 'Charlotte Hornets',
    'colors': ['Turquoise', 'Purple'],
    'players': {'Jeff Adrien':{'number': 4,'shoe':18, 'points':10, 'rebounds':1, 'assists':1, 'steals':2, 'blocks':7, 'slam_dunks':2},
        'Bismak Biyombo':{'number':0,'shoe':16, 'points':12, 'rebounds':4, 'assists':7, 'steals':7, 'blocks':15, 'slam_dunks':10},
        'DeSagna Diop':{'number': 2,'shoe':14, 'points':24, 'rebounds':12, 'assists':12, 'steals':4, 'blocks':5, 'slam_dunks':5},
        'Ben Gordon':{'number':8,'shoe':15, 'points':33, 'rebounds':3, 'assists':2, 'steals':1, 'blocks':1, 'slam_dunks':0},
        'Brendan Haywood':{'number':33,'shoe':15, 'points':6, 'rebounds':12, 'assists':12, 'steals':22, 'blocks':5, 'slam_dunks':12}
        }
    }
}

def game_dict():
    return game_dictionary

def merged_players():
    home_players = game_dictionary['home']['players']
    away_players = game_dictionary['away']['players']
    merged_player = home_players.copy()
    merged_player.update(away_players)
    return merged_player

def player_with_highest_stat(stat):
    players = merged_players()
    selected_stat_list = [v[stat] for k, v in players.items()]
    largest_stat = max(selected_stat_list)
    player_largest_stat = [k for k, v in players.items() if v[stat] == largest_stat]
    return player_largest_stat

def num_points_scored(player_name):
    player_dict = merged_players()
    player_points = [v['points'] for k,v in player_dict.items() if k == player_name]
    return player_points[0]

def shoe_size(player_name):
    player_dict = merged_players()
    player_shoes = [v['shoe'] for k,v in player_dict.items() if k == player_name]
    return player_shoes[0]

def team_colors(team_name):
    team_dict = game_dict()
    team_color = [v['colors'] for k,v in team_dict.items() if v['team_name'] == team_name]
    return team_color[0]

def team_names():
    team_dict = game_dict()
    team_list = []
    for location, team_stats in team_dict.items():
        team_list.append(team_stats['team_name'])
    print(team_list)
    return team_list

def player_numbers(team_name):
    team_dict = game_dict()
    home_info = team_dict['home']['players']
    numbers1 = [v['number'] for k, v in home_info.items() if game_dict()['home']['team_name'] == team_name]
    away_info = team_dict['away']['players']
    numbers2 = [v['number'] for k, v in away_info.items() if game_dict()['away']['team_name'] == team_name]
    numbers_list = numbers1 or numbers2
    print(numbers_list)
    return numbers_list

def player_stats(player_name):
    players = merged_players()
    player_statistics = players[player_name]
    print(player_statistics)
    return player_statistics

def big_shoe_rebounds():
    #get player with largest shoe size
    players = merged_players()
    shoe_list = [v['shoe'] for k, v in players.items()]
    largest_shoe = max(shoe_list)
    player_largest_shoe = [k for k, v in players.items() if v['shoe'] == largest_shoe]
    large_shoe_rebound = [v['rebounds'] for k, v in players.items() if v['shoe'] == largest_shoe]
    large_shoe_player_and_rebound = list(zip(player_largest_shoe, large_shoe_rebound))
    print(large_shoe_player_and_rebound)
    return large_shoe_player_and_rebound

def most_points_scored():
    return player_with_highest_stat('points')

def winning_team():
    team_dict = game_dict()
    home_info = team_dict['home']['players']
    home_points_list = [v['points'] for k, v in home_info.items()]
    total_home_points = sum(home_points_list)
    away_info = team_dict['away']['players']
    away_points_list = [v['points'] for k, v in away_info.items()]
    total_away_points = sum(away_points_list)
    if total_home_points > total_away_points:
        print(team_dict['home']['team_name'])
    else:
        print(team_dict['away']['team_name'])

def player_with_longest_name():
    players = merged_players()
    player_name_list = [k for k, v in players.items()]
    name_length = []
    for item in player_name_list:
        length = len(item)
        name_length.append(length)
    for item in player_name_list:
        if len(item) == max(name_length):
            print(item)

game_dict()
