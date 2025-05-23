
class game_controller:

    def __init__(self):
        pass
        

    def begin_game(self):

        print(
            """ *** Welcome to the Mastermind game! Please select a menu choice *** """
            )
        menu_choice_option = input("Menu Choice: ")
        match menu_choice_option:
            case 0:
                SystemExit
            case 1:
                player_vs_computer()
            case 2:
                player_vs_player()

        
    