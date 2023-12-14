import json
from kickbase_api.kickbase import Kickbase
from kickbase.constants import NUTZERNAME, PASSWORD

kickbase = Kickbase()
user, leagues = kickbase.login(NUTZERNAME, PASSWORD)

# This is my current league
liga = kickbase.leagues()[2]

def get_transfermarket(league_id):
    market = kickbase.market(league_id).players
    marketfeed = []
    for player in market:
        marketfeed.append(
        {
            "Spieler ID": player.id,
            "Vorname": player.first_name,
            "Nachname": player.last_name,
            "Average Points": player.average_points,
            "Total Points": player.totalPoints,
            "Marktwert": player.market_value,
            "Marktwert Trend": player.market_value_trend,
            "Position": player.position,
            "Status": player.status,
            "TeamID": player.team_id,
            "UserID": player.user_id,
            "Username": player.username,
            "User Path": player.user_profile_path,
            "Preis": player.price,
            "Abgelaufen": player.expiry,
        }
        )
    return marketfeed
