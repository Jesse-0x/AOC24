input_file = 'input.txt'

grid = [line.strip().upper() for line in open(input_file) if line.strip()]

def mas(sequence):
    return ''.join(sequence) == "MAS" or ''.join(sequence) == "SAM"

count = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        d1 = [grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]
        d2 = [grid[i-1][j+1], grid[i][j], grid[i+1][j-1]]
        if mas(d1) and mas(d2):
            count += 1

print(count)