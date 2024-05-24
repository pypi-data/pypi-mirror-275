import random

class MemoryGame:
    def __init__(self):
        self.board = self.create_board()
        self.turns = 0

    def create_board(self):
        values = list(range(1, 9)) * 2
        random.shuffle(values)
        return [values[i:i+4] for i in range(0, len(values), 4)]

    def display_board(self, reveal=None):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if reveal and (i, j) in reveal:
                    print(f'{val}', end=' ')
                else:
                    print('X', end=' ')
            print()
        print()

    def play_turn(self, first, second):
        self.turns += 1
        first_val = self.board[first[0]][first[1]]
        second_val = self.board[second[0]][second[1]]
        self.display_board(reveal=[first, second])

        if first_val == second_val:
            print("Match found!")
            self.board[first[0]][first[1]] = ' '
            self.board[second[0]][second[1]] = ' '
            return True
        else:
            print("No match, try again.")
            return False

    def is_game_over(self):
        for row in self.board:
            for val in row:
                if val != ' ':
                    return False
        return True

    def start_game(self):
        while not self.is_game_over():
            self.display_board()
            print(f'Turns: {self.turns}')
            first = tuple(map(int, input('Enter first card position (row col): ').split()))
            second = tuple(map(int, input('Enter second card position (row col): ').split()))
            if not self.play_turn(first, second):
                input('Press Enter to continue...')
        print(f'Game over! You finished in {self.turns} turns.')

def main():
    game = MemoryGame()
    game.start_game()

if __name__ == '__main__':
    main()
