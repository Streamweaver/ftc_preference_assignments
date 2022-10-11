import csv, random
from ftc_teams import Team, TeamCollection


class EventException(Exception):
    pass


class FTCEvent:

    def __init__(self, name, postal_code, event_date, event_location, capacity):
        self.capacity = capacity
        self.event_location = event_location
        self.event_date = event_date
        self.postal_code = postal_code
        self.name = name
        self.teams = []

    def __str__(self):
        return f"{self.name}"

    def assign_team(self, team) -> None:
        if not team.secured:
            raise EventException(f"Cannot assign unsecured team {team.number} to an event!")
        if self.is_team_assigned(team.number):
            raise EventException(f"Team {team.number} is already assigned and cannot be assigned again!")
        if len(self.teams) >= self.capacity:
            raise EventException(f"Event full, cannot add team {team.number}")
        self.teams.append(team)

    def capacity_left(self) -> int:
        """
        Returns an int of the number of unassigned slots at the event.

        :return: Int of remaining event capacity
        """
        return self.capacity - len(self.teams)

    def is_team_assigned(self, team_number) -> bool:
        """
        Checks if a team number is assigned to the event.

        :param team_number: string of team number
        :return: boolean if the team number is assigned
        """
        return team_number in [t.number for t in self.teams]


class EventAssigner:

    def __init__(self, events: list[FTCEvent], teams: TeamCollection):
        self.events = events
        self.teams = teams
        self.waitlist = []

    def _filter_team_by_selection(self, event: FTCEvent, index: int) -> list[Team]:
        """
        Returns a list of teams that have selected the event as a preference,
        :param event:
        :return:
        """
        filtered_teams = []
        for team in self.teams.unassigned:
            if team.event_preferences[index] == event.name:
                filtered_teams.append(team)
        return filtered_teams

    def match_preferences(self, events) -> None:
        """
        Matches teams based on their preference selections and returns any teams that could not be assigned.

        :param events:
        :return:
        """
        for i in range(0, 3):
            for event in events:
                filtered_teams = self._filter_team_by_selection(event, i)
                if len(filtered_teams) > event.capacity_left():
                    num_select = event.capacity_left
                else:
                    num_select = len(filtered_teams)
                for team in random.sample(filtered_teams, num_select):
                    event.assign_team(team)
                    self.teams.unassigned.remove(team)
        self.waitlist = self.teams.unassigned
        self.teams.unassigned = []


def parse_events(filename: str) -> list[FTCEvent]:
    events = []
    with open(filename, newline='') as csvfile:
        # Name,Date,Location,Street,City,State,Event Postal Code
        reader = csv.DictReader(csvfile)
        for row in reader:
            event = FTCEvent(
                row['Name'],
                row["Postal Code"],
                row['Date'],
                f"{row['Location']} in {row['City']}, {row['State']}",
                int(row['Capacity'])
            )
            events.append(event)
    return events
