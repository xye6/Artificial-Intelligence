public class NBoard {
	private Board[][] Nboard;
	private String[][] XorO;
	private int N;

	public NBoard(int N) {
		this.N = N;
		Nboard = new Board[N][N];
		XorO = new String[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				Nboard[i][j] = new Board(3);
				XorO[i][j] = "*";
			}
		}

//		Nboard[0][0].setElement(0, 0, "X");
//		Nboard[0][0].setElement(2, 0, "X");
//		Nboard[0][0].setElement(0, 1, "O");
//		Nboard[0][0].setElement(1, 0, "O");
//
//		Nboard[0][1].setElement(0, 1, "X");
//		Nboard[0][1].setElement(2, 0, "X");
//		Nboard[0][1].setElement(0, 2, "O");
//		Nboard[0][1].setElement(1, 1, "O");
//
//		Nboard[0][2].setElement(1, 0, "X");
//		Nboard[0][2].setElement(2, 0, "X");
//		Nboard[0][2].setElement(0, 1, "O");
//		Nboard[0][2].setElement(2, 2, "O");
//
//		Nboard[1][0].setElement(2, 0, "X");
//		Nboard[1][0].setElement(2, 1, "X");
//		Nboard[1][0].setElement(0, 2, "O");
//		Nboard[1][0].setElement(1, 0, "O");
//
//		Nboard[1][1].setElement(0, 0, "X");
//		Nboard[1][1].setElement(2, 1, "O");
//		Nboard[1][1].setElement(1, 1, "X");
//		Nboard[1][1].setElement(2, 2, "O");
//
//		Nboard[1][2].setElement(0, 0, "X");
//		Nboard[1][2].setElement(2, 0, "X");
//		Nboard[1][2].setElement(0, 1, "O");
//		Nboard[1][2].setElement(1, 0, "O");
//
//		Nboard[2][0].setElement(1, 1, "X");
//		Nboard[2][0].setElement(2, 0, "X");
//		Nboard[2][0].setElement(0, 1, "O");
//		Nboard[2][0].setElement(1, 0, "O");
//
//		Nboard[2][1].setElement(0, 1, "X");
//		Nboard[2][1].setElement(2, 0, "X");
//		Nboard[2][1].setElement(2, 1, "O");
//		Nboard[2][1].setElement(1, 2, "O");
//
//		Nboard[2][2].setElement(0, 0, "X");
//		Nboard[2][2].setElement(2, 0, "X");
//		Nboard[2][2].setElement(0, 1, "O");
//		Nboard[2][2].setElement(1, 0, "O");


//		Nboard[0][0].setElement(0, 0, "X");
//		Nboard[0][0].setElement(1, 1, "X");
//		Nboard[0][0].setElement(0, 2, "O");
//		Nboard[0][0].setElement(2, 2, "O");
//
//		Nboard[1][0].setElement(1, 2, "X");
//
//		Nboard[1][1].setElement(0, 0, "O");
//		Nboard[1][1].setElement(1, 0, "O");
//		Nboard[1][1].setElement(1, 1, "X");
//
//		Nboard[1][2].setElement(0, 0, "O");
//
//		Nboard[2][2].setElement(0, 0, "X");

	}

	public NBoard(NBoard inputnboard) {
		N = inputnboard.getNDimension();
		Nboard = new Board[N][N];
		XorO = new String[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				Nboard[i][j] = new Board(inputnboard.getBoard(i, j));
				XorO[i][j] = inputnboard.getXorO(i, j);
			}
		}
	}

	public Board getBoard(int i, int j) {
		return Nboard[i][j];
	}

	public void setBoard(int i, int j, String s) {
		XorO[i][j] = s;
	}

	public String getXorO(int i, int j) {
		return XorO[i][j];
	}

	public void PrintNBoard() {
		//System.out.println("$$$$$$$$$$$$$$$$$$$$");
		for (int i = 0; i < 3; i++) {
			for (int k = 0; k < 3; k++) {
				for (int j = 0; j < 3; j++) {
					Nboard[i][j].PrintBoardLine(k);
					System.out.print("|   ");
				}
				System.out.print("\n");
			}
			System.out.println("----------------------------------------------");
		}
	}

	public int getNDimension() {
		return N;
	}

	public static void main(String args[]) {
		NBoard test = new NBoard(3);
		test.getBoard(1, 1).setElement(1, 1, "X");
		test.getBoard(0, 0).setElement(1, 1, "O");
		test.getBoard(0, 2).setElement(0, 2, "K");
		test.PrintNBoard();
	}
}