# Each square is a dictionary with val (int) & marked (0 or 1)
# Each board is a 2d array

def parse_board(d):
    board = [[{"val": 0, "marked": 0} for y in range(5)] for x in range(5)]
    vals = d.split()
    for i in range(0, len(vals)):
        board[int(i/5)][i%5]["val"] = int(vals[i])
    return board

# For debugging
def pretty_print(board):
    for row in board:
        s = ""
        for cell in row:
            s += str(cell["val"])
            if cell["marked"] == 1:
                s += "* "
            else:
                s += "  "
        print(s)
    print("")

# Mistakenly included diagonals as a win con, commented out
def is_winner(board):
    #diag = 0
    #rdgl = 0
    for i in range(len(board)):
        horz = 0
        vert = 0
        for j in range(len(board[0])):
            horz += board[i][j]["marked"]
            vert += board[j][i]["marked"]
        #diag += board[i][i]["marked"]
        #rdgl += board[i][len(board[0])-1-i]["marked"]
        if horz == 5 or vert == 5:
            return True
    #if diag == 5 or rdgl == 5:
    #    return True
    return False

def sum_unmarked(board):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]["marked"] == 0:
                s += board[i][j]["val"]
    return s

def mark_board(board, val):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]["val"] == val:
                board[i][j]["marked"] = 1
    return board

def play(nums, boards):
    wins = 0
    winners = []
    for n in nums:
        for i in range(len(boards)):
            boards[i] = mark_board(boards[i], n)
            if is_winner(boards[i]) and i not in winners:
                wins += 1
                winners.append(i)
            if wins == len(boards):
                print("val:", n)
                print("board:", i)
                print("sum unmarked:", sum_unmarked(boards[i]))
                print("ans:", n * sum_unmarked(boards[i]))
                return


if __name__=="__main__":
    f = open("p1.txt", "r")
    data = f.read().split("\n\n")
    f.close()
    nums = [int(n) for n in data[0].split(",")]
    boards = [parse_board(d) for d in data[1:]]
    play(nums, boards)
