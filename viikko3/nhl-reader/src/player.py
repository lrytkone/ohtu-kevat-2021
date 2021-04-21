class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.ga = goals + assists

    def __str__(self):
        return f"{self.name} {self.nationality} {self.team} {str(self.goals)} + {str(self.assists)} = {str(self.ga)}"
