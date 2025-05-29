# test model.py / the game play

from model import GameModel

class TestGameModel:

    def test_set_codemaker_code_to_break_appears(self, capsys):
        mastermind_computer = GameModel()
        mastermind_computer.set_codemaker_code_to_break()
        result = capsys.readouterr().out
        assert  "The computer codemaker sets the code:" in result
        assert  "# " * 8 in result
        print(result)