 

# Program extracting first column 
import xlrd 
import xlwt
import xlsxwriter 
loc = ("C:/Users/ARUNBABU/Desktop/Mashupstack/Python/parvathy.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
for i in range(sheet.nrows):
	list1 = sheet.cell_value(i, 0)
	print(list1) 

row = 0
column = 0
  
# Workbook() takes one, non-optional, argument  
# which is the filename that we want to create. 
workbook = xlsxwriter.Workbook('hello2.xlsx') 
  
# The workbook object is then used to add new  
# worksheet via the add_worksheet() method. 
worksheet = workbook.add_worksheet() 
  
# Use the worksheet object to write 
# data via the write() method. 


for item in list1 : 
  
    # write operation perform 
    worksheet.write(row,column,item) 
  
    # incrementing the value of row by one 
    # with each iteratons. 
    row += 1
      
workbook.close() 

 

