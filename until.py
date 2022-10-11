import csv, random, re
from ftc_events import parse_events
from ftc_teams import parse_first_team_data, parse_event_preference_data, TeamCollection

def load_event_data(filename) -> list:
    events = parse_events(filename)
    return events


def load_team_data(filename) -> list:
    teams = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            teams.append(row)
    return teams


def generate_preference_data(team_list: list, event_list: list) -> list:
    preference_list = []
    for team in team_list:
        if team["Payment Ready Status"] == "Secured":
            event_picks = random.sample(event_list, 3)
            data = {
                "Timestamp": "10/7/2022 13:30:02",
                "Email Address": "sturnbull@firstchesapeake.org",
                "Team Number": team["Team Number"],
                "Team Name": team["Team Nickname"],
                "Most Preferred Event": event_picks[0],
                "Second Most Preferred Event": event_picks[1],
                "Third Most Preferred Event": event_picks[2]
            }
            preference_list.append(data)
    return preference_list


def dict_writer(filename, data) -> None:
    """
    Writes a csv file from a list of dictionaries.
    :param filename:
    :param data:
    :return:
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    team_list = load_team_data('data/FTC_team_data.csv')
    event_list = load_event_data('data/FTCEventList.csv')
    preference_list_data = generate_preference_data(team_list, event_list)
    dict_writer('data/first_pick_event_preferences_test_data.csv', preference_list_data)



