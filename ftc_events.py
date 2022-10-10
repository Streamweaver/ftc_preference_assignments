import csv


class FTCEvent:

    def __init__(self, name, postal_code, event_date, event_location, capacity):
        self.capacity = capacity
        self.event_location = event_location
        self.event_date = event_date
        self.postal_code = postal_code
        self.name = name
        self.teams = []

    def capacity_left(self):
        """
        Returns an int of the number of unassigned slots at the event.

        :return: Int of remaining event capacity
        """
        return self.capacity - len(self.teams)

    def team_assigned(self, team_number):
        """
        Checks if a team number is assigned to the event.

        :param team_number: string of team number
        :return: boolean if the team number is assigned
        """
        return team_number in [t.number for t in self.teams]


def parse_events(filename):
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
                row['Capacity']
            )
            events.append(event)
    return events
