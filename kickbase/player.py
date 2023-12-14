from kickbase import collection


# Funktion sucht einen Spieler anhand der ID in der Datenbank(MongoDB) und gibt die Daten zurück
def get_player_by_id(player_id):
    player = collection.find_one({'_id': str(player_id)})
    return player
