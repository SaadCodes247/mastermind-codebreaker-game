# test_controller.py
import pytest

from controller import GameController
from model import GameModel

class TestBeginGameFeatures:

    def test_begin_game_system_exit_option(self, capsys, monkeypatch): #capsys for checking print, monkeypatch for mocking input
        monkeypatch.setattr("builtins.input", lambda user_entry: "0") # mocks input
        mastermind_game = GameController()
        with pytest.raises(SystemExit):
            mastermind_game.begin_game()
        

    def test_begin_game_player_vs_computer_starts(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda user_entry: "1") # mocks input
        monkeypatch.setattr("model.GameModel.play_player_vs_computer", lambda self, **kwargs: None) # lambda self means don't go further, kwargs means accept additional arguments 
        mastermind_game = GameController()
        mastermind_game.begin_game()
        printed_menu = capsys.readouterr()
        assert  " *** Welcome to the Mastermind game! Please select a menu choice *** \n" in printed_menu




    
