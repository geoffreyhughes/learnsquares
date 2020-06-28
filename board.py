import chess

board = chess.Board()

# Nf3 = chess.Move.from_uci("g1f3")
# board.push(Nf3)

import numpy as np
import matplotlib.pyplot as plt
chessboard = np.zeros((8,8))
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [0, 1, 2, 3, 4, 5, 6, 7]

x_squares = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
y_squares = [8, 7, 6, 5, 4, 3, 2, 1]

plt.xticks(x, x_squares)
plt.yticks(y, y_squares)

plt.imshow(chessboard, cmap='binary')
plt.show()
