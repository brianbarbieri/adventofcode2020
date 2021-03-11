
with open("day8/data.txt", "r") as r:
    data = [l.replace("\n", "").split(" ") for l in r.readlines()]



def run_commands(data):
    accumulator = 0
    indexes = []
    current_index = 0


    while True:
        if current_index in indexes:
            return accumulator
        indexes.append(current_index)
        current_command, value = data[current_index]
        if current_command == "nop":
            current_index += 1
        elif current_command == "acc":
            current_index += 1
            accumulator += int(value)
        else: 
            current_index += int(value)

# part 2
import numpy as np
import copy

print(data)
d = np.array(data)

found_end = False
while not found_end:
    picked_com = np.random.choice(["jmp", "nop"])
    index_picked = np.random.choice(np.where(d == picked_com)[0])
    reverse_com = {"jmp" : "nop", "nop" : "jmp"}
    new_list = copy.deepcopy(d)
    new_list[index_picked,0] = reverse_com[picked_com]
    acc = run_commands(new_list.tolist())
    print(new_list.tolist())
    found_end = True
print(f"Acummulator value: {acc}")

