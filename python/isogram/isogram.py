def is_isogram(string):
	copy = string.replace("-", "").replace(" ", "").upper()
	for i in range(len(copy)-1):
		for j in range(i+1, len(copy)):
			if copy[i] == copy[j]:
				return False
	return True
