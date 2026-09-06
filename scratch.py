# day 1:

# # this works but not as readable
# with open("day-1-input.txt", 'r') as file:
#     lines = file.read().splitlines()
#     input_list = []
#     # example: [('L', 123)]
#     for line in lines:
#         input_list.append((line[0],int(line[1:])))
#     print(input_list)

# # this is better and more readable
# with open("day-1-input.txt", 'r') as file:
#     lines = file.read().splitlines()
#     input_list = [(line[0], int(line[1:])) for line in lines if line]
#     print(input_list)

# dial_input = [('L',68),('L',30),('R',48),('L',5),('R',60),('L',55),('L',1),('L',99),('R',14),('L',82)]

# for x,y in enumerate(dial_input):
#     direction = y[0]
#     number = y[1]
#     print(x)
#     print(direction, number)

# for x in dial_input:
#     print(dial_input[x][0])
#     print(dial_input[x][1])



# day 2: