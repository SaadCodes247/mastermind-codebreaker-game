# test_controller.py
from controller import game_controller

class Starting_Game_Functionality:

    def test_begin_game(capsys, monkeypatch): #capsys for checking print, monkeypatch for mocking input
        monkeypatch.setattr("builtins.input", lambda user_entry: "0") # mocks input
        controller = game_controller()
        controller.begin_game()
        printed_menu = capsys.readouterr()
        assert  " *** Welcome to the Mastermind game! Please select a menu choice *** \n" in printed_menu

        

    
