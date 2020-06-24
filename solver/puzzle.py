import solver.constant as constant

class Puzzle:
    def __init__(self, grid):
        self.grid = [0 for i in range(81)]
        self.values = [[1 for i in range(9)] for j in range(81)]    # 1 if possibility of being that number (index + 1)
        for i, n in enumerate(grid):
            if n != 0:
                self.assign(i, n - 1)

    def display(self):
        for i, n in enumerate(self.grid):
            print(n, end=' ')
            if i % 9 == 8:
                print()
                if i < 80 and i // 9 % 3 == 2:
                    print('---------------------')
            elif i % 3 == 2:
                print('| ', end='')
        print()

    # num must be index of number (e.g. num = 0 to represent 1)
    def assign(self, square, num):
        # Loop through and eliminate candidates
        for i, x in enumerate(self.values[square]):
            if x == 1 and i != num:
                self.eliminate(square, i)

    def eliminate(self, square, num):
        # Eliminate num
        self.values[square][num] = 0

        # If square is newly determined, then eliminate from peers
        for i in range(9):
            if self.values[square][i] == 1:
                if sum(self.values[square][i+1:]) == 0:
                    if self.grid[square] == 0:
                        self.grid[square] = i + 1
                        for peerIndex in constant.peers[square]:
                            self.eliminate(peerIndex, i)
                else:
                    break

        # If unit has only one possible space for num, do assignment there
        for unit in constant.units[square]:
            possible = [sq for sq in unit if self.values[sq][num] == 1]
            if len(possible) == 1:
                if self.grid[possible[0]] == 0:
                    self.grid[possible[0]] = num
                    self.assign(possible[0], num)
