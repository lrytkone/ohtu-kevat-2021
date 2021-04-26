from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
from querybuilder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(5, "assists"),
    #    PlaysIn("PHI")
    #)

    #matcher = And(
    #    Not(HasAtLeast(1, "goals")),
    #    PlaysIn("NYR")
    #)

    #matcher = And(
    #    HasFewerThan(1, "goals"),
    #    PlaysIn("NYR")
    #)

    #matcher = Or(
    #    HasAtLeast(40, "goals"),
    #    HasAtLeast(60, "assists")
    #)

    query = QueryBuilder()
    matcher = (
      query
        .playsIn("NYR")
        .hasAtLeast(5, "goals")
        .hasFewerThan(10, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)



if __name__ == "__main__":
    main()
