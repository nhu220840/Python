steps, lcm_of_moves = map(int, input().split())

if steps % 2 == 0:
    minimum_number_of_steps = steps // 2
else:
    minimum_number_of_steps = steps // 2 + 1
maximum_number_of_steps = steps

#Find the minimum number, such as if this number is greater or equal than x and divisible by m 
number_of_moves = (minimum_number_of_steps + lcm_of_moves - 1) // lcm_of_moves * lcm_of_moves

if number_of_moves <= maximum_number_of_steps:
    print(number_of_moves)
else: print(-1)