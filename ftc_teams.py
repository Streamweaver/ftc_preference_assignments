
class Team:

    def __init__(self, num, name):
        self.number = num
        self.name = name

class TeamCollection:

    def __init__(self):
        self._data = {} # Dict of team number and data
        self.unassigned = []

    def add_team(self, team):
        '''
        Adds a team to the collection and to the unassigned list.
        :param team:
        :return:
        '''
        self._data[team.number] = team
        self.unassigned = team
