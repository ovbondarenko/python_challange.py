import os
import csv
'''
main.py() reads "election_data.csv" and counts the total number of votes,
the number of votes casted for each candidate and identifies the winner.
The summary of the election results are printed into the termnal 
and exported as a text file ("output.txt").

'''
path = os.path.join('.','election_data.csv')

candidates = []


with open(path, 'r') as file:
    reader = csv.reader(file)
    # build lists containing (1)- voter ids, (2)
    for line in reader:
        candidates.append(line[2])

def total_votes(arr):
    # total_votes() coiunts total votes casted in the election
    return (len(arr)-1)

def candidate_list(candidates):
    # candidate_list() creates a list of from the list f votes
    names = []
    for i, name in enumerate(candidates):
        if i>0 and name not in names:
            names.append(name)
    return names

def count_votes(candidate):
    # count_votes() tallies the votes casted for each candidate
    count = 0
    for item in candidates[1:len(candidates)]:
        if item == candidate:
            count+=1
    return count

def calculate_percentage(number, total):
    # calculate_percentage() takes the number of votes casted 
    # for a candidate and a total number of votes and
    # calculates the percentage
    return round(number*100/total)

def find_the_winner(percentage, candidates):
    # find_the_winner() identifies the index of the highest vote percentage
    # and outputs the name of the candidate assosiated with it
    max_votes = max(percentage)
    winner_ind  = percentage.index(max_votes)
    return candidates[winner_ind]


def report(total, candidates, counter, percentage, winner):
    # report() accepts the poll results and creates a list 
    # of formatted strings
    return [f'\n',f'Election Results\n',
        '-----------------------------------------------\n',
        f'Total votes: {total}\n',
        '-----------------------------------------------\n',
        f'{candidates[0]}: {percentage[0]}% ({counter[0]})\n',
        f'{candidates[1]}: {percentage[1]}% ({counter[1]})\n',
        f'{candidates[2]}: {percentage[2]}% ({counter[2]})\n',
        f'{candidates[3]}: {percentage[3]}% ({counter[3]})\n',
        '-------------------------------------------------\n',
        f'Winner: {winner}\n',
        '-------------------------------------------------\n']

votes = total_votes(candidates)
candidate_list = candidate_list(candidates)
counter = [count_votes(candidate) for candidate in candidate_list]
percentage = [calculate_percentage(count, votes) for count in counter]
winner = find_the_winner(percentage, candidate_list)
report = report(votes, candidate_list, counter, percentage, winner)


# Create a .txt file 
with open('output.txt', 'w+') as file:

    # Write summary data into the output.txt file and print it to the therminal
    for line in report:
        print(line.strip('\n'))
        file.write(line)