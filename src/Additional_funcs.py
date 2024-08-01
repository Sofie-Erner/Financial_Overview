"""
File containing additional functions which will be used by other scripts
"""
import os
import pandas as pd

def check_file(filename,file_type):
	# Check if file exists and is an 'file_type' file
	type_2 = "." + file_type

	empty_file = 0 # Set to 1 if file empty

	# Check file extension
	if not filename.lower().endswith(type_2):
		print(filename," is not an ",file_type," file")
		exit()

	# Check if file exists
	if not os.path.isfile(filename):
		print(filename," is not a file")
		
		txt_in = input("Create this file? [y/n]")
		if txt_in == "y":
			if file_type == "csv":
				df = pd.DataFrame([])
				df.to_csv(filename)
			elif file_type == "xlsx":
				df = pd.DataFrame([])
				df.to_excel(filename)
			else:
				f = open(filename,"x") # Create file
				f.close()

			empty_file = 1 # file will now be empty
		else:
			print("Error exiting")
			exit()

	# Check if file empty
	if os.path.getsize(filename) == 0:
		empty_file = 1

	# Return file status
	return empty_file