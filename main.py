from ftc_teams import parse_first_team_data, Team, TeamException, TeamCollection, parse_event_preference_data

def load_team_data(team_data_filename, team_preferences_filename):
    teams_data = parse_first_team_data(team_data_filename)
    print(f'{len(teams_data)} teams parsed and loaded.')
    teams = TeamCollection()
    teams.add_teams(teams_data)
    parse_event_preference_data(team_preferences_filename, teams)


if __name__ == '__main__':
    load_team_data('data/FTC_team_data.csv', 'data/first_pick_event_preferences.csv')
