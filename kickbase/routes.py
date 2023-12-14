from kickbase import app
from kickbase.transfermarkt import liga, get_market
from kickbase.player import get_player_by_id
from kickbase.myteam import get_lineup_players
from kickbase.feed import liga, get_feed


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/market')
def market():
    return get_market(liga)


@app.route('/player/<player_id>')
def players(player_id):
    return get_player_by_id(player_id)


@app.route('/myteam')
def team():
    return get_lineup_players(liga)


@app.route('/feed')
def feed():
    return get_feed(0, liga)
