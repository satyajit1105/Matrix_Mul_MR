import sys

m_r = 2
m_c = 3
n_r = 3
n_c = 2

matrix = []
for row in range(m_r):
    r = []
    for col in range(n_c):
        s = 0
        for el in range(m_c):
            mul = 1
            for num in range(2):
                try:
                    line = input()  # Use input() instead of sys.stdin.readline() for testing
                    split_result = line.split()
                    if split_result:  # Check if the split result is non-empty
                        print("Split result:", split_result)  # Print the split result for debugging
                        n = int(split_result[-1])  # Take the last element
                        mul *= n
                except EOFError:
                    break  # Exit the loop if EOF is encountered
            s += mul
        r.append(s)
    matrix.append(r)

print('\n'.join([str(x) for x in matrix]))
