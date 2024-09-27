# ----- Financial History -----
# This script will read through the simplified bank statement
# Categories, based off csv file, will be added separately, together with balance, dates, and income
# --------------------------------

# ----- Libraries -----
import pandas as pd
import numpy as np
import datetime
import os
import sys
sys.path.append("../")

import src
from src.Additional_funcs import check_file
from src.Get_expense_categories import GetExpenseCategory

# ----- Function for simplifying bank statements -----
def FinancialHistory(in_doc,exp_cat_doc,out_doc):
	path = os.path.abspath(os.getcwd()) # path to directory of script

	# ----- Variables -----
	out_doc = "" # name of output file
	out_cols = ["Date","Category","Money In","Money Out","Balance"] # columns of output file
	out_data = [] # list wil contain data for output file

	# ----- Dictionary with Categories for Expenses -----
	expenses = GetExpenseCategory(exp_cat_doc) # Dictionary with expense categories, will contain list of key words for each category
		
	exp_cat = expenses.keys() # List of expenses categories
	print(expenses)
	
	# ----- Input File -----
	in_doc = str(path) + "/" + in_doc # path to bank statement (input file)
	empty_file = check_file(in_doc,"xlsx")

	if empty_file == 1:
		print("Error: input statement,",in_doc,", is empty")
		exit()

	f_in = pd.ExcelFile(in_doc, engine='openpyxl') 
	#print(f_in.sheet_names)