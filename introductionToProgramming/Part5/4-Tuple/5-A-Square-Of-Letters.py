layers = int(input("Layers: "))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create the square
square = []
for row in range(2*layers-1):
    row = []
    for column in range(2*layers-1):
        row.append('')
    square.append(row)

# Fill the square
for i in range(layers):
    letter = alphabet[layers-i-1]
    for j in range(i, 2*layers-1-i):
        square[i][j] = letter
        square[j][i] = letter
        square[2*layers-2-i][j] = letter
        square[j][2*layers-2-i] = letter

# Print the square
for row in square:
    row_print = ""
    for letter in row:
        row_print += letter
    print(row_print)