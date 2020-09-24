import hashlib
import csv
from collections import OrderedDict
import operator

def hash_password_hack(input_file_name, output_file_name):
    hashes = list()
    hashesList = list()
    names = list()
    row = 0
    hashrow = 0
    secrow = 0
    i = 0
    mylist = list()


    with open(input_file_name, 'r') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            name = row[0]
            names.append(name)
            mynumbers = list()
            for hashNum in row[1:]:
                mynumbers.append(hashNum)
                hashes.append(mynumbers[0])
        # print(hashes)
        
        for secrow in range(0,9999):
            hashesList.append(hashlib.sha256(str(secrow).encode('utf-8')).hexdigest())
    #         # print(hashesList[row])
    #         if hashesList[secrow] == hashes[0]:
    #             print(secrow)
    #             secrow = secrow+1
    # # print(names)


    # print(hashesList)
    # print(hashes)

    for finalrow in range(0,9999):
        if i>=len(hashes):
                break
        if hashesList[finalrow] == hashes[i]:
            mylist.append([names[i],str(finalrow)])
            
            finalrow = finalrow+1
            i = i+1
    print(mylist)

    with open(output_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in mylist:
            writer.writerow(row)
            



hash_password_hack('input.csv','output.csv')