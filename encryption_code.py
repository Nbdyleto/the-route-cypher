# Load the original text

original_text = "Hey I Like Cook French Potatos and I Really Believe That I Will Be A Great Chef Kitchen One Day"

print("Original Message:\n", original_text)

# Convert text into a list to split out individual words
original_split = original_text.split()

# Get input for the number of cols and rows.
COLS = 4
ROWS = 5

# Get input for the key.
key = [-1, 2, -3, 4] # "Negative numbers mean you start at the bottom and read up a column; positive numbers mean the reverse."

# Get the matrix from original list
count = 0
original_matrix = []
for row in range(ROWS):
    temp_matrix = []
    for col in range(COLS):
        word = original_split[count]
        temp_matrix.append(word)
        count += 1
    original_matrix.append(temp_matrix)

# Create a new list for the cipher matrix.

cipher_matrix = []

# For every number in the key:
# Create a new list and append every n items (n = # of rows) from the original matrix.
# Use the sign of key number to decide whether to read the row forward or backward.
# Using the chosen direction, add the new list to the matrix. The index of each
# new list is based on the column number used in the key.

cipher_text = ''

# Ciphering:
for num in key:
    col = abs(num)-1
    if num < 0:
        for row in range(ROWS-1, -1, -1):
            item = original_matrix[row][col]
            cipher_text += item + ' '
    else:
        for row in range(ROWS):
            item = original_matrix[row][col]
            cipher_text += item + ' '

print('cipher_text:\n', cipher_text)

