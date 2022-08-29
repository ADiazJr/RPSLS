from player import Player
from ai_computer import AI_Computer
from human import Human

class Game():
    def __init__(self):
        self.player = Human('P1')
        self.rounds = 0
        self.players = ''
        self.player_2= Human('P2')
        self.computer = AI_Computer('computer')
        self.current_round = 1
        self.player_points = 0
        self.player_2_points = 0
    
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
        #while self.current_round < self.rounds:
        self.choose_gesture(result)
        self.compare_gesture()
        print(self.player_2_points)
        print(self.player_points)


    def choose_rounds(self):
        self.rounds = input('Enter the number of rounds, minimum three rounds: ')
        
    def single_or_multiplayer(self):
        self.players = input('Choose to play with human or computer: ')
        if self.players == 'computer':
            return self.computer
        if self.players == 'human':
            return self.player_2
    def choose_gesture(self, result):
        self.player.select()
        if result == self.computer:
            self.computer.random_selection()
        elif result == self.player_2:
            self.player_2.select()

    def compare_gesture(self, result):
        if result == self.player_2:
            if self.player.gesture == self.player_2.gesture:
                print('tie')
                self.current_round -= 1
                if self.player.gesture == "Rock" and self.player_2.gesture == "Scissors":
                    self.player_points += 1
            # Rock crushes Scissors
                elif self.player.gesture == "Scissors" and self.player_2.gesture == "Paper":
                    self.player_points += 1
            # Scissors cuts Paper
                elif self.player.gesture == "Paper" and self.player_2.gesture == "Rock":
                    self.player_points += 1
            # Paper covers Rock
                elif self.player.gesture == "Rock" and self.player_2.gesture == "Lizard":
                    self.player_points += 1
            # Rock crushes Lizard
                elif self.player.gesture == "Lizard" and self.player_2.gesture == "Spock":
                    self.player_points += 1             
            # Lizard poisons Spock
                elif self.player.gesture == "Spock" and self.player_2.gesture == "Scissors":
                    self.player_points += 1
            # Spock smashes Scissors
                elif self.player.gesture == "Scissors" and self.player_2.gesture == "Lizard":
                    self.player_points += 1
            # Scissors decapitates Lizard
                elif self.player.gesture == "Lizard" and self.player_2.gesture == "Paper":
                    self.player_points += 1
            # Lizard eats Paper
                elif self.player.gesture == "Paper" and self.player_2.gesture == "Spock":
                    self.player_points += 1
            # Paper disproves Spock 
                elif self.player.gesture == "Spock" and self.player_2.gesture == "Rock":
                    self.player_points += 1
            # Spock vaporizes Rock
                elif self.player_2.gesture == "Rock" and self.player.gesture == "Scissors":
                    self.player_2_points += 1
            # Rock crushes Scissors
                elif self.player_2.gesture == "Scissors" and self.player.gesture == "Paper":
                    self.player_2_points += 1
            # Scissors cuts Paper
                elif self.player_2.gesture == "Paper" and self.player.gesture == "Rock":
                    self.player_2_points += 1
            # Paper covers Rock
                elif self.player_2.gesture == "Rock" and self.player.gesture == "Lizard":
                    self.player_2_points += 1
            # Rock crushes Lizard
                elif self.player_2.gesture == "Lizard" and self.player.gesture == "Spock":
                    self.player_2_points += 1             
            # Lizard poisons Spock
                elif self.player_2.gesture == "Spock" and self.player.gesture == "Scissors":
                    self.player_2_points += 1
            # Spock smashes Scissors
                elif self.player_2.gesture == "Scissors" and self.player.gesture == "Lizard":
                    self.player_2_points += 1
            # Scissors decapitates Lizard
                elif self.player_2.gesture == "Lizard" and self.player.gesture == "Paper":
                    self.player_2_points += 1
            # Lizard eats Paper
                elif self.player_2.gesture == "Paper" and self.player.gesture == "Spock":
                    self.player_2_points += 1
            # Paper disproves Spock 
                elif self.player_2.gesture == "Spock" and self.player.gesture == "Rock":
                    self.player_2_points += 1
            # Spock vaporizes Rock
        elif result == self.computer:
            if self.player.gesture == self.computer.gesture:
                print('tie')
                self.current_round -= 1
            if self.player.gesture == "Rock" and self.computer.gesture == "Scissors":
                self.player_points += 1
        # Rock crushes Scissors
            elif self.player.gesture == "Scissors" and self.computer.gesture == "Paper":
                self.player_points += 1
        # Scissors cuts Paper
            elif self.player.gesture == "Paper" and self.computer.gesture == "Rock":
                self.player_points += 1
        # Paper covers Rock
            elif self.player.gesture == "Rock" and self.computer.gesture == "Lizard":
                self.player_points += 1
        # Rock crushes Lizard
            elif self.player.gesture == "Lizard" and self.computer.gesture == "Spock":
                self.player_points += 1             
        # Lizard poisons Spock
            elif self.player.gesture == "Spock" and self.computer.gesture == "Scissors":
                self.player_points += 1
        # Spock smashes Scissors
            elif self.player.gesture == "Scissors" and self.computer.gesture == "Lizard":
                self.player_points += 1
        # Scissors decapitates Lizard
            elif self.player.gesture == "Lizard" and self.computer.gesture == "Paper":
                self.player_points += 1
        # Lizard eats Paper
            elif self.player.gesture == "Paper" and self.computer.gesture == "Spock":
                self.player_points += 1
        # Paper disproves Spock 
            elif self.player.gesture == "Spock" and self.computer.gesture == "Rock":
                self.player_points += 1
        # Spock vaporizes Rock
            elif self.computer.gesture == "Rock" and self.player.gesture == "Scissors":
                self.player_2_points += 1
        # Rock crushes Scissors
            elif self.computer.gesture == "Scissors" and self.player.gesture == "Paper":
                self.player_2_points += 1
        # Scissors cuts Paper
            elif self.computer.gesture == "Paper" and self.player.gesture == "Rock":
                self.player_2_points += 1
        # Paper covers Rock
            elif self.computer.gesture == "Rock" and self.player.gesture == "Lizard":
                self.player_2_points += 1
        # Rock crushes Lizard
            elif self.computer.gesture == "Lizard" and self.player.gesture == "Spock":
                self.player_2_points += 1             
        # Lizard poisons Spock
            elif self.computer.gesture == "Spock" and self.player.gesture == "Scissors":
                self.player_2_points += 1
        # Spock smashes Scissors
            elif self.computer.gesture == "Scissors" and self.player.gesture == "Lizard":
                self.player_2_points += 1
        # Scissors decapitates Lizard
            elif self.computer.gesture == "Lizard" and self.player.gesture == "Paper":
                self.player_2_points += 1
        # Lizard eats Paper
            elif self.computer.gesture == "Paper" and self.player.gesture == "Spock":
                self.player_2_points += 1
        # Paper disproves Spock 
            elif self.computer.gesture == "Spock" and self.player.gesture == "Rock":
                self.player_2_points += 1
        # Spock vaporizes Rock

    def determine_winner_round(self):
        pass

    def determine_game_won(self):
        pass

    def display_winner(self):
        pass