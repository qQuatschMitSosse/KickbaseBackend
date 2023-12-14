import json
from kickbase_api.kickbase import Kickbase
from kickbase.constants import NUTZERNAME, PASSWORD

kickbase = Kickbase()
user, leagues = kickbase.login(NUTZERNAME, PASSWORD)

# This is my current league
liga = kickbase.leagues()[2]


class MarketPlayer:
    def __init__(self, id, first_name, last_name, average_points, totalPoints, market_value, market_value_trend, number,
                 position, status, team_id, user_id, username, user_profile_path, price, expiry, lus):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.average_points = average_points
        self.totalPoints = totalPoints
        self.market_value = market_value
        self.market_value_trend = market_value_trend
        self.number = number
        self.position = position
        self.status = status
        self.team_id = team_id
        self.user_id = user_id
        self.username = username
        self.user_profile_path = user_profile_path
        self.price = price
        # self.date = date
        self.expiry = expiry
        self.lus = lus

    def __repr__(self):
        return (
            f"ID: {self.id} {self.first_name} {self.last_name} AVG: {self.average_points} Points: {self.totalPoints} " 
            f"Wert: {self.market_value} Trend:{self.market_value_trend} Number: {self.number} Position: {self.position} " 
            f"Status: {self.status} TeamID: {self.team_id} UserID:{self.user_id} "
            f"Username: {self.username} UserPath {self.user_profile_path} Price: {self.price}"
            f" Expiry: {self.expiry} Lus: {self.lus}")

    def to_dict(self):
        return {'_id': self.id, 'average_points': self.average_points, 'totalPoints': self.totalPoints,
                'market_value': self.market_value, 'market_value_trend': self.market_value_trend, 'number': self.number,
                'position': self.position, 'status': self.status, 'team_id': self.team_id, 'user_id': self.user_id,
                'username': self.username, 'user_profile_path': self.user_profile_path, 'price': self.price,
                'expiry': self.expiry, 'lus': self.lus}


def get_market(league_id):
    market = kickbase.market(league_id).players
    marketfeed = []
    for player in market:
        transferitem = MarketPlayer(player.id, player.first_name, player.last_name, player.average_points,
                                    player.totalPoints, player.market_value, player.market_value_trend, player.number,
                                    player.position, player.status, player.team_id, player.user_id, player.username,
                                    player.user_profile_path, player.price, player.expiry, player.lus)
        json_data = json.dumps(transferitem.to_dict())
        marketfeed.append(json_data)
    return marketfeed
