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



def on_button_press(event):
   n = 300 #number of timepoints
   t_sim = range(0, stop=1, length=n)
   t_span = (0.0, 300.0)
   x, y = event.xdata, event.ydata
   u0 = [x, y]
   prob = ODEProblem(f, u0, t_span)
   sol = solve(prob)
   plt.plot(sol(t_sim, idxs=1), sol(t_sim, idxs=2), "k-", markersize=10) # path
   plt.plot(sol(t_sim, idxs=1)[1], sol(t_sim, idxs=2)[2], "*", markersize=10) # start
   plt.plot(sol(t_sim, idxs=1)[end-1], sol(t_sim, idxs=2)[end], "o", markersize=10) # end
   fig.canvas.draw()


plt.canvas.mpl_connect("button_press_event", on_button_press)
plt.show()
