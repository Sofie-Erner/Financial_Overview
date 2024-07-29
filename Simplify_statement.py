# ----- Simplify Bank Statements -----
# This script will read through statements and specify their category
# Categories are based off Test_expenses_categories.cvs currently
#
# --------------------------------

# ----- Libraries -----
import pandas as pd
import numpy as np
import os
from Additional_funcs import check_file

def SimplifyStatement(in_doc,out_doc,exp_cat):
	path = os.path.abspath(os.getcwd()) # path to directory of script

	# ----- Dictionary with Categories for Expenses -----
	exp_doc = str(path) + "/" + exp_cat # path to csv file
	check_file(out_doc,"csv")
	df_exp = pd.read_csv(exp_doc,header=0) # dateframe of expenses categories and examples

	expenses = {}
	for i in range(len(df_exp)):
		test_list = np.array(df_exp.loc[i])[1:]
		test_list = test_list[~pd.isnull(test_list)]
		
		expenses[str(df_exp.loc[i][0])] = test_list
		
	exp_cat = expenses.keys() # List of expenses catefories

	# ----- Input File -----
	in_doc = str(path) + "/" + in_doc # path to bank statement (input file)
	check_file(in_doc,"xlsx")
	f_in = pd.ExcelFile(in_doc, engine='openpyxl') 
	print(f_in.sheet_names)

	# ----- Output File -----
	out_doc = str(path) + "/" + out_doc # path to output simplified bank statement
	check_file(out_doc,"xlsx")
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


SimplifyStatement("tests/Test_bank_statement.test","tests/Test_statement_simplify.test","tests/Test_expenses_categories.test")