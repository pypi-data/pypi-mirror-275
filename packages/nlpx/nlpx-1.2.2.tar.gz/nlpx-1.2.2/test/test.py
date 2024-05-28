

if __name__ == '__main__':
	texts = ['1', '2', '3', '4', '5']
	length = len(texts)
	batch_size = 4
	n = length / batch_size

	print([texts[i:i + batch_size] for i in range(0, len(texts), batch_size)])