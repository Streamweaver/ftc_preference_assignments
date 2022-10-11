import csv
import random
import re

from ftc_events import parse_events
from ftc_teams import parse_first_team_data, TeamCollection, parse_event_preference_data


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s


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


def load_event_data(filename) -> list:
    events = parse_events(filename)
    print(f"{len(events)} events parsed and loaded.")
    return events


def load_team_data(team_data_filename, team_preferences_filename) -> TeamCollection:
    teams_data = parse_first_team_data(team_data_filename)
    print(f'{len(teams_data)} teams parsed and loaded.')
    teams = TeamCollection()
    teams.add_teams(teams_data)
    parse_event_preference_data(team_preferences_filename, teams)
    return teams





def write_event_picks(event, filename):
    data = [{"Team Number": team.number} for team in event.teams]
    dict_writer(filename, data)


def main():
    teams_list = load_team_data('data/FTC_team_data.csv', 'data/first_pick_event_preferences_test_data.csv')
    event_list = load_event_data('data/FTCEventList.csv')
    waitlist = match_preferences(teams_list, event_list)
    dict_writer("output/waitlist_teams.csv", [{"Team Number": team.number for team in waitlist}])

    for event in event_list:
        write_event_picks(event, f"output/{slugify(event.name)}.csv")


if __name__ == '__main__':
    main()

