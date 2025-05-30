# test model.py / the game play

from src.model import GameModel

class TestGameModel:

    def test_set_codemaker_code_to_break_appears(self, capsys):
        computer_codemaker = GameModel()
        computer_codemaker.set_codemaker_code_to_break()
        result = capsys.readouterr().out
        assert  "The computer codemaker sets the code:" in result
        assert  "# " * 8 in result
        print(result)

    def test_play_player_vs_computer_for_player_win(self, monkeypatch, capsys):
        monkeypatch.setattr("builtins.input", lambda user_entry: "1")
        mastermind_game = GameModel()
        mastermind_game.play_player_vs_computer(lambda self, **kwargs: None)