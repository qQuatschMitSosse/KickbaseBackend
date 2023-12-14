from kickbase_api.kickbase import Kickbase
from kickbase.constants import NUTZERNAME, PASSWORD

kickbase = Kickbase()
kickbase.login(NUTZERNAME, PASSWORD)
liga = kickbase.leagues()[2]


def get_feed(start, league_id):
    league_feed = kickbase.league_feed(start, league_id)
    details = []
    for item in league_feed:
        if item.type == 1:
            details.append('News')
        elif item.type == 2:
            if item.meta.buyer_id is None:
                id = 999
                name = 'Kickbase'
            else:
                id = item.meta.buyer_id
                name = item.meta.buyer_name
            details.append(
                {
                    'BuyerID': id,
                    'BuyerName': name,
                    'Preis': item.meta.sell_price,
                    'Seller ID': item.meta.seller_id,
                    'Seller Name': item.meta.seller_name,
                    'Seller Price': item.meta.sell_price,
                    'SpielerID': item.meta.player_id,
                    'Spieler Vorname': item.meta.player_first_name,
                    'Spieler Nachname': item.meta.player_last_name,
                })
        # Neuer Spieler auf Transfermarkt
        elif item.type == 3:
            details.append(
                {
                    'SpielerID': item.meta.player_id,
                    'Spieler Vorname': item.meta.player_first_name,
                    'Spieler Nachname': item.meta.player_last_name,
                }
            )
        elif item.type == 8:
            details.append('Spieltag Zusammenfassung')
        elif item.type == 9:
            details.append('Status Nachricht')
        elif item.type == 10:
            details.append('Spieler Spieltag Zusammenfassung')
        elif item.type == 11:
            details.append('User Spieltag Zusammenfassung')
        elif item.type == 12:
            if item.meta.seller_id is None:
                id = 999
                name = 'Kickbase'
            else:
                id = item.meta.seller_id
                name = item.meta.seller_name
            details.append(
                {
                    'BuyerID': item.meta.buyer_id,
                    'BuyerName': item.meta.buyer_name,
                    'Preis': item.meta.sell_price,
                    'Seller ID': id,
                    'Seller Name': name,
                    'Seller Price': item.meta.sell_price,
                    'SpielerID': item.meta.player_id,
                    'Spieler Vorname': item.meta.player_first_name,
                    'Spieler Nachname': item.meta.player_last_name,
                })
        elif item.type == 14:
            details.append('Feed Kommentar oder Spieler Profil Status')
        elif item.type == 15:
            details.append('Transfer V2')
        elif item.type == 16:
            details.append('News V2')
        elif item.type == 17:
            details.append('Spieltag Zusammenfassung V2')
        elif item.type == 18:
            details.append('Predicted Lineup')
        elif item.type == 20:
            details.append('Type Empty')
        else:
            details.append('Unknown')
    return details
