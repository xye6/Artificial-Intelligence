Read me

1.Basic introduction:

	1) Basic TTT and Advance TTT are entirely completed by myself and work is done with python3.

	2) Super TTT is completed with my teammate(Yanhao Ding and Wei Zhou), work is done with Java, because all of us use different programming language and Yanhao Ding is the main person who complete this part of Super TTT.In this part, my work is that test program many time to find bugs and debug and use different evolution function to optimize code.


2.Basic TTT (using python3):

	1) Run it in terminal (python BasicTTT.py)

	2) First it will ask you to choose 'X' or 'O' and the game will really begin after you type 'X' or 'O'

	3) When it is player's turn to move, it will show the board and the words to prompt to type the number[1-9](your preference position) and program will check the number inputted and input will be invalid if the number is not between 1 and 9.

	4) When it is computer's turn to move, it will show the result of moving and the time it costs in this movement and the number about position.

	5) When the game is over, program will show the result (who win this game) and start a new game if you want to try again.


3.Advanced TTT (using python3):

	1) Run it in terminal (python AdvancedTTT.py)
	
	2) First it will ask you to choose 'X' or 'O' and the game will really begin after you have make decision to type 'X' or 'O'

	3) When it is player's turn to move, it will show the board and the words to prompt player to type two numbers (separated with space), for example: 1 6.
	And each number should be between 1 and 9, if not, computer will check whether this inputs is applicable. Then it shows the board after moving.

	4) When it is computer's turn to move, it will show the result of moving and the time it costs in this movement and the number about position.

	5) When the game is over, program will show the result (who win this game) and start a new game if you want to try again.

4. Super TTT (use java):

	1) Run it in terminal (java SuperTTT)

	2) First it will ask you to choose 'X' or 'O' and the game will really begin after you type 'X' or 'O'.

	3) When it is AI's turn to move first, it will show the result of moving and the number about position.

	4) When it is player's turn to move, it will show the board and the words to prompt player to type one numbers to choose the position you want to play, and player have no choice to choose grid which is depended on AI. (In this example, AI play first). If player play first, he or she will have opportunity to choose which child board they prefer.

	5)Who (player or AI) win one child board in the 9 boards will possess the whole grid and mark all the elements in this grid to be ‘O’ at same time . The opponent could only choose other boards to place ‘X’ or ‘O’.

	6) Game finished when one player firstly wins 3 child boards in row horizontally, vertically, or diagonally.
