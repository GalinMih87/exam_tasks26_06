friends_list_rep = list(map(str, input().split(", ")))
count_black = 0
count_err = 0

while True:
    command = input().split()

    if command[0] == "Report":
        break

    if command[0] == "Blacklist":
        if command[1] in friends_list_rep:
            print(f"{command[1]} was blacklisted.")
            a = 0
            for index, element in enumerate(friends_list_rep):
                if element == command[1]:
                    friends_list_rep[index] = "Blacklisted"
            count_black += 1
        else:
            print(f"{command[1]} was not found.")

    if command[0] == "Error":
        index = int(command[1])
        if 0 <= index <= len(friends_list_rep):
            friends_list_rep.remove(command[1])
            if friends_list_rep.pop(index) not in friends_list_rep:
                print(f"{friends_list_rep.pop(index)} was lost due to an error.")
                a = 0
                for index, element in enumerate(friends_list_rep):
                    if element == command[1]:
                        friends_list_rep[index] = "Lost"
                count_err += 1

    if command[0] == "Change":
        index = int(command[1])
        name = command[2]
        if 0 <= index <= len(friends_list_rep):
            friends_list_rep[index] = name
            print(f"{friends_list_rep[index]} changed his username to {name}.")

print(f"Blacklisted names: {count_black}")
print(f"Lost names: {count_err}")
print(*friends_list_rep, sep=" ")

