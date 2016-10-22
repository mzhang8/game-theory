import sys

def nash_equilibria(p1_matrix, p2_matrix):

  # combine payoff matrices for player 1 and 2
  payoff_matrix = combine_payoffs(p1_matrix, p2_matrix)

  # find best replies for each player for other player's strategies
  rows = len(payoff_matrix)
  cols = len(payoff_matrix[0])
  p1_best_reply(payoff_matrix, rows, cols)
  p2_best_reply(payoff_matrix, rows, cols)

  # find all strategy profiles that are nash equilibria
  for row in payoff_matrix:
    for payoff in row:
      if payoff['br1'] and payoff['br2']:
        print '[%d, %d]' % (payoff['p1'], payoff['p2'])


def p1_best_reply(payoff_matrix, r, c):
  for i in range(0, c):
    max_row = []
    max_payoff = -sys.maxint - 1

    for j in range(0, r):
      if payoff_matrix[j][i]['p1'] > max_payoff:
        max_row = [j]
        max_payoff = payoff_matrix[j][i]['p1']
      elif payoff_matrix[j][i]['p1'] == max_payoff:
        max_row.append(j)

    for row in max_row:
      payoff_matrix[row][i]['br1'] = True


def p2_best_reply(payoff_matrix, r, c):
  for i in range(0, r):
    max_col = []
    max_payoff = -sys.maxint - 1

    for j in range(0, c):
      if payoff_matrix[i][j]['p2'] > max_payoff:
        max_col = [j]
        max_payoff = payoff_matrix[i][j]['p2']
      elif payoff_matrix[i][j]['p2'] == max_payoff:
        max_col.append(j)

    for col in max_col:
      payoff_matrix[i][col]['br2'] = True


def combine_payoffs(p1_matrix, p2_matrix):
  combined_matrix = []

  for i in range(0, len(p1_matrix)):
    combined_row = []

    for j in range(0, len(p1_matrix[i])):
      payoff_obj = {'p1': float(p1_matrix[i][j]), 'p2': float(p2_matrix[i][j]), 'br1': False, 'br2': False}
      combined_row.append(payoff_obj)

    combined_matrix.append(combined_row)

  return combined_matrix


if __name__ == "__main__":
  n = int(raw_input("enter number of rows for each payoff matrix: "))
  print 

  p1 = []
  for i in range(0, n):
    row = raw_input("enter payoff row " + str(i) + " for player 1: ").split(' ') 
    p1.append(row)

  print

  p2 = []
  for i in range(0, n):
    row = raw_input("enter payoff row " + str(i) + " for player 2: ").split(' ')
    p2.append(row)

  print
  print "nash equilibria: "
  nash_equilibria(p1, p2)



