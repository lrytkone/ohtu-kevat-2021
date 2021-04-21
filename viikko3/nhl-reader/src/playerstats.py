
class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        self.nationality = nationality
        nat_list = []
        for player in self.players:
            if player.nationality == 'FIN':
                nat_list.append(player)

        nat_list.sort(key=lambda x: x.ga, reverse=True)
        return nat_list

