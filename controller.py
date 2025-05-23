from model import game_model

class game_controller:

    def __init__(self):
        pass
        
    def begin_game(self):

        player_vs_computer = game_model()

        print(
            """ *** Welcome to the Mastermind game! Please select a menu choice *** """
            )
        menu_choice_option = int(input("Menu Choice: "))
        match menu_choice_option:
            case 0:
                SystemExit
            case 1:
                player_vs_computer.play_player_vs_computer(codemaker_code_length = 8, allowed_guesses = 2)
                
    def computer_codemaker():
        pass

        
    