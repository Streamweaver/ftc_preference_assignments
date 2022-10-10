import csv


class TeamException(Exception):
    pass


class Team:

    def __init__(self, num, name):
        self.number = int(num)
        self.name = name
        self.secured = False
        self.first_coach_email = None
        self.second_coach_email = None
        self.postal_code = None
        self.event_preferences = []


class TeamCollection:

    def __init__(self):
        self._data = {}  # Dict of team number and data
        self.unassigned = []

    def add_team(self, team: Team):
        """
        Adds a team to the collection and to the unassigned list.
        :param team:
        :return:
        """
        if team.number in self._data:
            raise TeamException(f"Team number {team.number} already exists! Cannot add again.")
        self._data[team.number] = team
        if team.secured:
            self.unassigned.append(team)

    def add_teams(self, team_list: list):
        """
        Convienence method to add a bunch of teams.

        :param team_list: list of Team Objects
        :return:
        """
        for team in team_list:
            self.add_team(team)

    def add_event_preferences(self, team_number: int, first: str, second: str, third: str):
        if team_number not in self._data:
            raise TeamException(f"Cannot add preference for team {team_number}. They do not exist!")
        if not self._data[team_number].secured:
            raise TeamException(f"Team {team_number} is not secured and cannot be assigned preferences!")
        self._data[team_number].event_preferences = [first, second, third]


def parse_first_team_data(filename: str) -> list:
    """
    Parses the FIRST Inspires team data file and returns a list of serialized TEAM objects.

    :param filename: string of the FI datafile for teams
    :return: list of Team objects.
    """
    teams = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            team = Team(row['Team Number'], row['Team Nickname'])
            team.secured = row['Payment Ready Status'] == 'Secured'
            team.postal_code = row['Team Postal Code']
            team.first_coach_email = row['LC1 Email']
            team.second_coach_email = row['LC2 Email']
            teams.append(team)
    return teams


def parse_event_preference_data(filename: str, teams: TeamCollection):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            teams.add_event_preferences(
                int(row['Team Number']),
                row['Most Preferred Event'],
                row['Second Most Preferred Event'],
                row['Third Most Preferred Event']
            )
