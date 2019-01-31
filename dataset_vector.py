def return_dataset() : 
	
	dataset = []
	# Open dataset.txt file with read only permit
	f = open('dataset.txt')
	#read all lines 
	lines = f.readlines()

	# converting each line of dataset.txt from string to vector of int 
	
	for line in lines :
		temp_vec = map(int, line.split(',')) 
		dataset.append(temp_vec)

	# close the file when we finish 
	f.close()

	return dataset

