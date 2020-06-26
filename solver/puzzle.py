import solver.constant as constant

class Puzzle:
    def __init__(self, grid):
        self.grid = [0 for i in range(81)]
        self.values = [constant.digits for j in range(81)]
        for i, n in enumerate(grid):
            if n != 0:
                self.assign(i, str(n))

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

    def assign(self, square, num):
        # Loop through and eliminate candidates
        digitsToElim = self.values[square].replace(num, '')
        for d in digitsToElim:
            self.eliminate(square, d)

    def eliminate(self, square, num):
        # Eliminate num
        self.values[square] = self.values[square].replace(num, '')

        # If square is newly determined, then eliminate from peers
        if len(self.values[square]) == 1:
            if self.grid[square] == 0:
                self.grid[square] = int(self.values[square])
                for peerIndex in constant.peers[square]:
                    self.eliminate(peerIndex, self.values[square])
                    
        # If unit has only one possible space for num, do assignment there
        for unit in constant.units[square]:
            possible = [sq for sq in unit if num in self.values[sq]]
            if len(possible) == 1:
                if self.grid[possible[0]] == 0:
                    self.grid[possible[0]] = int(num)
                    self.assign(possible[0], num)

    def search(self):
        pass
