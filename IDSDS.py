from terminaltables import AsciiTable

def IDSDS(payoff_matrix):

	prev_matrix = payoff_matrix
	payoff_matrix = one_round(payoff_matrix)

	while prev_matrix != payoff_matrix:
		prev_matrix = payoff_matrix
		payoff_matrix = one_round(payoff_matrix)

	# print final payoff matrix, row by row
	table_data = []
	for i in range(0, len(payoff_matrix)):
		table_data.append(payoff_matrix[i])

	table = AsciiTable(table_data)
	table.inner_heading_row_border = False
	table.inner_row_border = True
	print table.table


def one_round(payoff_matrix):
	# eliminate rows
	new_matrix = eliminate_rows(payoff_matrix, len(payoff_matrix), len(payoff_matrix[0]))

	# eliminate columns
	new_matrix = eliminate_cols(new_matrix, len(new_matrix), len(new_matrix[0]))

	return new_matrix

def eliminate_rows(payoff_matrix, r, c):
	cur = 0 

	eliminated = []
	while cur < r:
		row = payoff_matrix[cur]

		for i in range(0, r):
			if cur != i:
				other_row = payoff_matrix[i]
				dominant = True

				for j in range(0, c):
					if row[j][0] >= other_row[j][0]:
						dominant = False
						break

				if dominant:
					eliminated.append(cur)
					break

		cur += 1

	reduced_matrix = []
	for k in range(0, r):
		if k not in eliminated:
			reduced_matrix.append(payoff_matrix[k])

	return reduced_matrix


def eliminate_cols(payoff_matrix, r, c):
	cur = 0

	eliminated = []
	while cur < c:

		for i in range(0, c):
			if cur != i:
				dominant = True

				for j in range(0, r):
					if payoff_matrix[j][cur][1] >= payoff_matrix[j][i][1]:
						dominant = False
						break

				if dominant:
					eliminated.append(cur)
					break

		cur += 1

	reduced_matrix = []

	for k in range(0, r):
		new_row = []
		for l in range(0, c):
			if l not in eliminated:
				new_row.append(payoff_matrix[k][l])
		reduced_matrix.append(new_row)

	return reduced_matrix


if __name__ == "__main__":
	n = int(raw_input("enter number of rows: "))
	print 

	matrix = []
	for i in range(0, n):
		row = eval(raw_input("enter row of tuples (payoffs): "))
		matrix.append(row)

	print
	print "final strategies: "
	IDSDS(matrix)


