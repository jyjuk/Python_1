class SoccerPlayer:

    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, value=1):
        self.goals += value

    def make_assist(self, value):
        self.assists += value

    def statistics(self):
        print(f'{self.surname} {self.name} - голи {self.goals}, передачі {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()
