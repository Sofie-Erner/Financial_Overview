import csv
import numpy as np

with open('colour_pal.csv', 'w', newline='') as csvfile: # open csv file
    fieldnames = ['r', 'g', 'b'] # column names

    writer = csv.writer(csvfile,delimiter=",") # initialise writer
    writer.writerow(fieldnames)

    file1 = open('15_colour_palette.txt', 'r') # open text file with colours
    lines = file1.readlines() # get lines

    for line in lines:
        line = line.strip() #strip lines
        a_line = line.split(" ") # split lines by whitespace
        a_line = [i for i in a_line if i] # remove empty entries

        if a_line[0] == "color": # only color lines
            writer.writerow(np.array(a_line[3:6]).astype(int)) #write rgb code to csv file
        
file1.close() # close text file