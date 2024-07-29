# ----- Simplify Bank Statements -----
# This script will read through statements and specify their category
# Categories are based off Test_expenses_categories.cvs currently
#
# --------------------------------

# ----- Libraries -----
import pandas as pd
import numpy as np
import sys
import os
import calendar

path = os.path.abspath(os.getcwd()) # path to directory of script

# ----- Functions -----
def check_excel(filename):
	# Check if file exists and is an excel file

	if not os.path.isfile(filename):
		print(filename," is not a file")
		
		txt_in = input("Create this file? [y/n] ")
		if txt_in == "y":
			f = open(filename,"x") # Create file
			f.close()
		else:
			print("Error, exiting")
			exit()
	if not filename.lower().endswith(('.xlsx','.xls')):
		print(filename," is not an excel spreadsheet")
		exit()

# ----- Dictionary with Categories for Expenses -----
exp_doc = str(path) + "/" + "Test_expenses_categories.csv"
df_exp = pd.read_csv(exp_doc,header=0) # dateframe of expenses categories and examples

expenses = {}
for i in range(len(df_exp)):
	test_list = np.array(df_exp.loc[i])[1:]
	test_list = test_list[~pd.isnull(test_list)]
	
	expenses[str(df_exp.loc[i][0])] = test_list
	
exp_cat = expenses.keys() # List of expenses catefories

# ----- Command Line Arguments -----
if len(sys.argv) < 3:
	print("Not enough arguments, needs document to read from and to")
	exit()

in_doc = sys.argv[1] # Input excel file
out_doc = sys.argv[2] # Output excel file

# ----- Input File -----
in_doc = str(path) + "/" + in_doc
check_excel(in_doc)
f_in = pd.ExcelFile(in_doc, engine='openpyxl') 
print(f_in.sheet_names)

# ----- Output File -----
out_doc = str(path) + "/" + out_doc
check_excel(out_doc)
f_out = pd.ExcelFile(out_doc, engine='openpyxl')
print(f_out.sheet_names)

# ----- Common Expressions to Replace
common_expr = np.array(["card payment to ","credit from ","direct debit payment to ","bill payment via faster payment to "])
date_expr = np.array(["00:00:00"])

# ----- Import Data ----- 
df = pd.read_excel(in_doc)

df.dropna(how="all",axis=1,inplace=True) #remove empty columns

if len(df.columns) != 5:
	print("Error in number of columns")
	exit()

# --- rename columns
df.rename({df.columns[0]:"Date"},axis='columns', inplace=True)
df.rename({df.columns[1]:"Description"},axis='columns', inplace=True)
df.rename({df.columns[2]:"Money in"},axis='columns', inplace=True)
df.rename({df.columns[3]:"Money out"},axis='columns', inplace=True)
df.rename({df.columns[4]:"Balance"},axis='columns', inplace=True)

# --- make descriptions easier to deal with
df["Description"] = df["Description"].str.lower()
for expr in common_expr:
	df["Description"].replace(expr,"", inplace=True, regex=True)
	
print(df)