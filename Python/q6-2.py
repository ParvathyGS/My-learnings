import os
path = "C:/Users/ARUNBABU/Desktop/Mashupstack/Python/q6-2-folder"

dirs = os.listdir(path)

for file in dirs:
	mon = file[2:4]
	mon_str = str(mon)
	#print(mon_str)
	month = {"01" : "Jan","02" : "Feb","03" : "Mar","04" : "Apr","05" : "May","06" : "Jun",
	"07" : "Jul","08" : "Aug","09" : "Sep","10" : "Oct","11" : "Nov","12" : "Dec"}
	for x in month:
		if x == mon_str:
			print(month[x] + " - " + (file))
	