# test
# The dial starts by pointing at 50.
# The dial is rotated L68 to point at 82.
# The dial is rotated L30 to point at 52.
# The dial is rotated R48 to point at 0.
# The dial is rotated L5 to point at 95.
# The dial is rotated R60 to point at 55.
# The dial is rotated L55 to point at 0.
# The dial is rotated L1 to point at 99.
# The dial is rotated L99 to point at 0.
# The dial is rotated R14 to point at 14.
# The dial is rotated L82 to point at 32.
# should be 3

# test input
# test_dial_input = [('L',68),('L',30),('R',48),('L',5),('R',60),('L',55),('L',1),('L',99),('R',14),('L',82)]

zero_count = 0
dial_input = []
current_position = int()

with open("day-1-input.txt", 'r') as file:
    lines = file.read().splitlines()
    dial_input = [(line[0], int(line[1:])) for line in lines if line] # example: [('L', 123)]

def direction_left(current_position, number):
    # going left decrements 
    # if it goes beyond 0, it rolls over 99
    # every time 0 is hit count that
    # zero_count++
    global zero_count
    new_position = current_position - number
    while new_position < 0:
        new_position = new_position + 100

    if new_position == 0:
        zero_count+=1

    current_position = new_position

    return current_position

def direction_right(current_position, number):
    # going right increments 
    # if it goes beyond 99, it rolls over to 0
    # every time 0 is hit count that
    # zero_count++
    global zero_count
    new_position = current_position + number
    while new_position > 99:
        new_position = new_position - 100

    if new_position == 0:
        zero_count+=1

    current_position = new_position

    return current_position

for x,y in enumerate(dial_input):
    direction = y[0]
    number = y[1]

    if x == 0:
        current_position = 50

    print(direction,number)
    print(f"iteration: {x}")
    print(f"current position: {current_position}\n")

    if direction == "L":
        current_position = direction_left(current_position, number)
    else:
        current_position = direction_right(current_position, number)
    

print(f"zero_count: {zero_count}")