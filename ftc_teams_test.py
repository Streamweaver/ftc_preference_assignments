import random
import string
import unittest

from ftc_teams import Team, TeamCollection, TeamException


class TestTeam(unittest.TestCase):

    def setUp(self):
        self.Team = Team("234555", "Test Name")

    def test_team_number(self):
        self.assertTrue(type(self.Team.number) is int, "Team number is not an int")


class TeamGenerator:

    def __init__(self):
        self.teams = []

    def get_teams(self, num):
        teams = []
        for i in range(len(self.teams), len(self.teams) + num):
            t_num = i + 1
            teams.append(
                Team(t_num, ''.join(random.choices(string.ascii_lowercase, k=5)))
            )
            self.teams.append(teams)
        return teams


class TestTeamCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.tc = TeamCollection()
        self.tg = TeamGenerator()

    def test_add_team(self):
        # It should add a single unsecured team
        teams = self.tg.get_teams(2)
        self.tc.add_team(teams[0])
        self.assertEqual(1, len(self.tc._data))
        self.assertEqual(0, len(self.tc.unassigned))

        # It should add a team to the unassigned list.
        teams[1].secured = True
        self.tc.add_team(teams[1])
        self.assertEqual(1, len(self.tc.unassigned))

        # It should throw an error.
        self.assertRaises(TeamException, self.tc.add_team, teams[0])

    def test_add_teams(self):
        teams = self.tg.get_teams(10)
        self.tc.add_teams(teams)
        self.assertEqual(len(self.tg.teams), len(self.tc._data))

    def test_add_event_preferences(self):
        teams = self.tg.get_teams(2)
        teams[1].secured = True
        self.tc.add_teams(teams)

        # It should throw an exception if team doesn't exist.
        self.assertRaises(TeamException, self.tc.add_event_preferences, 10, '', '', '')

        # It should raise exception if try to add an unsecured team.
        self.assertRaises(TeamException, self.tc.add_event_preferences, 1, '', '', '')

        # It should add a team preference for a secured team that exists
        self.tc.add_event_preferences(2, "first", "second", "third")
        self.assertEqual(3, len(teams[1].event_preferences))
