from kickbase_api.kickbase import Kickbase
from kickbase.constants import NUTZERNAME, PASSWORD
from kickbase.player import get_player_by_id

kickbase = Kickbase()
kickbase.login(NUTZERNAME, PASSWORD)
liga = kickbase.leagues()[2]


# Funktion umd die aktuelle Aufstellung des Teams zu bekommen. Return Werte sind eine Liste der SpielerIDs und das
# Spielsystem
def get_lineup(league_id):
    lineup = kickbase.line_up(league_id).players
    system = kickbase.line_up(league_id).type
    return lineup, system


def get_lineup_players(league_id):
    details = []
    lineup = get_lineup(league_id)[0]
    for player in lineup:
        details.append(get_player_by_id(player))

    return details

