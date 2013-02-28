#x = '''Hello!!! Loki ipsum dolor sit amet, consectetur adipiscing elit. Sed cursus convallis lorem at lobortis?? Quisque tempus congue tincidunt!'''

def rot13(x):
	letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	cap = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
	output = []
	for i in x:
		if i in letter:
			output.append(letter[letter.index(i) - 13])
		elif i in cap:
			output.append(cap[cap.index(i) - 13])
		else:
			output.append(i)

	return ''.join(output)

