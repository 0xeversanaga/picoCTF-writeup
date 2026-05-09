from sys import argv

if __name__ == '__main__':
	if len(argv) != 2:
		print(f"{argv[0]} <data>")
		exit()

	if len(argv[1]) != 32:
		print(f"data is not 32 bytes: {len(argv[1])}")
		exit()

	data = argv[1]

	l = []
	t = [0, 0, 0, 0, 0, 0, 0, 0]

	for j in data:
		l.append(ord(j))

	for o in range(0, 8):
		f1 = l[o*4] << 24 # first character
		f2 = l[o*4+1] << 16
		f3 = l[o*4+2] << 8
		f4 = l[o*4+3]

		t[o] = f1 | f2 | f3 | f4
		print(f"{data[o*4]}: {f1} -- {bin(ord(data[o*4]))} -> {bin(f1)}")
		print(f"{data[o*4+1]}: {f2} -- {bin(ord(data[o*4+1]))} ->{bin(f2)}")
		print(f"{data[o*4+2]}: {f3} -- {bin(ord(data[o*4+2]))} ->{bin(f3)}")
		print(f"{data[o*4+3]}: {f4} -- {bin(ord(data[o*4+3]))} ->{bin(f4)}")
		print(f"total: {t[o]} -- {bin(t[o])}\n")

	print(t)
