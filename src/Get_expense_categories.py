# ----- Get Expense Categories from csv file -----
# Function which reads through csv file
# Import expense categories and their associated key words
# Returns dictionary with categories as keys and list of key words as value
# --------------------------------

# ----- Libraries -----
import pandas as pd
import numpy as np
import os

import src
from src.Additional_funcs import check_file

# ----- Function for to make dictionary for expense categories -----
def GetExpenseCategory(exp_cat_doc):
    path = os.path.abspath(os.getcwd()) # path to directory of script
    exp_doc = str(path) + "/" + exp_cat_doc # path to csv file
    check_file(exp_doc,"csv")
    df_exp = pd.read_csv(exp_doc,header=0) # dateframe of expenses categories and examples

    if len(df_exp) < 1:
        print("Error: expense categories,",exp_cat_doc,", is empty")
        exit()

    first_col = df_exp.columns.tolist()[0] # Get index for first column

    expenses = {} # Dictionary with expense categories, will contain list of key words for each category
    for i in range(len(df_exp)):
        test_list = np.array(df_exp.loc[i])[1:]
        test_list = test_list[~pd.isnull(test_list)]
		
        expenses[str(df_exp.loc[i][first_col])] = test_list
		
    return expenses