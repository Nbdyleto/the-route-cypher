
# Load the ciphertext

cipher_text = "Hey I Like Cook French Potatos and I Really Believe That I Will Be A Great Chef Kitchen One Day"

# Convert ciphertext into a cipherlist to split out individual words
cipher_split = cipher_text.split()

# Get input for the number of cols and rows.
COLS = 4
ROWS = 5

# Get input for the key.
key = [-1, 2, -3, 4] # "Negative numbers mean you start at the bottom and read up a column; positive numbers mean the reverse."

# Convert ciphertext into a cipherlist to split out individual words
for row in range(ROWS):
    temp_matrix = []
    for col in range(COLS):
        word = cipher_split[count]
        temp_matrix.append(word)
        count += 1
    cipher_list.append(temp_matrix)
print(cipher_list)

# Create a new list for the translation matrix.

translation_matrix = []

# For every number in the key:
# Create a new list and append every n items (n = # of rows) from the cipherlist.
# Use the sign of key number to decide whether to read the row forward or backward.
# Using the chosen direction, add the new list to the matrix. The index of each
# new list is based on the column number used in the key.

for num in key:
    print('num: ', num)
    temp_list = []
    col = abs(num)-1
    if num < 0:
        for row in range(ROWS-1, -1, -1):
            print(row, col)
            item = cipher_list[row][col]
            temp_list.append(item)
            print(temp_list)
    else:
        for row in range(ROWS-1):
            print(row, col)
            item = cipher_list[row][col]
            temp_list.append(item)
    translation_matrix.append(temp_list)

