"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #created an empty list
melons_sold = [] #created an empty list

f = open('sales-report.txt') #created a file object and opened ot

for line in f: #for each line in file object
    line = line.rstrip() #strip whitepsace to right
    entries = line.split('|') #split at delimiter and create list
    salesperson = entries[0] #assign first item in line list to salesperson var
    melons = int(entries[2]) #assign the third item in list to var, typecast it to an int

    if salesperson in salespeople: #if person in each list thats a salesperson is true
        position = salespeople.index(salesperson) #return the position of salesperson in salespeople list, assign to var
        melons_sold[position] += melons  #melon count increasing
        
    else:
        salespeople.append(salesperson) #add salesperson to salespeople list
        melons_sold.append(melons)      #add melons to melons sold list


for i in range(len(salespeople)): #range is to gen iterable sequence of 0 to length of salesperson list, and for each iterable:
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print "name sold X amount"

#more: https://fellowship.hackbrightacademy.com/materials/wmt5/homework/salesperson-report/solution/index.html#notes

#^^ALSO:# Loop over indices of `salespeople` and use it to index into `salespeople` and
# `melons_sold`.

#didnt close file object