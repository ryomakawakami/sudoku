import solver.constant as constant

class Puzzle:
    def __init__(self, grid):
        self.done = False
        self.doneSquares = [False for i in range(81)]
        self.values = [constant.digits for j in range(81)]
        for i, n in enumerate(grid):
            if n != 0:
                self.assign(i, str(n))

    def display(self):
        for i, n in enumerate(self.values):
            if len(n) == 1:
                print(n, end=' ')
            else:
                print(' ', end=' ')
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
            if not self.doneSquares[square]:
                for peerIndex in constant.peers[square]:
                    self.eliminate(peerIndex, self.values[square])
                self.doneSquares[square] = True
                    
        # If unit has only one possible space for num, do assignment there
        for unit in constant.units[square]:
            possible = [sq for sq in unit if num in self.values[sq]]
            if len(possible) == 1:
                if not self.doneSquares[possible[0]]:
                    self.assign(possible[0], num)
                    self.doneSquares[possible[0]] = True

    def search(self, values):
        # Check if done
        if all(len(values[s]) == 1 for s in range(81)):
            self.done = True
            return

        _, square = min((len(values[sq]), sq) for sq in range(81) if range(81) if len(values[sq]) > 1)
        for num in values[square]:
            self.search(assign(values.copy(), square, num))
            if self.done == True:
                return

# Change self.values in assign and eliminate to values
