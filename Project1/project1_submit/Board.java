public class Board {
	private String[][] board;
	private int N;

	public Board(int N) {
		this.N = N;
		board = new String[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				board[i][j] = "*";
// Test Case 1
//		board[0][0] = "X";
//		board[0][1] = "X";
//		board[0][2] = "X";
//		board[1][0] = "*";
//		board[1][1] = "*";
//		board[1][2] = "*";
//		board[2][0] = "*";
//		board[2][1] = "*";
//		board[2][2] = "*";
// Test Case 2
//		board[0][0] = "X";
//		board[0][1] = "X";
//		board[0][2] = "*";
//		board[1][0] = "*";
//		board[1][1] = "O";
//		board[1][2] = "*";
//		board[2][0] = "*";
//		board[2][1] = "*";
//		board[2][2] = "O";
// Test Case 3
//		board[0][0] = "X";
//		board[0][1] = "*";
//		board[0][2] = "*";
//		board[1][0] = "*";
//		board[1][1] = "*";
//		board[1][2] = "*";
//		board[2][0] = "*";
//		board[2][1] = "*";
//		board[2][2] = "O";
// Test Case 4 for scores
//		board[0][0] = "*";
//		board[0][1] = "*";
//		board[0][2] = "O";
//		board[1][0] = "*";
//		board[1][1] = "*";
//		board[1][2] = "O";
//		board[2][0] = "*";
//		board[2][1] = "*";
//		board[2][2] = "O";

	}

	public Board(Board inputboard) {
		N = inputboard.getDimension();
		board = new String[N][N];
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				board[i][j] = inputboard.getElement(i, j);
	}

	public String getElement(int i, int j) {
		return board[i][j];
	}

	public void setElement(int i, int j, String s) {
		board[i][j] = s;
	}

	public void PrintBoard() {
		//System.out.println("$$$$$$$$$$$$$$$$$$$$");
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				System.out.print(board[i][j] + "\t");
			}
			System.out.print("\n");
		}
	}

	public void PrintBoardLine(int L) {
		for (int i = 0; i < N; i++) {
			System.out.print(board[L][i] + "   ");
		}
	}

	public int getDimension() {
		return N;
	}

	public void setDead() {
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				board[i][j] = "D";
	}

	public Double Heuristic(Board board) {
		Double Res = 0.0;
		String[][] Elements = new String[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				Elements[i][j] = (board.getElement(i, j));
			}
		}

		Res = Res + getScore(Elements[0][0], Elements[0][1], Elements[0][2]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[1][0], Elements[1][1], Elements[1][2]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[2][0], Elements[2][1], Elements[2][2]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[0][0], Elements[1][0], Elements[2][0]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[0][1], Elements[1][1], Elements[2][1]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[0][2], Elements[1][2], Elements[2][2]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[0][0], Elements[1][1], Elements[2][2]);
//		System.out.println(Res);
		Res = Res + getScore(Elements[0][2], Elements[1][1], Elements[2][0]);
//		System.out.println(Res);

		return Res;
	}

	private Double getScore(String s1, String s2, String s3) {
		Double XScore = 0.;
		Double OScore = 0.;

		if 		(s1.equals("X"))	{XScore++;}
		else if (s1.equals("O"))	{OScore++;}
		if 		(s2.equals("X"))	{XScore++;}
		else if (s2.equals("O"))	{OScore++;}
		if 		(s3.equals("X"))	{XScore++;}
		else if (s3.equals("O"))	{OScore++;}

		if 			(OScore == 0 && XScore == 3)		{return  200.0;}
		else if 	(OScore == 0 && XScore == 2)		{return    2.0;}
		else if 	(OScore == 0 && XScore == 1)		{return    1.0;}
		else if 	(XScore == 0 && OScore == 3)		{return  -200.0;}
		else if 	(XScore == 0 && OScore == 2)		{return  -2.0;}
		else if 	(XScore == 0 && OScore == 1)		{return  -1.0;}
		else 	return 0.0;
	}

	public static void main(String[] args) {
		Board test = new Board(3);
		test.PrintBoard();
		System.out.println("Heuristic = " + test.Heuristic(test));
	}











}