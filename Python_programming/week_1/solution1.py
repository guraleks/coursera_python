import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    for j in range(num_steps - i - 1):
        sys.stdout.write(' ')
    for k in range(i + 1):
        sys.stdout.write('#')
    print('')
