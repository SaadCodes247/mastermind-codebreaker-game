# test_controller.py
import pytest

from controller import GameController
from model import GameModel

class TestBeginGameFeatures:

    def test_begin_game_system_exit_option(self, capsys, monkeypatch): #capsys for checking print, monkeypatch for mocking input
        monkeypatch.setattr("builtins.input", lambda user_entry: "0") # mocks input
        controller = GameController()
        with pytest.raises(SystemExit):
            controller.begin_game()
        

    def test_begin_game_player_vs_computer_starts(self, monkeypatch, capsys):
        pass




    
