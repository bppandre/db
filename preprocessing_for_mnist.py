import csv 

filename = './traincopy.csv'

under_four = []
over_four = []

with open(filename,'r') as csvfile:
    
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    header = ','.join(header)+'\n'

    for row in csvreader:
        if int(row[0])<=4:
            label = row[0]
            pixels = ''.join(row[1:])
            under_four.append([label,pixels])
        else:
            label = row[0]
            pixels = ''.join(row[1:])
            over_four.append([label,pixels])


# here some code needs to add it to the db