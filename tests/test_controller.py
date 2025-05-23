# test_controller.py
from controller import game_controller

game_controller = game_controller()

def test_begin_game(capsys):
    game_controller.begin_game()
    stdout, stderr = capsys.readouterr()
    assert stdout == """
                    *** Welcome to the Mastermind game! Please select one of the following menu options ***
                    \n 1: One player codebreaker and one computer codemaker\n 
                    \n 2: One player codebreaker and one player codebreaker"

                    """