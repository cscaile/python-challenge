# bring in dependencies
import os
import csv
total_voters=[]
Khan_votes=[]
Correy_votes=[]
Li_votes=[]
O_votes=[]
Vote_list=[]

csvpath=os.path.join('..', 'python-challenge', 'PyPoll.csv')

#open the csv file
with open(csvpath, 'r') as csv_file:

    csv_reader=csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        voter_id=row[0]
        County=row[1]
        Candidate=row[2]
        total_voters.append(row[0])
        Vote_list.append(row[2])
    # print(len(total_voters))
    for votes in Vote_list:
        if votes=="Khan":
            Khan_votes.append(row[2])
        elif votes=="Correy":
            Correy_votes.append(row[2])
        elif votes=="Li":
            Li_votes.append(row[2])
        elif votes=="O'Tooley":
            O_votes.append(row[2])
    # print(len(Khan_votes))
    # print(len(Correy_votes))
    # print(len(Li_votes))
    # print((len(Khan_votes)/(len(total_voters))))
    # print((len(Correy_votes)/(len(total_voters))))
    # print((len(Li_votes)/(len(total_voters))))
    TV=len(total_voters)
    VFK=len(Khan_votes)
    VFC=len(Correy_votes)
    VFL=len(Li_votes)
    VFO=len(O_votes)
    PFK=round(VFK/TV*100,5)
    PFC=round(VFC/TV*100,5)
    PFL=round(VFL/TV*100,5)
    PFO=round(VFO/TV*100,5)
    print('Election Results')
    print('-----------------')
    print(f'Total Votes {TV}')
    print('-----------------')
    print(f'Khan: {PFK}% ({VFK})')
    print(f'Correy: {PFC}% ({VFC})')
    print(f'Li: {PFL}% ({VFL})')
    print(f"O'Tooley: {PFO}% ({VFO})")
    print('-----------------')
    if PFK > PFC and PFK >PFL and PFK>PFO:
        Winner = "Khan"
    elif PFC > PFK and PFC > PFL and PFC > PFO:
        Winner = "Correy"
    elif PFL>PFK and PFL> PFC and PFL > PFO:
        Winner = "Li"
    elif PFO>PFK and PFO>PFC and PFO>PFL:
        Winner = "O'Tolley"
    print(f'Winner: {Winner}')

output_path = os.path.join('..', 'python-challenge', 'pypoll_out.txt') 

with open(output_path, 'w') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter = ",")
    csvwriter.writerow([f'Election Results \n  ----------------- \n Total Votes {TV} \n ----------------- \n Khan: {PFK}% ({VFK}) \n Correy: {PFC}% ({VFC}) \
    \n Li: {PFL}% ({VFL})\n O Tooley: {PFO}% ({VFO})\n ----------------- \n Winner: {Winner}'])

# with open(output_path, 'w') as csvfile:
#     csvwriter=csv.writer(csvfile, delimiter = ",")
#     csvwriter.writerow([f'(('Election Results'),
#         ('-----------------'),
#         ('Total Votes {TV}'),
#         ('-----------------'),
#         ('Khan: {PFK}% ({VFK})'),
#         ('Correy: {PFC}% ({VFC})'),
#         ('Li: {PFL}% ({VFL})'),
#         ("O'Tooley: {PFO}% ({VFO})"),
#         ('-----------------'),
#         ('Winner: {Winner}'))])
