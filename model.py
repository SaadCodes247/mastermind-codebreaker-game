import random

class GameModel:

    def __init__(self):
        pass

    def set_codemaker_code_to_break(self, codemaker_code_length = 8):
        codemaker_peg_colors = ["r","g", "b", "y", "p", "n", "o", "t"]
        print("The computer codemaker sets the code: ")

        self.random_codemaker_peg_code = random.sample(codemaker_peg_colors, codemaker_code_length)
        hidden_codemaker_code = "# "*len(self.random_codemaker_peg_code)
        print(hidden_codemaker_code, "\n")
        return self.random_codemaker_peg_code

    def play_player_vs_computer(self, codemaker_code_length, allowed_guesses = 2):
        self.codemaker_code_length = codemaker_code_length
        self.allowed_guesses = allowed_guesses

        player_score = 0
        computer_score = 0
        

        code_to_break = self.set_codemaker_code_to_break(codemaker_code_length = 8)
        print(code_to_break)


        for player_turn in range(1, allowed_guesses+1):
            player_guess_response = []
            player_guess = list(input(f"""Player Guess {player_turn}: Please enter a sequence of 8 pegs\n""")) #add input helper 
            
            for peg_index, peg_color in enumerate(player_guess):
                if peg_color == code_to_break[peg_index]:
                    player_guess_response.append("Black")
                elif peg_color in code_to_break and peg_color != code_to_break[peg_index]:
                    player_guess_response.append("White")
            print(f"Response to your guess: {player_guess_response}\n")

            if player_guess_response.count("Black") == self.codemaker_code_length:
                print("Player_1 wins the game!\n")
                player_score += 1
                print(f"Player_1's score is now: {player_score}\n")
                print(f"Computer's score is now: {computer_score}\n")
                break
        else:
            print("The Computer has won the game!\n")
            computer_score += 1
            print(f"Computer's score is now: {computer_score}\n")
            print(f"Player_1's score is now: {player_score}\n")