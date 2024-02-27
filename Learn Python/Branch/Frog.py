length_of_right_step, length_of_left_step, steps = map(int, input().split())

if steps % 2 == 0:
    right_steps = steps // 2
else:
    right_steps = steps // 2 + 1
left_steps = steps - right_steps

coordinate = right_steps * length_of_right_step - left_steps * length_of_left_step

print(coordinate)