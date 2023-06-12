command = input()

my_list_for_chat = []

while command != 'end':
	command = command.split()

	if command[0] == 'Chat':
		my_list_for_chat.append(command[1])

	if command[0] == 'Delete':
		if command[1] in my_list_for_chat:
			position = my_list_for_chat.index(command[1])
			my_list_for_chat.pop(position)

	if command[0] == 'Edit':
		if command[1] in my_list_for_chat:
			position = my_list_for_chat.index(command[1])
			my_list_for_chat[position] = command[2]

	if command[0] == 'Spam':
		for c in command[1:]:
			my_list_for_chat.append(c)

	if command[0] == 'Pin':
		if command[1] in my_list_for_chat:
			position = my_list_for_chat.index(command[1])
			my_list_for_chat.append(my_list_for_chat.pop(position))

	command = input()

print('\n'.join(my_list_for_chat))