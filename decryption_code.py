original_msg = "Hey I Like Cook French Potatos and I Really Believe That I Will Be A Great Chef Kitchen One Day"
key = [-1, 2, -3, 4] # "Negative numbers mean you start at the bottom and read up a column; positive numbers mean the reverse."

spl_msg = original_msg.split()
encryption_matrix = [] 
count = 0
for row in range(5):
    temp_matrix = []
    for col in range(4):
        word = spl_msg[count]
        temp_matrix.append((word, count))
        count += 1
    encryption_matrix.append(temp_matrix)
print(encryption_matrix)  

# Now, get the cyphertext, in the order they where read.
