import random

class game_model:

    def __init__(self):
        pass

    def set_codemaker_code_to_break(self, codemaker_code_length = 8):
        codemaker_peg_colors = ["r","g", "b", "y", "p", "n", "o"]
        print("The computer codemaker sets the code: ")

        self.random_codemaker_peg_code = [random.choice(codemaker_peg_colors) for peg in range(1, codemaker_code_length+1)]
        hidden_codemaker_code = "# "*len(self.random_codemaker_peg_code)
        print(self.random_codemaker_peg_code)
        print(hidden_codemaker_code, "\n")
        return self.random_codemaker_peg_code

    def play_player_vs_computer(self, codemaker_code_length, allowed_guesses = 1):
        self.codemaker_code_length = codemaker_code_length
        self.allowed_guesses = allowed_guesses

        code_to_break = self.set_codemaker_code_to_break(codemaker_code_length = 8)
        print(code_to_break)

        for player_turn in range(1, allowed_guesses+1):
            player_guess_response = []
            player_guess = list(input(f"Player Guess {player_turn}: Please enter a sequence of 8 pegs \n")) #add input helper 
            for peg_index, peg_color in enumerate(player_guess):
                if peg_color == code_to_break[peg_index]:
                    player_guess_response.append("Black")
                elif peg_color in code_to_break and peg_color != code_to_break[peg_index]:
                    player_guess_response.append("White")
            print(f"Response to your guess: {player_guess_response}")

            



        

    

        
        
        