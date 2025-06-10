About:
This is a popular board game called Mastermind which I am currently creating In python. It offers both player and computer game play.

Example Game:
Try an existing online version of the game (linked below) to get a feel of how the game is played! 
https://www.webgamesonline.com/codebreaker/

Mastermind - Rules of the game.
2 Players: code_maker and code_breaker:
1. The computer or player generates a color sequence which is hidden to the opposite player, known as the code_to_break, and takes the role of the code_maker.
2. The objective for the opposite player is to correctly guess the exact positions and colors in the initial code_to_break sequence, taking the role of the code_breaker.

Gameplay
1. If the code_breaker guesses the correct color and position in the code_to_break,'black' is returned and the code_breaker scores 1 point.
2. If the code_breaker guesses the correct color but in the wrong position in the code_to_break,'white' is returned and no points are given
3. If the code_breaker cannot guess either a correct color or position in the sequence, 'blank' is returned and 1 point is taken away

The Challenge is for the code_breaker to guess the code_to_break with a limited number of guesses and by only observing the responses returned for each guess!

How does one become the Mastermind?
1. If the code_breaker correctly guesses the code_to_break within the allowed guesses they are truly the Mastermind!
2. However, if the code_breaker fails to guess the code_to_break, then the code_maker truly is the Mastermind!
