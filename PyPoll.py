#Import the datetime clase formthe datetime module
import datetime

#Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()

#Print the present time
print("The time right now is", now)

import datetime as dt
now = dt.datetime.now()
print("The time right now is", now)

#assign a varibale for the file to load the path
file_to_load = "Resources/election_results.csv"

#open the election results and read the file.
election_data = open(file_to_load, 'r')

#to do: perform analysis.
#close the file
election_data.close()

#open the election results and read the file
with open(file_to_load) as election_data:

    #to do: perform analysis
    print(election_data)

election_data.close()

import csv
import os
#assign a variable for the files to load and the path

file_to_load = os.path.join("resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the elction results and read the file
with open(file_to_load) as election_data:

    #print the file object
    print(election_data)

file_to_save = os.path.join("analysis", "election_analysis.txt")
open(file_to_save, "w")

file_to_save = os.path.join("analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson")
    txt_file.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("\n--------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    txt_file.close()  


import csv
import os
#assign a variable for the files to load and the path

file_to_load = os.path.join("resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the elction results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next (file_reader)
    print(headers)
