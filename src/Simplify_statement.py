# ----- Simplify Bank Statements -----
# This script will read through statements and specify their category
# Categories are based off csv file
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
def SimplifyStatement(in_doc,exp_cat_doc):
	path = os.path.abspath(os.getcwd()) # path to directory of script

	# ----- Variables -----
	out_doc = "" # name of output file
	out_cols = ["Date","Category","Money In","Money Out","Balance"] # columns of output file
	out_data = [] # list wil contain data for output file

	# ----- Dictionary with Categories for Expenses -----
	expenses = GetExpenseCategory(exp_cat_doc) # Dictionary with expense categories, will contain list of key words for each category
		
	exp_cat = expenses.keys() # List of expenses catefories
	print(expenses)
	
	# ----- Input File -----
	in_doc = str(path) + "/" + in_doc # path to bank statement (input file)
	empty_file = check_file(in_doc,"xlsx")

	if empty_file == 1:
		print("Error: input statement,",in_doc,", is empty")
		exit()

	f_in = pd.ExcelFile(in_doc, engine='openpyxl') 
	#print(f_in.sheet_names)

	# ----- Common Expressions to Replace
	common_expr = np.array(["card payment to ","credit from ","direct debit payment to ","bill payment via faster payment to "])

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
		df.replace(expr,"", inplace=True, regex=True)
		
	#print(df)

	# ----- Loop Over Data ----- 
	for i in range(len(df)):
		# --- Get Month
		if "XXXX" in str(df.loc[i,"Date"]):
			dates = df.loc[i,"Description"].split(" ")
			date1 = dates[0].split("/")
			date2 = dates[2].split("/")

			if int(date1[2]) == int(date2[2]) and int(date1[1]) == int(date2[1]): # same month and year
				out_doc = date1[1] + "_" + "-".join(date2)
			elif int(date1[2]) == int(date2[2]): # same year
				out_doc = "-".join(date1[:2]) + "_" + "-".join(date2)
			else: # different years
				out_doc = "-".join(date1) + "_" + "-".join(date2)

			print(out_doc)
		
		elif df.loc[i,"Date"] == "Date": # don't do anything for this line
			continue

		elif not pd.isnull(df.loc[i,"Balance"]): # For lines with expenses
			data1 = df.loc[i].values.flatten().tolist() # get dataframe row
			data1[0] = str(data1[0].day) + " " + str(data1[0].month) + " " + str(data1[0].year) #date

			# Find expense category
			alloc = 0 # whether it's been allocated
			for cat in expenses: # for each category
				if any(word in data1[1] for word in expenses[cat]): # if description in categories
					data1[1] = cat # note category
					alloc = 1

			if alloc == 0: # if expense category was not found
				data1[1] = "unknown"

			out_data.append(data1) # add to data

	# ----- Output File -----
	df_out = pd.DataFrame(data=out_data,columns=out_cols)

	out_doc = str(path) + "/" + out_doc + ".xlsx" # path to output simplified bank statement
	empty_file = check_file(out_doc,"xlsx")

	if empty_file == 0:
		print("Output file ",out_doc," is not empty")

		txt_in = input("The file will be overwritten, want to continue? [y/n]")
		if txt_in != "y":
			exit()

	out_writer = pd.ExcelWriter(out_doc, engine="xlsxwriter")
	df_out.to_excel(out_writer, sheet_name='Sheet1',index=False)

	# ----- Merge balance for dates which are the same
	out_workbook = out_writer.book
	out_worksheet = out_writer.sheets['Sheet1']

	merge_format = out_workbook.add_format({'align': 'right', 'valign': 'vcenter'})

	dates = df_out["Date"].tolist()
	print(dates)
	date_counts = [(i,dates.count(dates[i])) for i in range(0,len(dates))]
	print(date_counts)

	col_ix = df_out.columns.get_loc("Balance")

	# merge cells with the same date (dates assumed to be ordered )
	i = 0
	while i < len(date_counts):
		id = date_counts[i][0]
		count = date_counts[i][1]

		if count > 1: # more than one 
			# merge "balance" cell for same dates, have value for last expense
			out_worksheet.merge_range(id+1,col_ix,id+count,col_ix,df_out.loc[id+count-1,"Balance"],merge_format)
			i = i + count
		else:
			i += 1
			
	out_writer.close()
	
