import csv 

filename = './traincopy.csv'

under_four = ''
over_four = ''

with open(filename,'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    header = ','.join(header)+'\n'

    for row in csvreader:
        if int(row[0])<=4:
            line = ','.join(row) +'\n'
            under_four += line
        else:
            line = ','.join(row) +'\n'
            over_four += line
            

with open('under.csv','w') as f:
    f.write(header)
    f.write(under_four)

with open('over.csv', 'w') as f:
    f.write(header)
    f.write(over_four)