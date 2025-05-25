# test_controller.py
import pytest
from controller import game_controller

class TestBeginGameFeatures:

    def test_begin_game_system_exit_option(self, capsys, monkeypatch): #capsys for checking print, monkeypatch for mocking input
        monkeypatch.setattr("builtins.input", lambda user_entry: "0") # mocks input
        controller = game_controller()
        with pytest.raises(SystemExit):
            controller.begin_game()
        

        # def test_begin_game_menu_option_1(self, monkeypatch):
            # monkeypatch.setattr("("builtins.input", lambda user_entry: "0")")
            # controller = game_controller
            # controller.begin_game()
            # printed_menu = capsys.readouterr()
            # assert  " *** Welcome to the Mastermind game! Please select a menu choice *** \n" in printed_menu




    
