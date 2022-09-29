#Import the datetime clase formthe datetime module
import datetime
#from lib2to3.pytree import _Results

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

total_votes = 0

candidate_options=[]

candidate_votes ={}

#track the winning candidate, vote count, and percentage. 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the elction results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next (file_reader)

    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

#print(candidate_votes)    

with open(file_to_save, "w") as txt_file:
    election_results= (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)    


        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


    winning_candidate_summary = (f"------------------------\n" 
        f"Winner: {winning_candidate}\n" 
        f"Winning vote count: {winning_count:,}\n" 
        f"Winning Percentage: {winning_percentage:.1f}%\n" 
        f"------------------------\n")
    print(winning_candidate_summary) 

    txt_file.write(winning_candidate_summary)   


