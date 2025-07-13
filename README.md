# Welcome to the Mastermind Codebreaker Game!
## This is a popular board game known as Mastermind, created for the terminal using Python. 

### **Main Objective:** Guess a sequence of 8 hidden colors by relying solely on memory and strategy!

### Game Rules:
> - There are 2 Players: code_maker (1) and code_breaker (2).
> 1. The computer or player takes the role of 'code_maker' and generates a color sequence which is hidden from the opposite player
>    and known as the code_to_break.
> 2. The objective for the opposite player, the 'code breaker', is to correctly guess the exact positions
>    and colors in the code_to_break set by the code_maker
> 3. The code_breaker can make one of the guesses below in a series of 8 turns:
>     -  a correct colour and position of the code to break, 'black' is returned
>     -  a correct colour but incorrect position in the code_to_break, 'white' is returned
>     -  and if neither a correct colour nor position, then a blank is returned

## Example for Understanding Gameplay:
> 1. The code_maker sets the code_to_break as [red, green, blue, yellow], and the code_breaker sees [X, X, X, X]
>    
> 2. Turn 1 of 3: The code_breaker guesses [red, blue, green, purple] 
>
>    - The Response from the terminal is [black, white, white, blank], and the code_breaker still only sees [X, X, X, X]
>
> 3. Turn 2 of 3: The code_breaker tries a different guess like [red, green, blue, yellow]
>
>    - The Response from the terminal is [black, black, black, black]

## Who is The True Mastermind Above?

**Winner!** - The code_breaker is truly the Mastermind for guessing the code_to_break above within the number of guesses!

**Otherwise...** - the code_maker would have been the Mastermind. Not this time, though!

**Oh, and BTW** - This gets much harder with 8 colors to guess in 10 guesses!

## Third-Party Example Game:
Try a third-party existing online version of the game to get a better feel for it!
https://www.webgamesonline.com/codebreaker/
