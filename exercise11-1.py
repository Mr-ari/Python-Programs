def store_dict(file_name):
	fp = open (file_name,'r')
	Num = 1;
	line = "initialize";
	word_dict = dict()
	while (line != "bye"):
		line = fp.readline()
		print(line)
		word_dict[line] = Num;
		Num += 1
	fp.close()
	inp = input("Enter the string:")
	if inp in word_dict:
		print("string is present")

	else:
		print("String is not present")


		
store_dict("words1.txt")
	



		


