"""
File containing additional functions which will be used by other scripts
"""
import os

def check_file(filename,file_type):
	# Check if file exists and is an 'file_type' file
	type_2 = "." + file_type

	if not os.path.isfile(filename):
		print(filename," is not a file")
		
		txt_in = input("Create this file? [y/n] ")
		if txt_in == "y":
			f = open(filename,"x") # Create file
			f.close()
		else:
			print("Error exiting")
			exit()
	if not filename.lower().endswith(type_2):
		print(filename," is not an ",file_type," file")
		exit()