
class game_controller:

    def __init__(self):
        pass
        

    def begin_game():
        game_finished = False
        menu_choice_option = 0

        print(
            """

            *** Welcome to the Mastermind game! Please select one of the following menu options ***
            \n 1: One player codebreaker and one computer codemaker\n 
            \n 2: One player codebreaker and one player codebreaker
            
            """
            )
        menu_choice_option = input("Menu Choice: ")
        match menu_choice_option:
            case 0:
                SystemExit
            case 1:
                player_vs_computer()
                print(" ")
            case 2:
                player_vs_player()

        
    