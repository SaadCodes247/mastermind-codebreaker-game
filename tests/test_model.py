test model.py

from controller import GameController
from model import GameModel

class TestGameModel:

    def test_set_codemaker_code_to_break(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda user_entry: "1")
        model = game_model()
        controller = game_controller()
        controller.begin_game()
        printed_menu = capsys.readouterr()
        assert  " *** Welcome to the Mastermind game! Please select a menu choice *** \n" in printed_menu


    def test_play_player_vs_computer():
        pass