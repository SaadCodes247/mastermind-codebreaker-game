import random

class game_model:

    def __init__(self):
        pass

    def set_codemaker_code_to_break(self, codemaker_code_length = 8):
        codemaker_peg_colors = ["r","g", "b", "y", "p", "n", "o"]
        print("The computer codemaker sets the code: ")

        self.random_codemaker_peg_code = [random.choice(codemaker_peg_colors) for peg in range(codemaker_code_length+1)]
        hidden_codemaker_code = "#"*len(self.random_codemaker_peg_code)
        #print(self.random_codemaker_peg_code)
        print(hidden_codemaker_code, "\n")

    def play_player_vs_computer(self, codemaker_code_length, allowed_guesses):
        self.codemaker_code_length = codemaker_code_length
        self.allowed_guesses = allowed_guesses

        self.set_codemaker_code_to_break()

        

    

        
        
        