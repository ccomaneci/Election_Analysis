#How many votes did you get?
from itertools import count


my_votes = int(input("How many votes did you get in the election?"))

#Total votes in the election
total_votes = int(input("What is the total votes in the elcetion?"))

#Calculate the prencentage of votes you received.
percentage_votes = (my_votes / total_votes)*100
print("I reveived" + str(percentage_votes) + "% of the total votes.")

counties = ["Arapahoe", "Denver","jefferson"]

if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("what is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.") 

#what is the score?
score = int(input("what is your test score?"))  

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is a F.')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[1]) 

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}    

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)    

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for kcounty, voters in counties_dict.items():
    print (county, voters)

voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"jefferson","registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)
    
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"Ireceived {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe":369237,"Denver":413229,"Jefferson":390222}
for county, voters in counties_dict.items():
    print(county + "county has" + str(voters) + "registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
f"You receieved {candidate_votes} number of votes." 
f"The total number of votes in the election was {total_votes}."
f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")








