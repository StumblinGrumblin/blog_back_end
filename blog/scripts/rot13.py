letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
cap = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

x = '''Hello ipsum dolor sit amet, consectetur adipiscing elit. Sed cursus convallis lorem at lobortis. Quisque tempus congue tincidunt. Mauris eros lorem, fringilla at sollicitudin nec, eleifend vitae metus. Integer porttitor rutrum eros sed ornare. Nullam tincidunt mi et erat bibendum aliquam. Etiam tincidunt, odio in varius volutpat, leo eros mattis massa, eget adipiscing purus nulla id dolor. In a augue ut felis bibendum aliquet. Nulla accumsan, nisi ut viverra euismod, justo metus placerat nisi, id congue dolor odio quis risus. Nunc urna elit, vehicula ut semper sed, faucibus vitae leo. Sed interdum pellentesque tellus, eu pharetra enim sollicitudin sodales. '''


def rot13(x):
	output = []
	for i in x:
		if i in letter:
			output.append(letter[letter.index(i) - 13])
		elif i in cap:
			output.append(cap[cap.index(i) - 13])
		else:
			output.append(i)

	return ''.join(output)

