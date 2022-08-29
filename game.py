from player import Player
from ai_computer import AI_Computer
from human import Human

class Game():
    def __init__(self):
        self.player = Human('P1')
        self.rounds = 0
        self.players = ''
        self.ai_computer = AI_Computer('Computer')
        self.player2 = Human('P2')
        self.current_round = 1
    
    def display_welcome(self):
        print('''Welcome to RPSLS. This are the game rules:
                    Rock crushes Scissors
                    Scissors cuts Paper
                    Paper covers Rock
                    Rock crushes Lizard
                    Lizard poisons Spock
                    Spock smashes Scissors
                    Scissors decapitates Lizard
                    Lizard eats Paper
                    Paper disproves Spock
                    Spock vaporizes Rock''')

    def run_game(self):
        self.display_welcome()
        result = self.single_or_multiplayer()
        print(result)
        #while self.current_round < self.rounds:
            

    def choose_rounds(self):
        self.rounds = input('Enter the number of rounds, minimum three rounds: ')
        
    def single_or_multiplayer(self):
        self.players = input('Choose to play with human or computer: ')
        if self.players == 'computer':
            return self.ai_computer
        if self.players == 'human':
            return self.player2

    def choose_gesture(self):
        pass

    def compare_gesture(self):
        pass

    def determine_winner_round(self):
        pass

    def determine_game_won(self):
        pass

    def display_winner(self):
        pass