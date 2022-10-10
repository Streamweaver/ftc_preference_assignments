import unittest
from ftc_events import FTCEvent, EventException
from ftc_teams import Team


class FTCEventTest(unittest.TestCase):

    def setUp(self) -> None:
        self.team = Team(23954, "test team 1")
        self.team.secured = True
        self.capacity = 36
        self.event = FTCEvent(
            "Test Event 1",
            "23059",
            "10/20/2022",
            "Glen Allen, VA",
            self.capacity
        )

    def test_assign_team(self):
        self.assertEqual(0, len(self.event.teams))

        self.team.secured = False
        self.assertRaises(EventException, self.event.assign_team, self.team)

        self.team.secured = True
        self.event.assign_team(self.team)
        self.assertEqual(1, len(self.event.teams))

        self.assertRaises(EventException, self.event.assign_team, self.team)

    def test_assign_over_capacity(self):
        self.event.capacity = 0
        self.assertRaises(EventException, self.event.assign_team, self.team)

    def test_capacity_left(self) -> None:
        self.assertEqual(self.capacity, self.event.capacity_left())
        self.event.assign_team(self.team)
        self.assertEqual(self.capacity - 1, self.event.capacity_left())

    def test_is_team_assigned(self) -> None:
        self.assertFalse(self.event.is_team_assigned(self.team.number))
        self.event.assign_team(self.team)
        self.assertTrue(self.event.is_team_assigned(self.team.number))


if __name__ == '__main__':
    unittest.main()
