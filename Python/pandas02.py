import csv  
with open('csv-file.txt') as csv_file:  
    csv_reader = csv.reader(csv_file, delimiter=',')  
line_count = 0
for row in csv_reader:   
    line_count += 1
    if line_count == 3:  
        print(row)  
'''
for row in csv_reader:   
    content = list(row[i] for i in included_cols)
print(content)
              
'''
        