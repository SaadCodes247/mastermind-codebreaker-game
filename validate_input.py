# validate player's input

class ValidatePlayerInput:

    def __init__(self, player_input):
        self.player_input = player_input.strip().lower()
        
    def validate_input(self, allowed_chars = ["r","g", "b", "y", "p", "n", "o", "t"], required_length = 8):
        if(len(self.player_input)) != required_length:
            print("Please enter a string of exactly 8 characters only")
            return False

        elif any(char not in allowed_chars for char in self.player_input):
             print("Please enter a letter corresponding to one of the 8 peg colours. You can only enter each letter once")
             return False

        return True