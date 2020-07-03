# bring in dependencies
import os
import csv
values=[]
dates=[]
delta=[0]
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
    for i in range(0, len(values)-1):
        delta[i] = values[i]-values[i+1]
        delta.append(values[i]-values[i+1])
        # print(delta[i])
        # print(values[i])
        # print(values[i+1])

    # values=[int(i)for i in values]  
    delta=[int(i) for i in delta]  
    total_delta=sum(delta)
    total_value= sum(values)
    max_value=max(values)
    min_value=min(values)
    total_months=len(values)
    # print(len(delta))
    # print(len(values))
    # print(total_value)
    # print(max_value)
    # print(min_value)
    max_spot=values.index(max_value)
    min_spot=values.index(min_value)
    Average_change = round(total_delta/len(delta),2)
    max_date = dates[max_spot]
    min_date = dates[min_spot]
    print(f' Finacial Analysis \n Total: ${total_value} \n Average Change: ${Average_change} \
        \n Greatest Increase in Profits: {max_date} (${max_value}) \n Greatest Decrease in Profits : {min_date} (${min_value})')

outpath=os.path.join('..', 'python-challenge', 'pybank_out.txt')

with open(outpath, 'w') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter = ",")
    csvwriter.writerow([f' Finacial Analysis \n Total: ${total_value} \n Average Change: ${Average_change} \
        \n Greatest Increase in Profits: {max_date} (${max_value}) \n Greatest Decrease in Profits : {min_date} (${min_value})'])
    



    
       
