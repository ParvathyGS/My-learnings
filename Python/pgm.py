import csv
with open('parvathy.xlsx') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=' ')
	line_count = 0
	for column in csv_reader:
		if line_count == 0:
			print(''.join(column))
			line_count += 1
