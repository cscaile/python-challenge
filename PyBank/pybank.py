# bring in dependencies
import os
import csv
import numpy as np
values=[]
dates=[]
delta=[]
# delta = 0
csvpath=os.path.join('..', 'python-challenge', 'PyBank.csv')

#open the csv file
with open(csvpath, 'r') as csv_file:

    csv_reader=csv.reader(csv_file,delimiter=',')
    next(csv_reader)

    
    for row in csv_reader:
        date_=row[0]
        value=row[1]
        dates.append(row[0])
        values.append(row[1])

    values=[int(i)for i in values]  
    for i in range(1, len(values)):
        delta_row = values[i]-values[i-1]
        delta.append(delta_row)
        # print(delta[i])
        # print(values[i])
        # print(values[i+1])

    # values=[int(i)for i in values]  
    delta=[int(i) for i in delta]  
    total_delta=sum(delta)
    total_value= sum(values)
    max_value=max(delta)
    min_value=min(delta)
    total_months=len(values)
    # print(delta)
    # print(total_delta)
    # print(len(delta))
    # print(np.mean(delta))
    # print(len(delta))
    # print(len(values))
    # print(total_value)
    # print(max_value)
    # print(min_value)
    max_spot=delta.index(max_value)
    min_spot=delta.index(min_value)
    Average_change = round(total_delta/len(delta),2)
    max_date = dates[max_spot]
    min_date = dates[min_spot]
    print(f' Finacial Analysis \n Total Months: {total_months}  \n Total: ${total_value} \n Average Change: ${Average_change} \
        \n Greatest Increase in Profits: {max_date} (${max_value}) \n Greatest Decrease in Profits : {min_date} (${min_value})')

outpath=os.path.join('..', 'python-challenge', 'pybank_out.txt')

with open(outpath, 'w') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter = ",")
    csvwriter.writerow([f' Finacial Analysis \n Total Months: {total_months} \n Total: ${total_value} \n Average Change: ${Average_change} \
        \n Greatest Increase in Profits: {max_date} (${max_value}) \n Greatest Decrease in Profits : {min_date} (${min_value})'])
    



    
       
