import util
from collections import defaultdict

class GameBoard(object):
    
    def __init__(self, game_state):
        self._game_state = {}
        self._row_matches = defaultdict(lambda:[])
        self._column_matches = defaultdict(lambda:[])
        self._winning_numbers = []
        column_count = len(game_state[0])
        for r in range(0, len(game_state)):
            for c in range(0, column_count):
                value = game_state[r][c]
                self._game_state[value] = (r,c)


    def play_game(self, number_calls):
        for count, num in enumerate(number_calls):
            if num in self._game_state:
                self._winning_numbers.append(num)
                r,c = self._game_state[num]
                self._row_matches[r].append(num)
                self._column_matches[c].append(num)
                if len(self._row_matches[r]) == 5:
                    return count 

                if len(self._column_matches[c]) == 5:
                    return count
    

    def score(self):
        board_total = sum(self._game_state.keys())
        called_numbers_total = sum(self._winning_numbers)
        return (board_total - called_numbers_total) * self._winning_numbers[-1]


def run():
    input = util.read_file("day04/input.txt", str)
    bingo_numbers, game_boards = process_input(input)
    losing_board = find_loser(bingo_numbers, game_boards)
    print("result", losing_board.score())


def parse_board(rows):
    board_state = [[int(v) for v in r.split()] for r in rows]
    return GameBoard(board_state)


def process_input(input):
    bingo_numbers = [int(n) for n in input[0].split(",")]

    game_boards = []
    for i in range(1, len(input),5):
        game_boards.append(parse_board(input[i:i+5]))
    
    return bingo_numbers, game_boards


def find_loser(nums, boards):
    worst_board = None
    worst_board_count = 0
    for board in boards:
        calls_to_win = board.play_game(nums)
        if calls_to_win > worst_board_count:
            worst_board = board
            worst_board_count = calls_to_win
    
    return worst_board

     